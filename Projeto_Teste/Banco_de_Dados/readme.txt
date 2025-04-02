# Guia de Configuração do Banco de Dados e Execução das Queries Analíticas

## 1. Configuração do Banco de Dados

### Criando o Banco de Dados e as Tabelas
Execute os seguintes comandos no MySQL Workbench ou outro cliente MySQL:

```sql
CREATE DATABASE ans_despesas;
USE ans_despesas;

CREATE TABLE despesas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    DATA DATE,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2)
);

CREATE TABLE relatorio_cadop (
    Registro_ANS INT,
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(3),
    Telefone VARCHAR(15),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE,
    PRIMARY KEY (Registro_ANS)
);
```

## 2. Importação dos Dados

Coloque os arquivos CSV na pasta `C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/` e execute os comandos:

```sql
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2023.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@DATA, @REG_ANS, @CD_CONTA_CONTABIL, @DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET
    DATA = STR_TO_DATE(@DATA, '%d/%m/%Y'),
    VL_SALDO_INICIAL = REPLACE(@VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@VL_SALDO_FINAL, ',', '.');
```

Repita para os outros arquivos trocando o nome do arquivo.

Para o Relatório CADOP:
```sql
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv'
INTO TABLE relatorio_cadop
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

## 3. Queries Analíticas

### 3.1 Maiores Despesas no último Trimestre
```sql
SELECT r.Razao_Social, d.REG_ANS, FORMAT(SUM(d.VL_SALDO_FINAL), 2, 'pt_BR') AS Total_Despesas
FROM despesas d
JOIN relatorio_cadop r ON d.REG_ANS = r.Registro_ANS
WHERE d.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND d.DATA BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY d.REG_ANS, r.Razao_Social
ORDER BY SUM(d.VL_SALDO_FINAL) DESC
LIMIT 10;
```

### 3.2 Maiores Despesas no Ano
```sql
SELECT r.Razao_Social, d.REG_ANS, FORMAT(SUM(d.VL_SALDO_FINAL), 2, 'pt_BR') AS Total_Despesas
FROM despesas d
JOIN relatorio_cadop r ON d.REG_ANS = r.Registro_ANS
WHERE d.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND YEAR(d.DATA) = 2024
GROUP BY d.REG_ANS, r.Razao_Social
ORDER BY SUM(d.VL_SALDO_FINAL) DESC
LIMIT 10;
```

## 4. Como Salvar Queries no MySQL Workbench

- No Workbench, crie um novo script (`File > New Query Tab`).
- Cole suas queries e salve como `.sql` (`File > Save As`).
- Para rodar novamente, basta abrir o arquivo e executar.

## 5. Como Compartilhar os Arquivos

- Inclua os arquivos `.csv`, o script `.sql` e este `README.txt`.
- Envie como `.zip` ou compartilhe por um repositório Git.

## Fim

Esse guia cobre todo o processo para importar e analisar os dados conforme solicitado pela empresa. Boa sorte! 🚀
