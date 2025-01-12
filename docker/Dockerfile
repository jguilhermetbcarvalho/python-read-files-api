# Use a imagem base Python
FROM python:3.12

# Defina o diretório de trabalho
WORKDIR /

# Crie um diretório para a aplicação
RUN mkdir /home/app

# Copie o script de entrada
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh

# Conceda permissões ao script de entrada e crie um link simbólico
RUN chmod 755 /usr/local/bin/entrypoint.sh && ln -s /usr/local/bin/entrypoint.sh

# Instale o OpenJDK 11
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Defina a variável de ambiente JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

# Atualize o pip e instale o Poetry para gerenciar dependências do projeto
RUN pip install --upgrade pip && pip install poetry

# Exponha a porta 8000
EXPOSE 8012

# Defina o ponto de entrada
ENTRYPOINT ["entrypoint.sh"]