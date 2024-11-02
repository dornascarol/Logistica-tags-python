<h1> Tags 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃 </h1>
<br>

## Este foi o projeto que aprendi no curso da Rocketseat
API para criação de barras de código (tags).

## Introdução
Aplicação voltada para a criação de barras de código (tags) destinadas a produtos comerciais. Voltado para automatizar e usufruir na parte logística.

## Tecnologias utilizadas
- VS Code
- Insomnia
- Python
- Virtualenv
- Pylint
- Pre-commit
- 

## Ferramentas
Python na versão 3.10.2

Foi usado o programa <a href="https://insomnia.rest/download" target="_blank" > Insomnia </a> para testar as requisições das rotas simulando o Front-end.

Foi instalado a extensão Pylint no VS Code.


## Dependências
Biblioteca <a href= "https://pypi.org/project/virtualenv/" target="_blank" > virtualenv </a> na versão 20.26.6 → `pip3 install virtualenv`

Biblioteca <a href= "https://pypi.org/project/pylint/" target="_blank" > pylint </a> na versão 3.3.1 → `pip install pylint`

Biblioteca <a href= "https://pre-commit.com/#install" target="_blank" > pre-commit </a> na versão 4.0.1 → `pip install pre-commit`


## Rodando o projeto
Para <a href= "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#" target="_blank" >  criar um ambiente virtual </a> no Windows → `py -m venv .venv`

Para <a href= "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#" target="_blank" >  ativar um ambiente virtual </a> no Windows → `.venv\Scripts\activate`

Ou configurar o VS Code para trabalhar com ambiente virtual usando os seguintes passos: `Ctrl + Shift + p` → escrever na barra `Python: Select Interpreter` → escolher a opção recomendada do Python que tenha `('.venv':venv)`

-

Para <a href= "https://pre-commit.com/#install" target="_blank" > adicionar a configuração do pre-commit </a>, cria um arquivo chamado: `.pre-commit-config.yaml`

Para <a href= "https://pre-commit.com/#install" target="_blank" > instalar os scripts de hook do git </a> → `pre-commit install` 

-



## Endpoint
<p> Caminho da URL: http://localhost:3000 </p>

| Método | URL             | Descrição                                                                                             |
| ------ | --------------  | ------------------------------------------------------------------------------------------------------|
| POST   | /create_tag     | Cria uma nova tag usando o parâmetro obrigatório enviado dentro do `request.body` no formato JSON.    |

### Parâmetro request body
`{
	"product_code": "123456789"
}`

### Resposta positiva
200 - OK

``

### Resposta negativa
422 - UNPROCESSABLE ENTITY

``


## Testes unitários



## Status do projeto
:construction: Aplicação em andamento.
