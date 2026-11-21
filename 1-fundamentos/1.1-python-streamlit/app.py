import streamlit as st

st.title("Catalogo de PDFs")
st.write("Primeiro app do PDI")

nome = st.text_input("Nome do documento")
paginas = st.slider("Paginas", 1, 200, 50)
clicou = st.button("Classificar")

if clicou:
    st.write(f"{nome} tem {paginas} paginas")