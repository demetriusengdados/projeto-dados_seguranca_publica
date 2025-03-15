# 📌 Documentação do Projeto: Data Lake de Crimes e Segurança Pública

## 📖 Visão Geral
Este projeto tem como objetivo construir um **Data Lake de Crimes e Segurança Pública** utilizando **Azure e infraestrutura local**. A solução coleta, processa e armazena dados de segurança pública a partir de uma API real, possibilitando análises e insights relevantes para órgãos públicos e pesquisadores.

---

## 🎯 Objetivos do Projeto
- Extrair dados de crimes e segurança pública de uma API real;
- Armazenar os dados em um banco de dados PostgreSQL;
- Processar e transformar os dados para análises futuras;
- Criar um pipeline de ingestão automatizado na Azure e on-premise;
- Fornecer insights e dashboards a partir dos dados coletados.

---

## 🔧 Tecnologias Utilizadas

### **Infraestrutura**
- **Azure** (para armazenamento e processamento)
- **Infraestrutura local** (para backup e processamento adicional)
- **PostgreSQL** (armazenamento estruturado)

### **Linguagens e Ferramentas**
- **Python** (extração e processamento dos dados)
- **Pandas** (tratamento e análise de dados)
- **Requests** (consumo da API)
- **psycopg2** (conexão com PostgreSQL)
- **Apache Spark / Databricks** (para processamento distribuído, se necessário)
- **Power BI** (para visualização dos dados)

---

## 🔗 Fonte dos Dados
- **API Pública de Segurança** ([Catálogo de APIs Governamentais](https://www.gov.br/conecta/catalogo/))
- **Outras bases públicas, se necessário**

---

## 🏗️ Estrutura do Projeto
```
📂 projeto_data_lake_crimes
│── 📂 scripts
│   │── extracao_dados.py        # Script para extração dos dados da API
│   │── carga_postgres.py        # Script para armazenar dados no PostgreSQL
│   │── transformacao_dados.py   # Processamento e limpeza dos dados
│
│── 📂 config
│   │── config.py                # Configuração do banco de dados
│
│── 📂 notebooks
│   │── analise_exploratoria.ipynb # Jupyter Notebook para análise inicial
│
│── 📂 dashboards
│   │── crime_dashboard.pbix     # Dashboard Power BI
│
│── requirements.txt             # Lista de dependências do projeto
│── README.md                    # Documentação do projeto
```

---

## 🚀 Implementação
### **1️⃣ Criar o ambiente virtual e instalar as dependências**
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
pip install -r requirements.txt
```

### **2️⃣ Executar a extração dos dados**
```bash
python scripts/extracao_dados.py
```

### **3️⃣ Processar e transformar os dados**
```bash
python scripts/transformacao_dados.py
```

### **4️⃣ Armazenar os dados no PostgreSQL**
```bash
python scripts/carga_postgres.py
```

---

## 📊 Visualização dos Dados
- **Os dados podem ser analisados e visualizados em dashboards no Power BI.**
- **Consultas SQL podem ser feitas diretamente no PostgreSQL.**

---

## 📌 Próximos Passos
- Criar automação com **Airflow** para execução dos pipelines
- Integrar **Databricks** para processamento distribuído
- Melhorar o modelo de dados para análises preditivas

---

## 👥 Contribuidores
- **Demetrius Mata** (Engenheiro de Dados)

