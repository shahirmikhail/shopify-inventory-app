from flask import Flask

app = Flask(__name__)

from routes.image import *

if __name__ == '__main__':
    app.run(debug=True)
