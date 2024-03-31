import pandas as pd

df_principal = pd.read_excel("/content/tabela_acoes.xlsx", sheet_name="Principal")

df_pes_chatgpt = pd.read_excel("/content/tabela_acoes.xlsx", sheet_name="Segui_Idade")

df_qnt_acoes = pd.read_excel("/content/tabela_acoes.xlsx", sheet_name="Total_de_acoes")

df_tickers = pd.read_excel("/content/tabela_acoes.xlsx", sheet_name="Analises")

df_analises = pd.read_excel("/content/tabela_acoes.xlsx", sheet_name="Analises")

df_principal = df_principal[['Ativo', 'Data', 'Último (R$)', 'Var. Dia (%)']].copy()
