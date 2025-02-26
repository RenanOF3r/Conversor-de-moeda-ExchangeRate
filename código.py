import os
import requests
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from babel.numbers import format_currency

# Chave da API fornecida no código original
API_KEY = "df337cbc7cc4b0c9568b8bbc"
BASE_URL = f"https://v6.exchangerate-api.com/v6/df337cbc7cc4b0c9568b8bbc/latest/"
HISTORICO_CSV = "historico_conversoes.csv"

# Buscar lista de moedas disponíveis
def obter_moedas():
    try:
        response = requests.get(BASE_URL + "USD")
        response.raise_for_status()
        data = response.json()
        return list(data.get("conversion_rates", {}).keys())
    except (requests.RequestException, ValueError) as e:
        messagebox.showerror("Erro", f"Erro ao conectar à API: {e}")
        return []

moedas = obter_moedas()

# Função para realizar a conversão
def converter():
    moeda_origem = combo_origem.get()
    moeda_destino = combo_destino.get()
    try:
        quantia = float(entry_valor.get())
        if quantia <= 0:
            raise ValueError("O valor deve ser maior que zero.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido maior que zero.")
        return
    
    try:
        response = requests.get(BASE_URL + moeda_origem)
        response.raise_for_status()
        taxas = response.json().get("conversion_rates", {})
        taxa_cambio = taxas.get(moeda_destino)
        if taxa_cambio is None:
            raise ValueError(f"Taxa de câmbio para {moeda_destino} não encontrada.")
    except (requests.RequestException, ValueError) as e:
        messagebox.showerror("Erro", f"Erro ao buscar os dados: {e}")
        return
    
    valor_convertido = quantia * taxa_cambio
    resultado_label.config(text=f"{format_currency(quantia, moeda_origem, locale='pt_BR')} equivale a "
                              f"{format_currency(valor_convertido, moeda_destino, locale='pt_BR')}")
    
    # Salvar histórico no CSV
    file_exists = os.path.isfile(HISTORICO_CSV)
    with open(HISTORICO_CSV, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Origem", "Destino", "Valor", "Taxa", "Convertido", "Timestamp"])
        writer.writerow([moeda_origem, moeda_destino, quantia, taxa_cambio, valor_convertido, time.strftime('%Y-%m-%d %H:%M:%S')])
    messagebox.showinfo("Sucesso", "Conversão salva no histórico!")

# Criar interface gráfica
root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("400x300")

frame = ttk.Frame(root, padding=10)
frame.pack(expand=True, fill=tk.BOTH)

# Combobox para selecionar moedas
ttk.Label(frame, text="Moeda de Origem:").pack()
combo_origem = ttk.Combobox(frame, values=moedas)
combo_origem.pack()
combo_origem.set("USD")

ttk.Label(frame, text="Moeda de Destino:").pack()
combo_destino = ttk.Combobox(frame, values=moedas)
combo_destino.pack()
combo_destino.set("BRL")

# Campo para inserir o valor
ttk.Label(frame, text="Valor a Converter:").pack()
entry_valor = ttk.Entry(frame)
entry_valor.pack()

# Botão para converter
botao_converter = ttk.Button(frame, text="Converter", command=converter)
botao_converter.pack(pady=10)

# Rótulo para mostrar o resultado
resultado_label = ttk.Label(frame, text="")
resultado_label.pack()

root.mainloop()
