import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Render nos va a guardar estos secretos bajo llave en su plataforma
API_KEY = os.environ.get("CALLMEBOT_API_KEY", "256412")
SIGNAL_ID = os.environ.get("SIGNAL_GROUP_ID") 

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    mensaje_recibido = ""
    if request.method == 'POST':
        datos = request.get_json() or {}
        mensaje_recibido = datos.get('text', '')
    else:
        mensaje_recibido = request.args.get('text', '')

    if mensaje_recibido:
        print(f"Recibido desde Signal: {mensaje_recibido}")
        
        # URL de CallMeBot para enviar mensajes a grupos
        url = "https://signal.callmebot.com/signal/send.php"
        payload = {
            "group": SIGNAL_ID, 
            "apikey": API_KEY,
            "text": f"¡Bot activo en el grupo! Recibí tu mensaje: {mensaje_recibido}"
        }
        try:
            requests.get(url, params=payload)
        except Exception as e:
            print(f"Error al enviar a Signal: {e}")

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
