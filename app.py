from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para el traductor
@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['language']
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == '__main__':
    app.run(debug=True)
