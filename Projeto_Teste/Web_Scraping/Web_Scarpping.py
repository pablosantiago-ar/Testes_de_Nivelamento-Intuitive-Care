import requests
from bs4 import BeautifulSoup
import os
import zipfile
from urllib.parse import urljoin

# URL do site da ANS
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório para salvar os PDFs
download_dir = "anexos_ans"
os.makedirs(download_dir, exist_ok=True)

# Requisição ao site
response = requests.get(url)
response.raise_for_status()

# Parser do HTML
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar os links dos anexos
pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    if "Anexo" in href and href.endswith(".pdf"):  # Filtrando apenas PDFs
        full_url = urljoin(url, href)  # Adicionando domínio se necessário
        pdf_links.append(full_url)

# Verificando os links encontrados
if not pdf_links:
    print("Nenhum link de anexo encontrado. Verifique a estrutura do site.")
else:
    print("Links encontrados:")
    for link in pdf_links:
        print(link)

# Baixar os PDFs
def download_pdf(url, folder):
    filename = url.split("/")[-1]
    filepath = os.path.join(folder, filename)
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, "wb") as f:
        f.write(response.content)
    print(f"Baixado: {filename}")
    return filepath

pdf_files = [download_pdf(link, download_dir) for link in pdf_links]

# Criando o arquivo ZIP
zip_filename = "anexos_ans.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for pdf in pdf_files:
        zipf.write(pdf, os.path.basename(pdf))
        print(f"Adicionado ao ZIP: {pdf}")

print(f"Arquivo ZIP criado com sucesso: {zip_filename}")
