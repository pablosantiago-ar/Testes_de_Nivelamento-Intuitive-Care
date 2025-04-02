## Requisitos
Instale as bibliotecas necessárias com o seguinte comando:

pip install pdfplumber pandas

## Como Usar

1. Coloque o arquivo PDF que deseja processar na mesma pasta do script e renomeie-o para `Anexo_I.pdf` 
   ou ajuste o nome no código.
2. Execute o script com o seguinte comando:

   python nome_do_arquivo.py

3. O script irá:
   - Ler o PDF e extrair as tabelas
   - Substituir abreviações conforme dicionário predefinido
   - Salvar os dados em um arquivo CSV chamado `dados_extraidos.csv`
   - Compactar o arquivo CSV em um ZIP chamado `Teste_Pablo_Santiago.zip`

4. Se a extração for bem-sucedida, o arquivo ZIP será gerado e a versão CSV será removida automaticamente.

## Estrutura do Projeto
/
|-- Anexo_I.pdf
|-- nome_do_arquivo.py
|-- Teste_Pablo_Santiago.zip  # (gerado após a execução)

