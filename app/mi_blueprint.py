from flask import Blueprint

mi_blueprint = Blueprint('mi_blueprint',
                         __name__,
                         url_prefix = '/que'
                          )

@mi_blueprint.route('/so')
def index():
    return "Hola, a mi me gusta la pepsi a mi me gusta la cola pero lo que mas me gusta tus labios color rosa"
