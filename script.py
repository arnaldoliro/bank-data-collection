from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print("Conectando ao banco em:", DATABASE_URL)

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    query = text("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_schema NOT IN ('information_schema', 'pg_catalog');
    """)
    result = connection.execute(query)
    tables = result.fetchall()

df = pd.DataFrame(tables, columns=["table_schema", "table_name"])
print("Tabelas encontradas:")
print(df)

with engine.connect() as connection:
    search_query = text("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_name ILIKE '%candidatesimtech%';
    """)
    search_result = connection.execute(search_query)
    search_tables = search_result.fetchall()

df_search = pd.DataFrame(search_tables, columns=["table_schema", "table_name"])
print("Busca pela tabela 'candidatesimtech':")
print(df_search)