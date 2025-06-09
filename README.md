<h1> Tag 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃 </h1>
<br>

_This was the project I learned in the Rocketseat course_

## Introduction
The purpose of the application is to create barcode images (tags) for commercial products. It is aimed at automating and benefiting from the logistics side. Taking into account the errors that may occur and having good interaction with the user.

## Technologies used
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
  

## Tools
<a href= "https://www.python.org/downloads/" target="blank" > Python</a> language version 3.10.2

The <a href="https://insomnia.rest/download" target="_blank" > Insomnia</a> program was used to test route requests simulating the Front-end.

Pylint extension has been installed in <a href = "https://code.visualstudio.com/download" target="_blank" > VS Code</a>.


## Dependencies
<a href= "https://pypi.org/project/virtualenv/" target="_blank" > Virtualenv</a> library in version 20.27.1 → `pip3 install virtualenv`

<a href= "https://pypi.org/project/pylint/" target="_blank" > Pylint</a> library in version 3.3.1 → `pip install pylint`

<a href= "https://pre-commit.com/#install" target="_blank" > Pre-commit</a> framework in version 4.0.1 → `pip install pre-commit`

<a href= "https://pypi.org/project/Flask/" target="_blank" > Flask</a> framework in version 3.0.3  → `pip install Flask`

<a href= "https://pypi.org/project/python-barcode/" target="_blank" > Python-barcode</a> library in version 0.15.1 → `pip install python-barcode` 

<a href= "https://pypi.org/project/pillow/" target="_blank" > Pillow</a> library in version 11.0.0 → `pip install pillow` 

<a href= "https://pypi.org/project/Cerberus/" target="_blank" > Cerberus</a> library in version 1.3.5 → `pip install Cerberus` 

<a href= "https://pypi.org/project/pytest/" target="_blank" > Pytest</a> library in version 8.3.3 → `pip install pytest` 


## Running the project
To obtain the repository, you need to write the following command `git clone https://github.com/dornascarol/Logistica-tags-python.git` in your computer's terminal and direct it to a folder.

Open the cloned folder in VS Code.

-

To <a href= "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#" target="_blank" > create a virtual environment</a> in Windows, type the following command in the terminal → `py -m venv .venv`

To <a href= "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#" target="_blank" >  activate a virtual environment</a> in Windows, type the following command in the terminal → `.venv\Scripts\activate`

Or configure VS Code to work with a virtual environment using the following steps: `Ctrl + Shift + p` → type `Python: Select Interpreter` in the bar → choose the recommended Python option that has `('.venv':venv)`

-

Then download the dependency installations in the virtual environment.

-

To <a href= "https://pre-commit.com/#install" target="_blank" > add pre-commit configuration</a>, create a file called: `.pre-commit-config.yaml`

To <a href= "https://pre-commit.com/#install" target="_blank" > install the git hook scripts</a>, type the following command in the terminal → `pre-commit install`

-

To run the server, type the following command in the terminal → `python run.py`  

To close the server, click the following keys: `Ctrl + c`

- 

Go to Insomnia to test the route. Paste the full URL. Write the parameter in the body. Wait for the response.


## Endpoint
<p> URL path= http://localhost:3000 </p>

| HTTP Method | URL             | Description                                                                                           |
| ----------- | --------------  | ------------------------------------------------------------------------------------------------------|
|    POST     | /create_tag     | Creates a new tag using the required parameter sent inside `request.body` in JSON format.             |

### Request body parameter
```
{
	"product_code": "exemplo_123456789"
}

```

### Positive response
200 - OK: tag successfully created in image format (png)

```
{
	"data": {
		"count": 1,
		"path": "123456789.png",
		"type": "Tag Image"
	}
}

```

### Negative responses
422 - UNPROCESSABLE ENTITY: syntactical error in mandatory parameter

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


500 - INTERNAL SERVER ERROR: when it does not send the mandatory parameter

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


## Unit tests
1) File to validate whether the request is actually performing the tag creation process.

2) File to check if the request is returning the barcode integration behavior for tag creation with the type, count and path parameters.

-

To run the unit test, type the following command in the terminal → `pytest` 

Or to run and display the name of the test with the status (whether it passed or failed), write the following command in the terminal → `pytest -s -v` 


## Project status
:heavy_check_mark: Application completed.
