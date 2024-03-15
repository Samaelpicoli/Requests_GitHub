import requests
import base64
from dotenv import load_dotenv
import os

class ManipulaRepositorios():
    def __init__(self, usuario):
        self.usuario = usuario
        self.url_base = 'https://api.github.com'
        load_dotenv()
        self.token = os.getenv('TOKEN_GITHUB')
        self.headers = {'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}

    def criar_repositorio(self, nome, descricao):
        dados = {
            "name": nome,
            "description": descricao,
            "private": True
        }
        resposta = requests.post(f'{self.url_base}/user/repos', json=dados, headers=self.headers)
        print(f'Status da criação do repositório: {resposta.status_code}')

    def add_arquivo(self, nome_repositorio, nome_arquivo, caminho_arquivo):
        with open(caminho_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
        conteudo_codificado = base64.b64encode(conteudo)

        url = f'{self.url_base}/repos/{self.usuario}/{nome_repositorio}/contents/{nome_arquivo}'
        dados = {
            'message': 'Adicionando um novo arquivo',
            'content': conteudo_codificado.decode('utf-8')
        }

        requisicao = requests.put(url, headers=self.headers, json=dados)
        print(requisicao.status_code)



        