# Conversor de Moedas com API de Taxas de Câmbio

Este projeto é um conversor de moedas baseado em **Flask** que utiliza a API **Exchange Rate API** para obter taxas de câmbio em tempo real. Ele permite converter valores entre diferentes moedas e registrar o histórico das conversões em um arquivo CSV.

## Funcionalidades
- Obtém a lista de moedas disponíveis via API.
- Converte valores entre diferentes moedas.
- Interface Web interativa desenvolvida com **HTML, CSS e JavaScript**.
- Salva um histórico de conversões em um arquivo CSV.
- Exibe os valores convertidos formatados conforme a localização brasileira.

## Tecnologias Utilizadas
- **Python 3**
- **Flask** para criação da API Web.
- **Requests** para consumo da API de taxas de câmbio.
- **Babel** para formatação de valores monetários.
- **CSV** para armazenamento de histórico de conversões.
- **HTML, CSS e JavaScript** para a interface do usuário.

## Requisitos
Antes de executar o programa, instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
Ou, manualmente:
```bash
pip install flask requests babel pandas matplotlib
```

## Configuração da Chave da API
Este programa utiliza a API **Exchange Rate API**, e é necessário definir a chave de acesso no ambiente:

1. Obtenha uma chave gratuita em [Exchange Rate API](https://www.exchangerate-api.com/).
2. Defina a variável de ambiente `EXCHANGE_RATE_API_KEY`. No terminal, use:
   ```bash
   export EXCHANGE_RATE_API_KEY="SUA_CHAVE_AQUI"
   ```
   Caso esteja utilizando Windows (PowerShell), use:
   ```powershell
   $env:EXCHANGE_RATE_API_KEY="SUA_CHAVE_AQUI"
   ```

## Como Executar
Para rodar o conversor de moedas, execute os seguintes comandos:
```bash
python app.py
```
O servidor Flask será iniciado e a aplicação poderá ser acessada em:
 **http://127.0.0.1:5000**

A interface exibirá opções para selecionar moedas e converter valores diretamente pelo navegador.

## Estrutura do Projeto
```
/
|-- app.py                 # Código principal do Flask
|-- requirements.txt       # Lista de dependências
|-- historico_conversoes.csv  # (Criado automaticamente) Registro de conversões
|-- templates/
|   ├── index.html        # Interface do usuário
|-- static/
|   ├── style.css         # Arquivo de estilos (opcional)
```

## Histórico de Conversões
Cada conversão realizada é registrada no arquivo `historico_conversoes.csv`, contendo:
- Moeda de origem
- Moeda de destino
- Valor original
- Taxa de câmbio utilizada
- Valor convertido
- Timestamp da operação

## Possíveis Melhorias Futuras
- Melhorar o design da interface usando Bootstrap.
- Implementar cache para evitar consultas repetidas à API.
- Criar gráficos de variação cambial utilizando `matplotlib`.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme suas necessidades.

🔹 Desenvolvido por Renan Fernandes
📧 Contato: renanofernandes@gmail.com  
🔗 LinkedIn: [Perfil](https://www.linkedin.com/in/renan-oliveira-fernandes-50319b172/)


