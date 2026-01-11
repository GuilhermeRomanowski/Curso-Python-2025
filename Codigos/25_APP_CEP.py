import streamlit as st
import requests
import pandas as pd

url = "https://viacep.com.br/ws/{cep}/json/"


st.title("Bucas por CEP")
cep = st.text_input("Entre com o CEP")

if cep != "":
   
    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.write(data)
    
    except Exception as err:
        st.error("Entre com um CEP válido!")










