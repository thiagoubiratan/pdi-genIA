import streamlit as st

valor_um = st.number_input("Digite o primeiro valor")
valor_dois = st.number_input("Digite o segundo valor")

st.write("Selecione a operação abaixo:")

col_soma, col_subtracao, col_multiplicacao, col_divisao = st.columns(4);
resultado = 0

with col_soma:
    if st.button("[ + ] Soma"):
        resultado = valor_um + valor_dois
        
with col_subtracao:
    if st.button("[ - ] Subtração"):
        resultado = valor_um - valor_dois

with col_multiplicacao:
    if st.button("[ x ] Multiplicação"):
        resultado = valor_um * valor_dois

with col_divisao:
    if st.button("[ / ] Divisão"):
        try:
            resultado = valor_um / valor_dois
        except ZeroDivisionError:
            st.error("Não é possível dividir por zero")


st.write(f"o resultado é: {resultado}")