import streamlit as st

# na primeira execucao a chave nao existe; nos reruns seguintes o valor e preservado
if "total" not in st.session_state:
    st.session_state["total"] = 0

valor = st.number_input("Valor")
somar = st.button("Somar")
zerar = st.button("Zerar")

# os botoes so viram True no rerun imediatamente apos o clique
if somar:
    st.session_state["total"] = st.session_state["total"] + valor

if zerar:
    st.session_state["total"] = 0

# aspas simples dentro da f-string, que esta delimitada por aspas duplas
st.write(f"Total: {st.session_state['total']}")
