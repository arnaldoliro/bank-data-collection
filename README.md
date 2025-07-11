# 📊 Bank Data Collection

Este projeto realiza a extração de dados de uma tabela PostgreSQL hospedada na AWS (via Neon), gerada com Prisma, e exporta esses dados para uma planilha Excel de forma automatizada.

A configuração é feita via variáveis de ambiente, o que permite reutilizar o script para diferentes tabelas e formatos de saída.

---

## 🚀 Funcionalidades

- Conexão automática com banco PostgreSQL usando SQLAlchemy
- Filtro para selecionar apenas registros com `workload` diferente de 0
- Seleção de colunas desejadas via `.env`
- Exportação para planilha `.xlsx`
- Geração automática da pasta `sheets/` para armazenar os arquivos

---

## 🛠️ Tecnologias utilizadas

- Python 3.11+
- SQLAlchemy 2.x
- Pandas
- python-dotenv
- openpyxl (para salvar Excel)

---

## 📁 Estrutura do Projeto

```
bank-data-collection/
├── script.py # Script principal de extração
├── .env # Configurações de ambiente
├── sheets/ # Pasta onde os arquivos .xlsx são salvos
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo
```

---

## ⚙️ Configuração

### 1. Instale as dependências:

```bash
pip install -r requirements.txt
