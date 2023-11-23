import streamlit as st
import requests
import json

# URL do servidor Flask
url = "http://127.0.0.1:5000"

def cadastra_usuario(email, senha, time):
    payload = {"email": email, "senha": senha, "clube": time}
    response = requests.post(f"{url}/cadastro", json=payload)
    return response

def login(email, senha,time):
    payload = {"email": email, "senha": senha,"clube":time}
    response = requests.post(f"{url}/login", json=payload)
    return response

def partidas():
    response = requests.get(f"{url}/partidas")
    return response

print(partidas())