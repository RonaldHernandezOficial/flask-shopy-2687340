# Dependencia para hacer un blue_print
from flask import Blueprint

# Definir paquete  'prducts'
products = Blueprint('products',
                     __name__,
                     url_prefix= '/products',
                     template_folder='templates')

from . import routes