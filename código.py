import os
import requests
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from babel.numbers import format_currency

# 🔑 Obter chave da API do ambiente
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not API_KEY:
    raise ValueError("Erro: Chave da API não encontrada. Defina EXCHANGE_RATE_API_KEY nos Secrets do GitHub.")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"
HISTORICO_CSV = "historico_conversoes.csv"

# Buscar lista de moedas disponíveis
def obter_moedas():
    try:
        response = requests.get(BASE_URL + "USD")
        response.raise_for_status()
        data = response.json()
        return list(data.get("conversion_rates", {}).keys())
    except (requests.RequestException, ValueError) as e:
        print(f"Erro ao conectar à API: {e}")
        return []

moedas = obter_moedas()

# Função para realizar a conversão
def converter(moeda_origem, moeda_destino, quantia):
    try:
        if quantia <= 0:
            raise ValueError("O valor deve ser maior que zero.")
    except ValueError:
        print("Erro: Digite um valor válido maior que zero.")
        return None
    
    try:
        response = requests.get(BASE_URL + moeda_origem)
        response.raise_for_status()
        taxas = response.json().get("conversion_rates", {})
        taxa_cambio = taxas.get(moeda_destino)
        if taxa_cambio is None:
            raise ValueError(f"Taxa de câmbio para {moeda_destino} não encontrada.")
    except (requests.RequestException, ValueError) as e:
        print(f"Erro ao buscar os dados: {e}")
        return None
    
    valor_convertido = quantia * taxa_cambio
    print(f"{format_currency(quantia, moeda_origem, locale='pt_BR')} equivale a "
          f"{format_currency(valor_convertido, moeda_destino, locale='pt_BR')}")
    
    # Salvar histórico no CSV
    file_exists = os.path.isfile(HISTORICO_CSV)
    with open(HISTORICO_CSV, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Origem", "Destino", "Valor", "Taxa", "Convertido", "Timestamp"])
        writer.writerow([moeda_origem, moeda_destino, quantia, taxa_cambio, valor_convertido, time.strftime('%Y-%m-%d %H:%M:%S')])
    print("Conversão salva no histórico!")
    return valor_convertido

# Exemplo de uso sem interface gráfica
if __name__ == "__main__":
    print("Moedas disponíveis: ", ", ".join(moedas))
    moeda_origem = input("Digite a moeda de origem (ex: USD, BRL, EUR): ").strip().upper()
    moeda_destino = input("Digite a moeda de destino: ").strip().upper()
    try:
        quantia = float(input("Digite o valor a converter: ").strip())
    except ValueError:
        print("Erro: Digite um número válido.")
    else:
        converter(moeda_origem, moeda_destino, quantia)
