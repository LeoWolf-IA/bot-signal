from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
    # Esto captura TODO lo que llegue, sin filtros
    args = request.args.to_dict()
    print(f"DEBUG: Datos completos recibidos -> {args}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
