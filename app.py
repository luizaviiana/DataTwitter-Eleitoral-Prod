import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open("analise.jpg")
st.image(image)

st.title('Data Twitter Eleitoral')
st.text('Aplicação que realiza análise de sentimentos dos candidatos à presidência usando dados do Twitter')

df = pd.read_csv("etapa4_dataframe_final.csv")

candidato_unico = sorted(df['Candidato'].unique())
selecionar_candidato = st.sidebar.multiselect('Candidato', candidato_unico, candidato_unico)

df_candidato_selecionado = df[(df['Candidato'].isin(selecionar_candidato))]

st.dataframe(df_candidato_selecionado)


# utilização do streamlit cloud p colocar no servidor
