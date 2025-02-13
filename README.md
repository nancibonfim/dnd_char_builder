# DnD 5e 2024 haracter Builder

## Development Setup

### Install poetry

#### Linux
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

####  Windows (Powershell)
``` bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### 
```bash
poetry install --no-root
poetry run pre-commit install Alexa party
```

## Python Version
Make sure you are running the application with Python 3.12, or you may run into incompatibilities with certain libraries.
It is recommended to use pyenv to manage Python versions:

``` bash
pyenv install 3.12.5
pyenv global 3.12.5
```

Then configure Poetry to use that version of Python:
```bash
poetry env use 3.12.5
```

## Executing Tests

```bash
poetry run pytest
```