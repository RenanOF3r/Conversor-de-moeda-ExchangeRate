# Conversor de Moedas com API de Taxas de Câmbio

Este projeto é um conversor de moedas que utiliza a API **Exchange Rate API** para obter taxas de câmbio em tempo real. O programa permite converter valores entre diferentes moedas e registra o histórico das conversões em um arquivo CSV.

## Funcionalidades
- Obtém a lista de moedas disponíveis via API.
- Converte valores entre diferentes moedas.
- Salva um histórico de conversões em um arquivo CSV.
- Exibe os valores convertidos formatados conforme a localização brasileira.

## Tecnologias Utilizadas
- **Python 3**
- **Requests** para consumo da API de taxas de câmbio.
- **Pandas** para manipulação de dados.
- **Matplotlib** para visualização gráfica (futuras melhorias).
- **CSV** para armazenamento de histórico de conversões.
- **Babel** para formatação de valores monetários.

## Requisitos
Antes de executar o programa, instale as dependências necessárias:
```bash
pip install requests pandas matplotlib babel
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
Para rodar o conversor de moedas, execute o seguinte comando:
```bash
python conversor_moedas.py
```
O programa exibirá as moedas disponíveis e solicitará ao usuário que informe:
1. A moeda de origem.
2. A moeda de destino.
3. O valor a ser convertido.

Exemplo de entrada:
```
Digite a moeda de origem (ex: USD, BRL, EUR): USD
Digite a moeda de destino: BRL
Digite o valor a converter: 100
```
Saída esperada:
```
$100,00 (USD) equivale a R$500,00 (BRL)
Conversão salva no histórico!
```
(O valor convertido depende da taxa de câmbio do momento.)

## Estrutura do Projeto
```
/
|-- conversor_moedas.py   # Arquivo principal do conversor
|-- historico_conversoes.csv  # (Criado automaticamente) Registro de conversões
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
- Criar uma interface gráfica (GUI) para facilitar o uso.
- Implementar um modo offline utilizando dados armazenados previamente.
- Gerar gráficos de variação cambial utilizando `matplotlib`.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme suas necessidades.

Desenvolvido por Renan Fernandes
Contato: renanofernandes@gmail.com
LinkedIn: https://www.linkedin.com/in/renan-oliveira-fernandes-50319b172/
