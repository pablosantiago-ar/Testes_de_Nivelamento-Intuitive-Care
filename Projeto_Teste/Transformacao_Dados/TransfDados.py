import pdfplumber
import pandas as pd
import os

pdf_path = "Anexo_I.pdf"
csv_path = "dados_extraidos.csv"
zip_name = "Teste_Pablo_Santiago.zip"

abr = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulaorial"
}

def extrair_tabelas(pdf_path):
    """Extrai tabelas do PDF e retorna uma lista de DataFrames."""
    dataframes = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_table()
            if tables:
                df = pd.DataFrame(tables[1:], columns=tables[0])
                df.rename(columns=abr, inplace=True)
                dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True) if dataframes else None

def salvar_csv(df, csv_path):
    df.to_csv(csv_path, index=False, encoding='utf-8')

def compactar_csv(csv_path, zip_path):
    import zipfile
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    os.remove(csv_path)

def substituir_abreviacoes(df, column_change):
    return df.replace(column_change)

df = extrair_tabelas(pdf_path)
if df is not None:
    df = substituir_abreviacoes(df, abr)
    salvar_csv(df, csv_path)
    compactar_csv(csv_path, zip_name)
    print(f"Arquivo salvo como {zip_name}")
else:
    print("Nenhuma tabela encontrada no PDF.")
