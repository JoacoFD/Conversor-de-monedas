from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "http://apilayer.net/api/live"
ACCESS_KEY = "a2dafcaabd342b1006fd79d90b459cbc"  # Reemplaza con tu propia clave de API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form['amount']
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    # Realiza la llamada a la API de apilayer
    response = requests.get(f"{API_URL}?access_key={ACCESS_KEY}&currencies={to_currency}&source={from_currency}&format=1")
    data = response.json()

    if response.status_code == 200 and 'quotes' in data:
        # Obtén la tasa de conversión
        conversion_rate = data['quotes'][f"{from_currency}{to_currency}"]
        result = float(amount) * conversion_rate
    else:
        result = "Error: Conversión no disponible"

    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
