# INTEGRANTES DO GRUPO:
# Matteo Porcare           10418276
# Tomy Goldberg Boimel     10417109
# Yuri Milliet             10417884
# Lucas Tuon de Matos      10417987

import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# CONFIGURACAO VISUAL
st.set_page_config(page_title="Assistente de IA", page_icon="🤖")
st.title("Assistente Virtual - Inteligência Artificial 📚")

# Inicializa Ollama local
llm= Ollama(model="llama3.2")

# Carrega o banco vetorial com o modelo multilingue
@st.cache_resource 
def carregar_banco():
    embeddings = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")
    return FAISS.load_local("./banco_faiss_ia", embeddings, allow_dangerous_deserialization=True)

try:
    banco_vetorial = carregar_banco()
    st.success("Banco de materiais carregado com sucesso!!!")
except Exception as e:
    st.error(f"Erro ao carregar o banco: {e}")

# MEMORIA DO CHAT
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

# INTERACAO COM USUARIO
pergunta = st.chat_input("Digite sua dúvida sobre a disciplina...")

if pergunta:
    # Mostra a pergunta do usuário
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    st.chat_message("user").write(pergunta)
    
    # Busca os 3 pedacos mais parecidos com a pergunta
    resultados = banco_vetorial.similarity_search(pergunta, k=3)
    contexto_recuperado = "\n\n".join([f"[Fonte: {doc.metadata['source']}]\n{doc.page_content}" for doc in resultados])
    
    historico_formatado = ""
    for m in st.session_state.mensagens[-5:-1]: # ignora a pergunta atual que já vai no final do prompt
        papel = "ALUNO" if m["role"] == "user" else "ASSISTENTE"
        historico_formatado += f"{papel}: {m['content']}\n"
    
    # Prompt para evitar alucinacoes
    prompt = f"""Você é um assistente virtual acadêmico da disciplina de Inteligência Artificial.
Sua tarefa é responder à pergunta do aluno baseando-se EXCLUSIVAMENTE no contexto fornecido abaixo.
Se a resposta não estiver no contexto, diga claramente: "Não possuo informações suficientes no material didático para responder a isso."
Nunca invente informações. Ao final da sua resposta, cite o nome dos arquivos fonte utilizados.

HISTÓRICO RECENTE DA CONVERSA:
{historico_formatado}

CONTEXTO DOS MATERIAIS DO PROFESSOR:
{contexto_recuperado}

PERGUNTA DO ALUNO: 
{pergunta}

RESPOSTA:"""

    # Digita palavra por palavra pra nao parecer travado
    with st.chat_message("assistant"):
        st.write("*Processando a resposta...*")
        # O st.write_stream pega os pedacinhos de texto conforme o Ollama gera
        resposta_final = st.write_stream(llm.stream(prompt))

    # Salva a resposta da IA na memoria
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_final})
    
    # Mostra o contexto bruto em um menu abaixo da resposta
    with st.expander("Ver trechos originais recuperados pelo sistema"):
        st.write(contexto_recuperado)