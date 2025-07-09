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
        SELECT name, email, phone, course, institution, cpf
        FROM public.candidate_simtech
        WHERE workload <> 0;
    """)
    result = connection.execute(query)
    rows = result.fetchall()
    columns = result.keys()

df = pd.DataFrame(rows, columns=columns)
print(f"Encontrados {len(df)} registros com workload diferente de 0.")

output_path = "Congressitas_Certificado.xlsx"
df.to_excel(output_path, index=False)
print(f"Planilha salva em: {output_path}")