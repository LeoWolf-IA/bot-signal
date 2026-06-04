from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
    # Capturamos los datos que envía CallMeBot
    data = request.args
    text = data.get('text', '')
    sender = data.get('phone', '') # Aquí vendrá el ID del grupo
    
    # Imprimimos en los logs de Render para poder copiar el ID
    print(f"DATOS_RECIBIDOS: Texto='{text}' | ID='{sender}'")
    
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
