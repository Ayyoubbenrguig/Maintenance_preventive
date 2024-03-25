from flask import Flask, render_template, request, redirect, url_for, flash
from model import *

app = Flask(__name__)
app.secret_key = '123456789'
@app.route('/')

def index():
    return render_template('index.html')
# Route principale
@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        user_input = [[
            int(request.form['Type']),
            float(request.form['Air_temperature_K']),
            float(request.form['Process_temperature_K']),
            float(request.form['Rotational_speed_rpm']),
            float(request.form['Torque_Nm']),
            float(request.form['Tool_wear_min']),
            float(request.form['Power'])
        ]]
        prediction = predict(user_input)

        # Renvoyer les résultats à la page HTML
        return render_template('index.html', prediction=prediction)
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

