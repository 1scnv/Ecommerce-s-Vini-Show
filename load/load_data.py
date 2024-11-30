import pandas as pd
import pyodbc

#Configuração de Conexão
server = 'localhost'                #Servidor
database = 'teste'                  #Banco de dados
username = 'SA'                     #Usuário
password = '123@Mudar'              #Senha
table_name = ''                     #Tabela
csv_file = 'dados.csv'              #Caminho CSV

# String de conexão
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

#Conexão do banco de dados
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

datasets = {
    'customers': './ingestion/olist_customers_dataset.csv',
    'geolocation': './ingestion/olist_geolocation_dataset.csv',
    'items': './ingestion/olist_order_items_dataset.csv',
    'payments': './ingestion/olist_order_payments_dataset.csv',
    'reviews': './ingestion/olist_order_reviews_dataset.csv',
    'orders': './ingestion/olist_orders_dataset.csv',
    'products': './ingestion/olist_products_dataset.csv',
    'sellers': './ingestion/olist_sellers_dataset.csv',
    'category_name_translation': './ingestion/product_category_name_translation.csv'
}

#Insert dos datasets
for table_name, dataset in datasets.items():
    df = pd.read_csv(dataset)
    for index, row in df.iterrows():
        # Inserção
        columns = ', '.join(row.index)
        placeholders = ', '.join('?' for _ in row)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(row)
        cursor.execute(sql, values)

#Commit
conn.commit()

#Fechar Conexão
cursor.close()
conn.close()