from manipula_repositorio import ManipulaRepositorios
from dados_repositorio import DadosRepositorios
import os
from dotenv import load_dotenv


if __name__ == '__main__':

    load_dotenv()
    usuario = os.getenv('USUARIO')

    netflix = DadosRepositorios('netflix')
    df = netflix.criar_df()
    print(df)
    netflix.gerar_csv()

    spotify = DadosRepositorios('spotify')
    df = spotify.criar_df()
    print(df)
    spotify.gerar_csv()

    amazon = DadosRepositorios('amzn')
    df = amazon.criar_df()
    print(df)
    amazon.gerar_csv()



    novo_repositorio = ManipulaRepositorios(usuario)
    nome = 'Lingugagens_Repositorios_Empresas'
    novo_repositorio.criar_repositorio(nome, 'Linguagem de Programação utilizadas por grandes empresas')

    novo_repositorio.add_arquivo(nome, 'Dados Amzn.csv', 'Dados\Dados Amzn.csv')
    novo_repositorio.add_arquivo(nome, 'Dados Netflix.csv', 'Dados\Dados Netflix.csv')
    novo_repositorio.add_arquivo(nome, 'Dados Spotify.csv', 'Dados\Dados Spotify.csv')
