from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
# Carregar CSV
CSV_FILE = "Relatorio_cadop.csv"
df = pd.read_csv(CSV_FILE, sep=';', dtype=str).fillna("")

# Função de busca
@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("q", "").lower()
    if not termo:
        return jsonify([])
    
    resultados = []
    for _, row in df.iterrows():
        ocorrencias = sum(row.astype(str).str.lower().str.count(termo))
        if ocorrencias > 0:
            resultados.append({"dados": row.to_dict(), "relevancia": ocorrencias})
    
    resultados.sort(key=lambda x: x["relevancia"], reverse=True)
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
