# Requests_GitHub

# Sobre o projeto

Esse projeto é um Projeto desenvolvido junto ao curso "Python e APIs: conhecendo a biblioteca Requests" da Alura, 
onde é realizado extrações pela API do GitHub sobre nome de repositórios e a linguagem de programação utilizada neles em grandes empresas,
e também realiza a manipulação para criação de repositórios e adição de arquivos a repositórios existentes.
 
Durante o processo, o robô faz uma requisição ao site do GitHub, realiza a extração dos dados dos repositórios existentes
em grandes empresas (mas é possível passar qualquer nome de usuário do GitHub para essa extração) e/ou permite a criação de um repositório
e adicionar arquivos em repositórios existentes na sua própria conta.

# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

- Estão listadas no arquivo "requirements.txt".

## Sobre o código

O projeto foi dividido em classes, onde uma classe contém as funcionalidades referentes a extração de dados
de perfis do GitHub onde ele irá retornar a principal linguagem de programação utilizada em cada repositório, sendo necessário o token do 
GitHub e o nome do usuário que você quer realizar esse scraping, esta no arquivo dados_repositorios.py. 

Já a classe que manipula repositórios da própria conta, criando um repositório e adicionando arquivo em qualquer repositório já existente
está no arquivo manipula_repositorios.py.

As duas classes estão sendo instânciadas e utilizadas no arquivo main.py.



# Como executar o projeto
Pré-requisitos: Python 3.11

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

## Observações:

Por ser um WebScraping utilizando a API do GitHub, pode ser que em algum momento o Scraping pare de funcionar caso ter alguma alteração na API.

# Autor
Samael Muniz Picoli
