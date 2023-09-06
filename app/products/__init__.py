# Dependencia para hacer un blue_print
from flask import Blueprint

# Definir paquete  'products'
products = Blueprint('products',
                     __name__,
                     url_prefix= '/products',
                     template_folder = 'templates',
                     static_folder = 'imagenes'
                     )

from . import routes