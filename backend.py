import requests

cep = input("Insira o seu CEP:")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(f"Você mora na {resposta["logradouro"]}, no Bairro {resposta["bairro"]}, na Cidade de {resposta["localidade"]}, no Estado de {resposta["estado"]}")