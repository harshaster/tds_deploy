import streamlit as st

st.title('Division of two numbers')
st.subheader('Harshit Katiyar')
st.text('21f1006135')

num1 = st.text_input('Enter first number : ')
num2 = st.text_input('Enter second number : ')

btn = st.button('Calculate')

out = f"{num1} / {num2} = {float(num1) / float(num2)}"

if btn:
    st.markdown(f"## {out}")