from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Obtendo o caminho do diretório atual do script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Dados de exemplo
produtos = [
    {
        "foto": "produto1.jpg",
        "nome": "Produto 1",
        "quantidade": 10,
        "valor": 20
    },
    {
        "foto": "produto2.jpg",
        "nome": "Produto 2",
        "quantidade": 5,
        "valor": 15
    },
    {
        "foto": "produto3.jpg",
        "nome": "Produto 3",
        "quantidade": 5,
        "valor": 15
    },
]

# Rota para renderizar o template com os produtos
@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

# Rota para obter produtos como JSON (opcional)
@app.route('/api/produtos')
def obter_produtos():
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(debug=True)
