import streamlit as st  # importa a biblioteca Streamlit, apelidada de "st"

texto = st.text_input("Digite seu nome") # cria um campo de texto na tela

if st.button("Enviar"): # cria um botão , o bloco abaixo só roda quando clicado
    st.write(f"Olá {texto}, bem vindo!") # exibe o texto digitado na tela