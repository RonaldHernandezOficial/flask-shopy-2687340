# Dependencia del flask
from flask import Flask

# Dependencia de configuracion
from .config import Config

# Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
# Dependencia de migraciones
from flask_migrate import Migrate

# Crear el objeto flask
app = Flask(__name__)


# Configuracion objeto flask
app.config.from_object(Config)


# Crear el objeto de modelos
db = SQLAlchemy(app)

# Crear el objeto de migracion
migrate = Migrate(app, db)

# Importar modelos de .models
from .models import Cliente, Venta, Detalle, Producto