# Projeto Django com MySQL utilizando Docker

Este é um exemplo de como configurar um ambiente de desenvolvimento utilizando Docker para um projeto Django com MySQL.

## Tecnologias

- **Django**: Framework web para Python.
- **MySQL**: Sistema de gerenciamento de banco de dados.
- **Docker**: Plataforma para desenvolvimento e execução de contêineres.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o Docker e o Docker Compose instalados em sua máquina. Caso ainda não tenha, você pode seguir os seguintes tutoriais:

- [Instalar Docker](https://docs.docker.com/get-docker/)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Estrutura do Projeto

O projeto é composto por dois serviços principais:

1. **db**: Contêiner que executa o MySQL.
2. **web**: Contêiner que executa o Django.

### Comandos

- Dentro da pasta project, rode
> docker-compose up --build && docker-compose up

- Logo após, apenas entrar em [link da aplicação](http://127.0.0.1:8000/hello_mundo/)


