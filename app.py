# Dependencia del flask
from flask import Flask
# Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
# Dependencia de migraciones
from flask_migrate import Migrate
# Dependencia para fecha y hora
from datetime import datetime

# Crear el objeto flask
app = Flask(__name__)


# Definir la cadena de conexion(conection string)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

# Crear el objeto de modelos
db = SQLAlchemy(app)

# Crear el objeto de migracion
migrate = Migrate(app, db)

# Crear los modelos
class Cliente(db.Model):
    # Definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(120), nullable = True)

# Crear los modelos
class Producto(db.Model):
    # Definir los atributos
    __tablename__="productos"
    id = db.Column(db.Integer , primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))

# Crear los modelos
class Venta(db.Model):
    # Definir los atributos
    __tablename__="ventas"
    id = db.Column(db.Integer , primary_key = True)
    fecha = db.Column(db.DateTime , default = datetime.utcnow)
    # Clave foranea
    cliente_id = db.Column(db.Integer , db.ForeignKey('clientes.id'))

    # Crear los modelos
class Detalle(db.Model):
    # Definir los atributos
    __tablename__="detalles"
    id = db.Column(db.Integer , primary_key = True)
    producto_id = db.Column(db.Integer , db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer , db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

