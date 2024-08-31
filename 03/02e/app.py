from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    # Example of using pandas and numpy in your Flask app
    data = pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))
    return f'Hello, World!<br><br>Here is some sample data:<br>{data.to_html()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
