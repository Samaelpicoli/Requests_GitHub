from manipula_repositorio import ManipulaRepositorios
from dados_repositorio import DadosRepositorios
import os
from dotenv import load_dotenv
from pathlib import Path


if __name__ == '__main__':

    load_dotenv()
    usuario = os.getenv('USUARIO')
    pasta = Path('Dados').mkdir(exist_ok=True)

    netflix = DadosRepositorios('netflix')
    df = netflix.criar_df()
    print(df)
    netflix.gerar_csv(pasta)

    spotify = DadosRepositorios('spotify')
    df = spotify.criar_df()
    print(df)
    spotify.gerar_csv(pasta)

    amazon = DadosRepositorios('amzn')
    df = amazon.criar_df()
    print(df)
    amazon.gerar_csv(pasta)

    
    


    novo_repositorio = ManipulaRepositorios(usuario)
    nome = 'Lingugagens_Repositorios_Empresas'
    novo_repositorio.criar_repositorio(nome, 'Linguagem de Programação utilizadas por grandes empresas')

    novo_repositorio.add_arquivo(nome, 'Dados Amzn.csv', pasta / 'Dados Amzn.csv')
    novo_repositorio.add_arquivo(nome, 'Dados Netflix.csv', pasta / 'Dados Netflix.csv')
    novo_repositorio.add_arquivo(nome, 'Dados Spotify.csv', pasta / 'Dados Spotify.csv')
