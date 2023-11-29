import streamlit as st
import requests
import json
import requests

# URL do servidor Flask
url = "http://127.0.0.1:5000"

def cadastra_usuario(email, senha, time):
    payload = {"email": email, "senha": senha, "clube": time}
    response = requests.post(f"{url}/cadastro", json=payload)
    return response

def login(email, senha):
    payload = {"email": email, "senha": senha}
    response = requests.post(f"{url}/login", json=payload)
    global id_user_atual
    id_user_atual = str(response.headers['usuario'])
    return response

def partidas():
    headers = {'usuario': id_user_atual}
    st.write(headers)
    response =  requests.get(f"{url}/partidas", headers=headers)
    return  json.loads(response.text)


def obter_clube_usuario():
    try:
        header = {'usuario': id_user_atual}
        response = requests.get(f"{url}/get_clube",headers=header)
        response.raise_for_status()
        return response.json()['clube']
    except requests.RequestException as e:
        print(f"Erro ao obter o clube: {e}")
        return None
