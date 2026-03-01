## Sobre o projeto
Estude! é uma aplicação feita em Django que permite o usuário gerenciar seu cronograma de estudos usando uma interface simples e intuitiva.

## Rodando o Projeto
### Subindo Servidor de Produção com o Docker Compose
O [Docker](https://www.docker.com/resources/what-container/) é uma aplicação que encapsula o software e suas dependências em um container, que pode ser executado como um só processo em qualquer sistema. Caso o intuito seja apenas testar a aplicação recomenda-se usar esse método. 
1. Instale o [Docker](https://www.docker.com/products/docker-desktop/).
2. Depois de navegar para a raiz do projeto, suba o container:
```bash
docker compose -f docker/docker-compose.yml up
```
3. Abra o site em: [https://localhost:8000/login](https://localhost:8000/login)

### Subindo o Servidor de Desenvolvimento
1. Instale o [Python](https://www.python.org/downloads/windows/)
2. Instale o [uv](https://docs.astral.sh/uv/getting-started/installation/), esse programa substitui o pip e venv, facilitando o desenvolvimento:
```bash
pip install uv
```
3. Navegue para a pasta do projeto e, em seguida, instale as dependências do projeto:
```bash
uv sync
```
4. Suba o servidor de desenvolvimento:
```bash
uv run src/manage.py runserver
```
5. Abra o site em: [https://localhost:8000/login](https://localhost:8000/login)