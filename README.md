<h1> Tag 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃 </h1>
<br>

## Este foi o projeto que aprendi no curso da Rocketseat
API para criação de código de barras (tag).

## Introdução
O objetivo da aplicação é para criações de imagens de códigos de barras (tags) destinados aos produtos comerciais. Voltado para automatizar e usufruir na parte logística. Levando em consideração os erros que podem acontecer e tendo uma boa interação com o usuário.

## Tecnologias utilizadas
- VS Code
- Insomnia
- Python
- Virtualenv
- Pylint
- Pre-commit
- Flask
- Python-barcode
- Pillow
- Cerberus
- Pytest
  

## Ferramentas
A linguagem <a href= "https://www.python.org/downloads/" target="blank" > Python </a> na versão 3.10.2

Foi usado o programa <a href="https://insomnia.rest/download" target="_blank" > Insomnia </a> para testar as requisições das rotas simulando o Front-end.

Foi instalado a extensão Pylint no VS Code.


## Dependências
Biblioteca <a href= "https://pypi.org/project/virtualenv/" target="_blank" > virtualenv </a> na versão 20.27.1 → `pip3 install virtualenv`

Biblioteca <a href= "https://pypi.org/project/pylint/" target="_blank" > pylint </a> na versão 3.3.1 → `pip install pylint`

Framework <a href= "https://pre-commit.com/#install" target="_blank" > pre-commit </a> na versão 4.0.1 → `pip install pre-commit`

Framework <a href= "https://pypi.org/project/Flask/" target="_blank" > Flask </a> na versão 3.0.3  → `pip install Flask`

Biblioteca <a href= "https://pypi.org/project/python-barcode/" target="_blank" > python-barcode </a> na versão 0.15.1 → `pip install python-barcode` 

Biblioteca <a href= "https://pypi.org/project/pillow/" target="_blank" > pillow </a> na versão 11.0.0 → `pip install pillow` 

Biblioteca <a href= "https://pypi.org/project/Cerberus/" target="_blank" > Cerberus </a> na versão 1.3.5 → `pip install Cerberus` 

Biblioteca <a href= "https://pypi.org/project/pytest/" target="_blank" > pytest </a> na versão 8.3.3 → `pip install pytest` 


## Rodando o projeto
Para rodar o repositório é necessário dar um `git clone https://github.com/dornascarol/Logistica-tags-python.git` em alguma pasta do seu computador.

-

Para <a href= "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#" target="_blank" >  criar um ambiente virtual </a> no Windows, escreva o seguinte comando no terminal → `py -m venv .venv`

Para <a href= "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#" target="_blank" >  ativar um ambiente virtual </a> no Windows, escreva o seguinte comando no terminal → `.venv\Scripts\activate`

Ou configurar o VS Code para trabalhar com ambiente virtual usando os seguintes passos: `Ctrl + Shift + p` → escrever na barra `Python: Select Interpreter` → escolher a opção recomendada do Python que tenha `('.venv':venv)`

-

Em seguida, rodar as instalações de dependências no ambiente virtual.

-

Para <a href= "https://pre-commit.com/#install" target="_blank" > adicionar a configuração do pre-commit </a>, cria um arquivo chamado: `.pre-commit-config.yaml`

Para <a href= "https://pre-commit.com/#install" target="_blank" > instalar os scripts de hook do git </a>, escreva o seguinte comando no terminal → `pre-commit install` 

-

Para rodar o servidor, escreva o seguinte comando no terminal → `python run.py`  

Para fechar o servidor, clique nas seguintes teclas: `Ctrl + c`

- 
Ir no Insomnia para testar a rota. Colar a URL completa. Escrever o parâmetro no body. Aguardar pela resposta. 


## Endpoint
<p> Caminho da URL= http://localhost:3000 </p>

| Método HTTP | URL             | Descrição                                                                                             |
| ----------- | --------------  | ------------------------------------------------------------------------------------------------------|
|    POST     | /create_tag     | Cria uma nova tag usando o parâmetro obrigatório enviado dentro do `request.body` no formato JSON.    |

### Parâmetro request body
```
{
	"product_code": "123456789"
}

```

### Resposta positiva
200 - OK: tag criada com sucesso no formato imagem (png)

```
{
	"data": {
		"count": 1,
		"path": "123456789.png",
		"type": "Tag Image"
	}
}

```

### Respostas negativas
422 - UNPROCESSABLE ENTITY: erro sintático no parâmetro obrigatório

```
{
	"errors": [
		{
			"detail": {
				"product": [
					"unknown field"
				],
				"product_code": [
					"required field"
				]
			},
			"title": "UnprocessableEntity"
		}
	]
}

```


500 - INTERNAL SERVER ERROR: quando não envia o parâmetro obrigatório

```
{
	"errors": [
		{
			"detail": "400 Bad Request: Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)",
			"title": "Server Error"
		}
	]
}

```


## Testes unitários
Arquivo para validar se realmente a requisição está fazendo o processo de criação de tag.

Arquivo para verificar se a requisição está retornando o comportamento da integração do barcode para criação de tag com os parâmetros de type, count e path.

-

Para rodar o teste unitário → `pytest` 

Ou para rodar e apresentar o nome do teste com o status (se passou ou falhou) → `pytest -s -v` 


## Status do projeto
:heavy_check_mark: Aplicação finalizada.
