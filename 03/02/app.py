from flask import Flask
import pandas as pd
import numpy as np
import html

app = Flask(__name__)

@app.route('/')
def hello():
    # Exemple d'utilisation de pandas et numpy dans votre application Flask
    data = pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))
    # Échapper les caractères HTML pour éviter les attaques XSS
    data_html = html.escape(data.to_html())
    # Formater le message avec le contenu HTML
    message = f'Hello, World!<br><br>Voici quelques données d'exemple :<br>{data_html}'
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
