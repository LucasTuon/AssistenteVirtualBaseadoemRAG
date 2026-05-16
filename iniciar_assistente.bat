@echo off
color 0A
title Assistente Virtual - Inteligencia Artificial
echo ===================================================
echo    Iniciando o Assistente Academico...
echo ===================================================
echo.
echo Verificando dependencias...
echo (Certifique-se de que o aplicativo do Ollama esta aberto perto do relogio do Windows)
echo.

:: O comando abaixo inicia o Streamlit automaticamente e abre no navegador padrão
streamlit run app.py

:: Se der erro e fechar, a tela pausa para você conseguir ler o que aconteceu
pause