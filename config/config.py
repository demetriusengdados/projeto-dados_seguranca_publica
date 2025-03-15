import os

# Configurações do Banco de Dados PostgreSQL
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "seguranca_publica"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "senha_segura")
}

def get_db_connection_url():
    """
    Retorna a URL de conexão com o PostgreSQL.
    """
    return f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

if __name__ == "__main__":
    print("URL de conexão:", get_db_connection_url())
