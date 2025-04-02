# Guia de Uso - API de Busca de Operadoras

## 1️ Configuração do Backend (Flask)

### 📌 Pré-requisitos
- Python 3 instalado (versão 3.8 ou superior recomendada)
- Pip instalado

### 📦 Instalar dependências
Abra o terminal/cmd na pasta do backend e execute:
```
pip install flask flask-cors pandas
```

### 🚀 Rodar o backend
Certifique-se de que o arquivo **Relatorio_cadop.csv** está na pasta correta e execute:
```
python app.py
```
Se tudo estiver certo, o servidor será iniciado em `http://127.0.0.1:5000`.

---

## 2️ Configuração do Frontend (Vue.js)

### 📌 Pré-requisitos
- Node.js e npm instalados
- Vue CLI instalado (se necessário, instale com: `npm install -g @vue/cli`)

### 📦 Instalar dependências
Navegue até a pasta do frontend e execute:
```
npm install
```

### 🚀 Rodar o frontend
No terminal, dentro da pasta do frontend, execute:
```
npm run dev
```
Acesse o frontend no navegador em `http://localhost:5173` (ou a porta indicada no terminal).

---

## 3️ Testando no Postman

### 📌 Importar a coleção
1. Abra o **Postman**.
2. Vá em **File > Import** e selecione o arquivo `Teste_API_Operadoras.postman_collection.json`.

### 🔎 Testando a API
1. Dentro da coleção importada, clique na requisição **"Buscar Operadora"**.
2. Confirme que o método **GET** está selecionado.
3. Altere o parâmetro `q` na URL para testar diferentes buscas:
   ```
   http://localhost:5000/buscar?q=nome_da_operadora
   ```
4. Clique em **Send** e verifique os resultados no **Body**.

Se os dados aparecerem corretamente, está tudo funcionando! 🎉
