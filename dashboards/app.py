import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import databricks.sql as dbsql

# Configuração do Databricks
DATABRICKS_SERVER = "https://<URL-WORKSPACE>.databricks.com"
ACCESS_TOKEN = "<TOKEN>"

# Consulta SQL na Tabela Gold
query = """
SELECT ano, mes, customer_id, avg_gasto
FROM delta.`/mnt/datalake/gold/transacoes_agg`
"""

# Conectar ao Databricks e buscar os dados
with dbsql.connect(server_hostname=DATABRICKS_SERVER, http_path="/sql/1.0/endpoints/<ENDPOINT>", access_token=ACCESS_TOKEN) as conn:
    df = pd.read_sql(query, conn)

# Criar coluna de data
df["data"] = pd.to_datetime(df["ano"].astype(str) + "-" + df["mes"].astype(str) + "-01")

# Criar o app Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Transações 🔥"),
    
    # Filtro de ano
    dcc.Dropdown(
        id="filtro-ano",
        options=[{"label": str(ano), "value": ano} for ano in sorted(df["ano"].unique())],
        value=df["ano"].max(),
        clearable=False
    ),
    
    # Gráfico de linha
    dcc.Graph(id="grafico-linha"),
    
    # Gráfico de ranking de clientes
    dcc.Graph(id="grafico-ranking")
])

# Callback para atualizar os gráficos
@app.callback(
    [dash.dependencies.Output("grafico-linha", "figure"),
     dash.dependencies.Output("grafico-ranking", "figure")],
    [dash.dependencies.Input("filtro-ano", "value")]
)
def atualizar_graficos(ano_selecionado):
    df_filtrado = df[df["ano"] == ano_selecionado]

    # Gráfico de linha
    fig_linha = px.line(df_filtrado, x="data", y="avg_gasto", color="customer_id",
                        title="Média de Gasto por Cliente")

    # Gráfico de ranking
    df_top = df_filtrado.groupby("customer_id")["avg_gasto"].sum().reset_index()
    df_top = df_top.sort_values("avg_gasto", ascending=False).head(10)
    fig_ranking = px.bar(df_top, x="customer_id", y="avg_gasto", title="Top 10 Clientes")

    return fig_linha, fig_ranking

if __name__ == '__main__':
    app.run_server(debug=True)


# Execute no terminal python app.py
# Depois, acesse no navegador: 📍 http://127.0.0.1:8050/