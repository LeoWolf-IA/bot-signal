@app.route('/webhook', methods=['GET'])
def webhook():
    data = request.args
    text = data.get('text', '')
    sender = data.get('phone', '') # Aquí viene el ID que nos falta
    
    # Esto va a salir en los logs de Render para que lo copiemos
    print(f"DATOS: Texto='{text}' | ID='{sender}'")
    
    return "OK", 200
