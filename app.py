from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def integracao_claude():
    url = "http://pangeabnp.pdpj.jus.br/"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        sopa = BeautifulSoup(resposta.text, "html.parser")

        titulos = [h.get_text(strip=True) for h in sopa.find_all(["h1", "h2", "h3"])]
        paragrafos = [p.get_text(strip=True) for p in sopa.find_all("p")]

        return jsonify({
            "name": "juris pangeia",
            "version": "1.0",
            "capabilities": ["consulta", "resumo", "raspagem"],
            "endpoint": url,
            "fonte": url,
            "títulos": titulos,
            "parágrafos": paragrafos[:5]
        })

    except Exception as e:
        return jsonify({"erro": f"Erro ao acessar: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
