#Dependencia de flask
from flask import Flask
#Dependencias de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de migraciones
from flask_migrate import Migrate

#Crear el objeto Flask
app = Flask(__name__)

#Definir la 'cadena de conexión' o en inglés = (connectionstring) para la base de datos del proyecto
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

#Crear el objeto para crear modelos
db = SQLAlchemy(app)

#Crear el objeto de la migración
migrate = Migrate(app, db) #Este pide el objeto flask y el db

#Dependencia para fecha y hora del sistema
from datetime import datetime

#Crear lo modelos
class Cliente(db.Model):
    #Definir los atributos
    __tablename__ = "clientes"
    id = db.Column(db.Integer , primary_key = True)
    user = db.Column(db.String(120) , nullable = True)
    password = db.Column(db.String(128) , nullable = True)
    email = db.Column(db.String(120) , nullable = True)

#Crear lo modelos
class Producto(db.Model):
    #Definir los atributos
    __tablename__ = "productos"
    id = db.Column(db.Integer , primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))

class Venta(db.Model):
    #Definir los atributos
    __tablename__ = "ventas"
    id = db.Column(db.Integer , primary_key = True)
    fecha = db.Column(db.DateTime , default = datetime.utcnow)
    #Clave foránea
    cliente_id = db.Column(db.Integer , db.ForeignKey('clientes.id'))

class Detalle(db.Model):
    #Definir los atributos
    __tablename__ = "detalles"
    id = db.Column(db.Integer , primary_key = True)
    producto_id = db.Column(db.Integer , db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer , db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)
