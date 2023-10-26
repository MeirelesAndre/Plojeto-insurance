import streamlit as st

st.set_page_config(page_title='DNC')

# Elementos de texto
st.header('Título: Página principal')
st.markdown('Aqui um **texto** em [markdown](https://www.markdownguide.org/basic-syntax/)')

# Página lateral
st.sidebar.header('Texto principal sidebar')

# Widgets
nome = st.text_input('Qual o seu nome?')
st.write(f'Muito prazer, {nome}!')

idade = st.number_input('Qual a sua idade?', value=18)
st.write(f'Você tem {idade} anos.')

# Widgets página lateral
super_poderes = ['Jedi dos dados', 'Mestre dos dados', 'Data Expert']
superpoder = st.sidebar.selectbox('Qual o seu super-poder?', options=super_poderes)
st.sidebar.write(f'Seu super-poder é {superpoder}!')

