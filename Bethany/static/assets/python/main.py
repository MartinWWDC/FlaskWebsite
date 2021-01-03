from flask import Flask, render_template
import json
app = Flask(__name__)
images = None # il riferimento alla lista di oggetti di tipo dizionario. Ogni
 # dizionario contiene le 3 chiavi title, subtitle e image
 # caricamento degli oggetti json nella lista images
with open('static/assets/json/images.json') as f:
    images = json.load(f)
print(images) # stampa di controllo
@app.route('/')
def index():
        return render_template('index1.html', images=images)
@app.route('/portfolio_details')
def portfolio_details():
   return render_template('portfolio-details.html')
app.run(host='0.0.0.0', port=8080, debug=True) 