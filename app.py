from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Buscamos datos en todos los formatos posibles
    data_get = request.args.to_dict()
    data_post = request.form.to_dict()
    
    print(f"DEBUG - Datos GET: {data_get}")
    print(f"DEBUG - Datos POST: {data_post}")
    
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
