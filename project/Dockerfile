# Imagem base para o Django
FROM python:3.10-slim

# Atualiza os repositórios e instala as dependências do sistema
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Diretório onde o código da aplicação será copiado
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt /app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . /app/

# Expõe a porta do Django
EXPOSE 8000

# Comando para rodar a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
