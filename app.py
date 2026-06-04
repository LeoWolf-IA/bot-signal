from flask import Flask, request
import requests

app = Flask(__name__)

# Tus datos fijos
API_KEY = "256412"
GROUP_ID = "CjQKIKAKaf_FeA9B6TIFBy_TrkVwblpVcYQ4OxJt0ripKBZSEhCZxZSLd3Ids5E-0ck6aa1k"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # 1. Capturamos lo que vos escribiste en el grupo
    # CallMeBot manda los datos como parámetros en la URL (GET)
    texto_recibido = request.args.get('text') or request.args.get('mensaje')
    id_origen = request.args.get('group') or request.args.get('id')
    
    # Imprimimos en la consola de Render para ver qué llegó
    print(f"DEBUG - Llegó un mensaje al grupo: {texto_recibido} desde el ID: {id_origen}")
    
    # Si viene un mensaje vacío (la prueba técnica de CallMeBot), no hacemos nada
    if not texto_recibido:
        return "OK", 200

    # 2. Preparamos la respuesta automática
    # El bot va a responder esto cada vez que hables
    respuesta_bot = f"¡Te escuché perfecto! Dijiste: {texto_recibido}"
    
    # 3. Le ordenamos a CallMeBot que mande la respuesta de vuelta al grupo
    url_enviar = f"https://signal.callmebot.com/signal/send.php?apikey={API_KEY}&group={GROUP_ID}&text={respuesta_bot}"
    
    requests.get(url_enviar)
    
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
