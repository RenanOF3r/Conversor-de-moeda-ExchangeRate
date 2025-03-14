import os
import requests
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from babel.numbers import format_currency
import tkinter as tk
from tkinter import ttk, messagebox

# Obter chave da API do ambiente
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not API_KEY:
    messagebox.showerror("Erro", "Chave da API não encontrada.")
    exit()

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
        messagebox.showerror("Erro", f"Erro ao conectar à API: {e}")
        return []

moedas = obter_moedas()

# Função para realizar a conversão
def converter():
    moeda_origem = moeda_origem_var.get()
    moeda_destino = moeda_destino_var.get()
    quantia = entrada_valor.get()

    try:
        quantia = float(quantia)
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
    resultado_var.set(f"{format_currency(quantia, moeda_origem, locale='pt_BR')} equivale a "
                      f"{format_currency(valor_convertido, moeda_destino, locale='pt_BR')}")
    
    # Salvar histórico no CSV
    file_exists = os.path.isfile(HISTORICO_CSV)
    with open(HISTORICO_CSV, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Origem", "Destino", "Valor", "Taxa", "Convertido", "Timestamp"])
        writer.writerow([moeda_origem, moeda_destino, quantia, taxa_cambio, valor_convertido, time.strftime('%Y-%m-%d %H:%M:%S')])
    
    messagebox.showinfo("Sucesso", "Conversão salva no histórico!")

# Exibir histórico de conversões
def mostrar_historico():
    if not os.path.isfile(HISTORICO_CSV):
        messagebox.showinfo("Histórico", "Nenhuma conversão encontrada.")
        return
    
    df = pd.read_csv(HISTORICO_CSV)
    df_last = df.tail(10)  # Mostrar apenas as 10 últimas conversões
    
    janela_historico = tk.Toplevel(root)
    janela_historico.title("Histórico de Conversões")

    text_area = tk.Text(janela_historico, height=15, width=80)
    text_area.pack(padx=10, pady=10)
    
    text_area.insert(tk.END, df_last.to_string(index=False))

# Exibir gráfico do histórico
def mostrar_grafico():
    if not os.path.isfile(HISTORICO_CSV):
        messagebox.showinfo("Histórico", "Nenhuma conversão encontrada para o gráfico.")
        return
    
    df = pd.read_csv(HISTORICO_CSV)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df_last = df.tail(10)  # Mostrar apenas as 10 últimas conversões
    
    plt.figure(figsize=(10, 5))
    plt.plot(df_last['Timestamp'], df_last['Convertido'], marker='o', linestyle='-')
    plt.xlabel("Data e Hora")
    plt.ylabel("Valor Convertido")
    plt.title("Últimas Conversões")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Criando interface gráfica
root = tk.Tk()
root.title("Conversor de Moedas")

# Labels e Entradas
ttk.Label(root, text="Moeda de Origem:").grid(row=0, column=0, padx=10, pady=5)
moeda_origem_var = tk.StringVar(value="USD")
moeda_origem_menu = ttk.Combobox(root, textvariable=moeda_origem_var, values=moedas)
moeda_origem_menu.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Moeda de Destino:").grid(row=1, column=0, padx=10, pady=5)
moeda_destino_var = tk.StringVar(value="BRL")
moeda_destino_menu = ttk.Combobox(root, textvariable=moeda_destino_var, values=moedas)
moeda_destino_menu.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Valor:").grid(row=2, column=0, padx=10, pady=5)
entrada_valor = ttk.Entry(root)
entrada_valor.grid(row=2, column=1, padx=10, pady=5)

# Botão de conversão
botao_converter = ttk.Button(root, text="Converter", command=converter)
botao_converter.grid(row=3, column=0, columnspan=2, pady=10)

# Resultado da conversão
resultado_var = tk.StringVar()
label_resultado = ttk.Label(root, textvariable=resultado_var, font=("Arial", 12, "bold"), foreground="blue")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

# Botões de histórico e gráfico
botao_historico = ttk.Button(root, text="Ver Histórico", command=mostrar_historico)
botao_historico.grid(row=5, column=0, pady=5)

botao_grafico = ttk.Button(root, text="Ver Gráfico", command=mostrar_grafico)
botao_grafico.grid(row=5, column=1, pady=5)

# Iniciar interface
root.mainloop()
