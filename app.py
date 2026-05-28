import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados simulados do satélite Sentinel que serão exibidos no painel
    dados_satelite = {
        "status_satelite": "Operacional (Orbitando LEO)",
        "ultima_atualizacao": "Tempo Real",
        "regiao_critica": "Bacia Amazônica - Setor Norte",
        "alerta_desmatamento": "Nenhum alerta crítico nas últimas 24h",
        "indice_ndvi_medio": "0.78 (Vegetação Densa)"
    }
    return render_template('index.html', dados=dados_satelite)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)