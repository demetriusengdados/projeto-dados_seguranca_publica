import psycopg2
from config import DB_CONFIG

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("Conexão bem-sucedida ao PostgreSQL!")

    # Testando a conexão com um SELECT
    cursor.execute("SELECT version();")
    print(f"Versão do PostgreSQL: {cursor.fetchone()[0]}")

    # Fechando a conexão
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
