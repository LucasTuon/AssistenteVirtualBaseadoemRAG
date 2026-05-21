# Assistente Virtual Académico Baseado em RAG: Uma Abordagem Local com LLMs para Apoio ao Aprendizado

Este repositório contém a implementação prática de um pipeline de Geração Aumentada por Recuperação (RAG) desenvolvido localmente para atuar como assistente na disciplina de Inteligência Artificial. O sistema utiliza uma base de dados vetorial para contextualizar as respostas de um modelo de linguagem (LLM) estritamente baseado no material didático fornecido pelo professor, mitigando alucinações e garantindo a rastreabilidade das fontes.

---

## 1. Como Rodar a Aplicação

Siga o passo a passo abaixo para configurar o ambiente e executar o assistente virtual em sua máquina local.

### Requisitos Obrigatórios
* **Python:** Versão 3.10 ou superior instalada.
* **Armazenamento Livre:** Cerca de 3 GB livres para os modelos de IA (Embeddings e LLM).

### Passo 1: Instalação e Configuração do Ollama
O Ollama é o motor responsável por executar o Modelo de Linguagem Amplo (LLM) localmente na sua máquina.

1. Acesse o site oficial do Ollama: [https://ollama.com](https://ollama.com).
2. Baixe e instale a versão correspondente ao seu sistema operacional.
3. **VERIFICAÇÃO CRÍTICA:** Após a instalação, certifique-se de que o Ollama está ativamente rodando em segundo plano. No Windows, confirme isso procurando pelo **ícone da Lhama na barra de ferramentas (ícones ocultos, próximo ao relógio do sistema)**. O sistema não funcionará se o motor estiver desligado.

### Passo 2: Baixar o Modelo de Linguagem (LLM)
Com o Ollama ativo, abra o seu terminal (Prompt de Comando ou PowerShell no Windows) e execute o comando abaixo para realizar o download do modelo adotado no projeto:

```bash
ollama pull llama3.2
```

Aguarde até que o terminal exiba a mensagem de sucesso (success).  

### Passo 3: Instalação das Dependências do Python

Navegue até a pasta raiz do projeto usando o terminal e instale todas as bibliotecas necessárias (incluindo o Streamlit e o LangChain) agrupadas em um único comando pip:

```bash
pip install streamlit langchain-community langchain-huggingface faiss-cpu sentence-transformers
```

### Passo 4: Execução do Sistema  

Você possui duas formas de colocar o assistente virtual no ar:  

1. Via Script Automatizado: 
Dê dois cliques no arquivo `iniciar_assistente.bat` presente na pasta raiz. Ele abrirá o terminal e lançará a interface automaticamente.
2. Via Terminal: 
Execute manualmente o comando abaixo no terminal da pasta do projeto:
```bash
streamlit run app.py
```
O Streamlit abrirá automaticamente uma aba no seu navegador padrão. Na primeira execução, o sistema pode levar cerca de um minuto para carregar o modelo de embeddings na memória RAM. Assim que o aviso verde aparecer, o chat estará pronto para uso.

## 2. Estrutura do Repositório
preparacao_dados.ipynb: Jupyter Notebook responsável pelo pipeline de extração, chunking, embedding e criação do índice vetorial local.

app.py: Script Python principal contendo a interface gráfica do usuário, a lógica de memória do chat, a busca vetorial e a LLM.

iniciar_assistente.bat: Script de inicialização  do Windows para execução rápida do projeto.

banco_faiss_ia/: Diretório contendo os arquivos indexados e serializados do banco de dados vetorial FAISS (gerados pelo notebook).

## 3. Autores

- Lucas Tuon de Matos - RA: 10417987

- Matteo Porcare - RA: 10418276

- Tomy Goldberg Boimel - RA: 10417109

- Yuri Milliet - RA: 10417884

Para mais informações consulte o RelatorioProjetoIA.pdf
