## Sobre o projeto
Estude! é um website feito para facilitar a gerência de cronogramas de estudos.

## Rodando o Projeto
### Subindo o Servidor de Desenvolvimento
1. Instale o [Python](https://www.python.org/downloads/windows/), no instalador marque a opção 'Add python to path'. Após a instalação, reinicie seu computador.
2. Instale o [uv](https://docs.astral.sh/uv/getting-started/installation/), esse programa substitui o pip e venv, facilitando o desenvolvimento:
```bash
pip install uv
```
3. Navegue para a pasta do projeto e, em seguida, instale as dependências do projeto:
```bash
uv sync
```
4. Atualize as tabelas do banco de dados:
```bash
uv run src/manage.py migrate
```
5. Suba o servidor de desenvolvimento:
```bash
uv run src/manage.py runserver
```
6. Abra o site em: [https://localhost:8000/login](https://localhost:8000/login)

## Arquitetura do Projeto
### URLs disponíveis

| Página            | URL                              |
|-------------------|----------------------------------|
| Cadastro          | `/register/`                     |
| Login             | `/login/`                        |
| Logout            | `/logout/`                       |
| Lista de matérias | `/materia/`                      |
| Nova matéria      | `/materias/nova/`                |
| Editar matéria    | `/materias/<pk>/editar/`         |
| Excluir matéria   | `/materias/<pk>/deletar/`        |

