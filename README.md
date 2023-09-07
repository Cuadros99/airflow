# **airflow**


**Descrição do Projeto**: Este projeto consiste em um sistema de coleta e armazenamento de tweets relacionados a serviços de streaming, como Disney Plus, Netflix, HBOGO, Globoplay, entre outros. Os tweets são coletados em tempo real, passam por um processo de limpeza e estruturação e são armazenados em um banco de dados PostgreSQL.

## Requisitos

- Python 3.10

## Configuração do Ambiente

1. Clone este repositório:
    
    ```bash
    git clone https://github.com/Cuadros99/airflow.git
    ```
    
2. Navegue até o diretório do projeto:
    
    ```bash
    cd airflow
    ```
    
3. Crie um ambiente virtual
    
    ```jsx
    python3 -m venv venv
    ```
    
4. Ative o ambiente virtual criado
    
    ```jsx
    source venv/bin/activate
    ```
    
5. Instale as dependências necessárias no ambiente virtual
    
    ```bash
    pip install -r requirements_airflow.txt
    ```
    
6. Execute os seguintes comandos

    ```bash
    airflow webserver
    ```

    ```bash
    airflow scheduler
    ```
    **Obs:** Lembre-se de executá-los com o ambiente virtual ativado

7. Acesse o link **`localhost:8080`** e insira os dados a seguir para realizar o login:
    - **Usuário:** admin
    - **Senha:** atg_project

8. O projeto pode ser utilizado juntamente com o Projeto Streaming-insights que pode ser encontrado nesse link: https://github.com/Cuadros99/Streaming-insights
    
    **Obs:** Atente-se para deixar ambos os repositórios no mesmo diretório
