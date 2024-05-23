import requests
import pandas as pd
from dotenv import load_dotenv
import os

class DadosRepositorios:

    """
    Classe para manipulação e obtenção de dados de repositórios 
    de um usuário do GitHub.
    """

    def __init__(self, usuario):
        """
        Inicializa a classe com o nome de usuário do GitHub, 
        configura a URL base da API do GitHub e carrega 
        o token de autenticação do ambiente.

        Args:
            usuario (str): Nome de usuário do GitHub.
        """
        self.usuario = usuario
        self.url_base = 'https://api.github.com'
        load_dotenv()
        self.token = os.getenv('TOKEN_GITHUB')
        self.headers = {'Authorization': f'Bearer {self.token}', 
                        'X-GitHub-Api-Version': '2022-11-28'}
    
    def _lista_repositorio(self):
        """
        Obtém a lista de repositórios do usuário a partir da API do GitHub.

        Returns:
            list: Lista de repositórios do usuário, com a paginação.
        """
        lista_de_repositorios = []
        pagina = 1
        while True:
            url = f'{self.url_base}/users/{self.usuario}/repos?page={pagina}'
            requisicao = requests.get(url, headers=self.headers)
            repositorios = requisicao.json()

            if len(repositorios) == 0:
                break

            lista_de_repositorios.append(repositorios)
            pagina = pagina + 1

        return lista_de_repositorios
    
    def _nomes_repositorios(self, lista_de_repositorios: list):
        """
        Extrai os nomes dos repositórios de uma lista de repositórios.

        Args:
            lista_de_repositorios (list): Lista de repositórios paginada.

        Returns:
            list: Lista com os nomes dos repositórios.
        """
        nomes = []
        for pagina in lista_de_repositorios:
            for repositorio in pagina:
                try:
                    nomes.append(repositorio['name'])
                except:
                    pass
        return nomes
    
    def _linguagens_repositorios(self, lista_de_repositorios: list):
        """
        Extrai as linguagens de programação dos repositórios de 
        uma lista de repositórios.

        Args:
            lista_de_repositorios (list): Lista de repositórios paginada.

        Returns:
            list: Lista com as linguagens de programação dos repositórios.
        """
        linguagens = []
        for pagina in lista_de_repositorios:
            for repositorio in pagina:
                try:
                    linguagens.append(repositorio['language'])
                except:
                    pass
        return linguagens
    
    def criar_df(self):
        """
        Cria um DataFrame com os nomes e linguagens de programação 
        dos repositórios do usuário.

        Returns:
            pd.DataFrame: DataFrame contendo os dados dos repositórios.
        """
        repositorios = self._lista_repositorio()
        nomes = self._nomes_repositorios(repositorios)
        linguagens = self._linguagens_repositorios(repositorios)

        dados = pd.DataFrame()
        dados['Nome Repositorio'] = nomes
        dados['Linguagem de Programacao'] = linguagens 
        print(dados)
        return dados
    
    def gerar_csv(self, pasta):
        """
        Gera um arquivo CSV com os dados dos repositórios do usuário.

        O arquivo CSV é salvo no diretório 'Dados' com o nome 'Dados <usuario>.csv'.
        """
        dados = self.criar_df()
        nome_arquivo = pasta / f'Dados {self.usuario.capitalize()}.csv'
        dados.to_csv(nome_arquivo, sep=',', index=False)
        
