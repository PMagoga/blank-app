import streamlit as st
import numpy as np
import pandas as pd


st.title("Aplicativo da Subtenência")

st.sidebar.title('Barra Lateral')
st.sidebar.write("Escolha um item")
st.sidebar.selectbox('Selecione uma opção', ['Opção 1', 'Opção 2', 'Opção 3'])
