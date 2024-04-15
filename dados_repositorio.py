import requests
import base64
from dotenv import load_dotenv
import os

class ManipulaRepositorios:
    """Classe para manipular repositórios no GitHub."""

    def __init__(self, usuario):
        """
        Inicializa a classe ManipulaRepositorios.

        Args:
            usuario (str): O nome do usuário do GitHub.
        """
        self.usuario = usuario
        self.url_base = 'https://api.github.com'
        load_dotenv()
        self.token = os.getenv('TOKEN_GITHUB')
        self.headers = {'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}

    def criar_repositorio(self, nome, descricao):
        """
        Cria um novo repositório no GitHub.

        Args:
            nome (str): O nome do novo repositório.
            descricao (str): A descrição do novo repositório.
        """
        dados = {
            "name": nome,
            "description": descricao,
            "private": True
        }
        resposta = requests.post(f'{self.url_base}/user/repos', json=dados, headers=self.headers)
        print(f'Status da criação do repositório: {resposta.status_code}')

    def add_arquivo(self, nome_repositorio, nome_arquivo, caminho_arquivo):
        """
        Adiciona um novo arquivo a um repositório existente no GitHub.

        Args:
            nome_repositorio (str): O nome do repositório ao qual o arquivo será adicionado.
            nome_arquivo (str): O nome do arquivo a ser adicionado.
            caminho_arquivo (str): O caminho local do arquivo a ser adicionado.
        """
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
