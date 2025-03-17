import os
import requests
import csv
import time
from flask import Flask, jsonify, request, render_template
from babel.numbers import format_currency

app = Flask(__name__)

# Configuração da API
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

@app.route('/')
def index():
    return render_template("index.html", moedas=moedas)

@app.route('/converter', methods=['GET'])
def converter():
    moeda_origem = request.args.get("moeda_origem", "").upper()
    moeda_destino = request.args.get("moeda_destino", "").upper()
    try:
        quantia = float(request.args.get("quantia", 0))
        if quantia <= 0:
            return jsonify({"erro": "O valor deve ser maior que zero."}), 400
    except ValueError:
        return jsonify({"erro": "Valor inválido."}), 400

    try:
        response = requests.get(BASE_URL + moeda_origem)
        response.raise_for_status()
        taxas = response.json().get("conversion_rates", {})
        taxa_cambio = taxas.get(moeda_destino)
        if taxa_cambio is None:
            return jsonify({"erro": f"Taxa de câmbio para {moeda_destino} não encontrada."}), 400
    except (requests.RequestException, ValueError) as e:
        return jsonify({"erro": f"Erro ao buscar os dados: {e}"}), 500

    valor_convertido = quantia * taxa_cambio
    resultado = {
        "moeda_origem": moeda_origem,
        "moeda_destino": moeda_destino,
        "quantia": quantia,
        "taxa": taxa_cambio,
        "convertido": valor_convertido,
        "valor_formatado": format_currency(valor_convertido, moeda_destino, locale="pt_BR")
    }

    # Salvar no histórico
    file_exists = os.path.isfile(HISTORICO_CSV)
    with open(HISTORICO_CSV, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Origem", "Destino", "Valor", "Taxa", "Convertido", "Timestamp"])
        writer.writerow([moeda_origem, moeda_destino, quantia, taxa_cambio, valor_convertido, time.strftime('%Y-%m-%d %H:%M:%S')])

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
