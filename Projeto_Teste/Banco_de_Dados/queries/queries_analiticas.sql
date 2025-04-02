-- Consulta 1: Top 10 operadoras com maiores despesas no último trimestre
SELECT r.Razao_Social, d.REG_ANS, 
       CONCAT('R$ ', REPLACE(FORMAT(SUM(d.VL_SALDO_FINAL), 2), '.', ',')) AS Total_Despesas
FROM despesas d
JOIN relatorio_cadop r ON d.REG_ANS = r.Registro_ANS
WHERE d.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
AND d.DATA >= '2024-10-01'
GROUP BY d.REG_ANS, r.Razao_Social
ORDER BY SUM(d.VL_SALDO_FINAL) DESC
LIMIT 10;

-- Consulta 2: Top 10 operadoras com maiores despesas no último ano
SELECT r.Razao_Social, d.REG_ANS, 
       CONCAT('R$ ', REPLACE(FORMAT(SUM(d.VL_SALDO_FINAL), 2), '.', ',')) AS Total_Despesas
FROM despesas d
JOIN relatorio_cadop r ON d.REG_ANS = r.Registro_ANS
WHERE d.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
AND d.DATA BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY d.REG_ANS, r.Razao_Social
ORDER BY SUM(d.VL_SALDO_FINAL) DESC
LIMIT 10;