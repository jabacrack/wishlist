from flask import Flask

app = Flask(__name__, template_folder='../client')
app.config.from_object('config')

from service import index
from service import add