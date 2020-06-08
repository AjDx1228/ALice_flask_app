from flask import Flask, request
import logging
import os

import json

from flask import Flask

app = Flask(__name__)

from views import general
app.register_blueprint(general.mod)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(port=port, host='0.0.0.0')