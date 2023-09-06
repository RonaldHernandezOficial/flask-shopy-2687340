# Dependencia del flask
from flask import Flask

# Dependencia de configuracion
from .config import Config

# Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
# Dependencia de migraciones
from flask_migrate import Migrate

# Importar el mi_blueprint
from .mi_blueprint import mi_blueprint

from app.products import products
# Dependencia Bootstrap
from flask_bootstrap import Bootstrap

# Crear el objeto flask
app = Flask(__name__)

# Configuracion objeto flask
app.config.from_object(Config)

# Vincular blueprint del proyecto 
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)


# Crear el objeto de modelos
db = SQLAlchemy(app)

# Crear el objeto de migracion
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

# Crear objeto bootstrap

# Importar modelos de .models
from .models import Cliente, Venta, Detalle, Producto

