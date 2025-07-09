from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
TABLE_NAME = os.getenv("TABLE_NAME")
TABLE_FIELDS = os.getenv("TABLE_FIELDS")

print("Conectando ao banco em:", DATABASE_URL)
print("Tabela configurada:", TABLE_NAME)
print("Campos configurados:", TABLE_FIELDS)

engine = create_engine(DATABASE_URL)

fields = TABLE_FIELDS.replace(" ", "")
query_str = f"""
    SELECT {fields}
    FROM public.{TABLE_NAME}
    WHERE workload <> 0;
"""

with engine.connect() as connection:
    query = text(query_str)
    result = connection.execute(query)
    rows = result.fetchall()
    columns = result.keys()

df = pd.DataFrame(rows, columns=columns)
print(f"Encontrados {len(df)} registros com workload diferente de 0.")

output_path = "Congressistas_Certificados.xlsx"
df.to_excel(output_path, index=False)
print(f"Planilha salva em: {output_path}")