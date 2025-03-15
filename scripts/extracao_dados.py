import requests
import psycopg2
import pandas as pd

# Configuração do PostgreSQL
DB_CONFIG = {
    "dbname": "seguranca_publica",
    "user": "seu_usuario",
    "password": "sua_senha",
    "host": "localhost",
    "port": "5432",
}

# URL da API pública de segurança (substitua por uma real)
API_URL = "https://github.com/rayonnunes/api_seguranca_publica"

# Função para extrair os dados da API
def extrair_dados_api():
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        dados = response.json()  # Converter para JSON
        return dados
    else:
        print(f"Erro ao acessar API: {response.status_code}")
        return []

# Função para transformar os dados em um DataFrame do Pandas
def transformar_dados(dados):
    df = pd.DataFrame(dados)

    # Renomear colunas para um padrão mais claro
    df.rename(columns={
        "id": "crime_id",
        "tipo": "tipo_crime",
        "data": "data_ocorrencia",
        "localizacao": "endereco",
        "descricao": "descricao_crime"
    }, inplace=True)

    # Converter colunas para o formato adequado
    df["data_ocorrencia"] = pd.to_datetime(df["data_ocorrencia"])

    return df

# Função para salvar os dados no PostgreSQL
def salvar_no_postgres(df):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Criar tabela se não existir
        cur.execute("""
        CREATE TABLE IF NOT EXISTS crimes (
            crime_id SERIAL PRIMARY KEY,
            tipo_crime VARCHAR(255),
            data_ocorrencia TIMESTAMP,
            endereco TEXT,
            descricao_crime TEXT
        );
        """)

        # Inserir dados no banco
        for _, row in df.iterrows():
            cur.execute("""
            INSERT INTO crimes (tipo_crime, data_ocorrencia, endereco, descricao_crime)
            VALUES (%s, %s, %s, %s);
            """, (row["tipo_crime"], row["data_ocorrencia"], row["endereco"], row["descricao_crime"]))

        conn.commit()
        cur.close()
        conn.close()
        print("Dados inseridos no PostgreSQL com sucesso!")

    except Exception as e:
        print(f"Erro ao salvar no PostgreSQL: {e}")

# Fluxo do pipeline
dados_crimes = extrair_dados_api()
if dados_crimes:
    df_crimes = transformar_dados(dados_crimes)
    salvar_no_postgres(df_crimes)
