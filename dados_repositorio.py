import requests
import pandas as pd
from dotenv import load_dotenv
import os

class DadosRepositorios:
    def __init__(self, usuario):
        self.usuario = usuario
        self.url_base = 'https://api.github.com'
        load_dotenv()
        self.token = os.getenv('TOKEN_GITHUB')
        self.headers = {'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}
    
    def _lista_repositorio(self):
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
        nomes = []
        for pagina in lista_de_repositorios:
            for repositorio in pagina:
                try:
                    nomes.append(repositorio['name'])
                except:
                    pass
        return nomes
    
    def _linguagens_repositorios(self, lista_de_repositorios: list):
        linguagens = []
        for pagina in lista_de_repositorios:
            for repositorio in pagina:
                try:
                    linguagens.append(repositorio['language'])
                except:
                    pass
        return linguagens
    
    def criar_df(self):
        repositorios = self._lista_repositorio()
        nomes = self._nomes_repositorios(repositorios)
        linguagens = self._linguagens_repositorios(repositorios)

        dados = pd.DataFrame()
        dados['Nome Repositorio'] = nomes
        dados['Linguagem de Programacao'] = linguagens 

        return dados
    
    def gerar_csv(self):
        dados = self.criar_df()
        dados.to_csv(f'Dados\Dados {self.usuario.capitalize()}.csv', sep=',', index=False)
        

