import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Reemplazá esto con tu ID de grupo o número si lo tenés a mano
# Si no, después lo configuramos como "Variable de Entorno"
API_KEY = "256412"
SIGNAL_ID = "AQUÍ_VA_TU_ID_DE_GRUPO" 

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Escuchamos lo que viene de Signal
    mensaje_recibido = ""
    if request.method == 'POST':
        datos = request.get_json() or {}
        mensaje_recibido = datos.get('text', '')
    else:
        mensaje_recibido = request.args.get('text', '')

    if mensaje_recibido:
        print(f"Recibido: {mensaje_recibido}")
        
        # Respondemos al grupo
        url = "https://api.callmebot.com/signal/send.php"
        payload = {
            "group": SIGNAL_ID, 
            "apikey": API_KEY,
            "text": f"¡Bot activo! Recibí tu mensaje: {mensaje_recibido}"
        }
        requests.get(url, params=payload)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
