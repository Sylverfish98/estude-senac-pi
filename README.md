## Sobre o projeto
Estude! é um website feito para facilitar a gerência de cronogramas de estudos.

### Integrantes:
- Fernando Augusto De Araujo
- Flávia Maria Dos Santos Castro
- Gabriel Fonseca Sales
- Henrique Jorge Oliveira Almeida
- João Gabriel Rodrigues De Jesus

## Rodando o Projeto
### Subindo Servidor de Produção com o Docker Compose

O [Docker](https://www.docker.com/resources/what-container/) dispensa a instalação das dependências do projeto e,
portanto, recomendamos esse método para testar o programa:

1. Instale o [Docker](https://www.docker.com/products/docker-desktop/).
2. Depois de navegar para a raiz do projeto, suba o container:

```bash
docker compose -f docker/docker-compose.yml up
```

3. Abra o site em: [http://localhost:8000/login](http://localhost:8000/login)

> **Nota**: Caso seja necessário subir o container com o estado inicial novamente, por favor pare o mesmo e limpe os
> volumes com o seguinte comando:

```bash
docker compose -f ./docker/docker-compose.yml down && docker volume rm -f estude-db estude-staticfiles && docker compose -f ./docker/docker-compose.yml up --build
```

### Subindo o Servidor de Desenvolvimento

1. Instale o [Python](https://www.python.org/downloads/windows/), no instalador marque a opção 'Add python to path'.
   Após a instalação, reinicie seu computador.
2. Instale o [uv](https://docs.astral.sh/uv/getting-started/installation/), esse programa substitui o pip e venv,
   facilitando o desenvolvimento:

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

6. Abra o site em: [http://localhost:8000/login](http://localhost:8000/login)

## Arquitetura do Projeto
### URLs disponíveis

| Página                       | URL                       |
|------------------------------|---------------------------|
| Cadastro                     | `/register/`              |
| Login                        | `/login/`                 |
| Logout                       | `/logout/`                |
| Lista de matérias            | `/materia/`               |
| Nova matéria                 | `/materias/nova/`         |
| Detalhes da matéria          | `materias/<pk>/`          |
| Editar matéria               | `/materias/<pk>/editar/`  |
| Excluir matéria              | `/materias/<pk>/deletar/` |
| Listar tópicos               | `/agenda/`                |
| Completar um tópico (evento) | `topics/<pk>/toggle/`     |
| Deletar um tópico (evento)   | `topics/<pk>/deletar/`    |

