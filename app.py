#Dependencia de flask
from flask import Flask, render_template

#Dependencias de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de migraciones
from flask_migrate import Migrate

#Dependencia para fecha y hora del sistema
from datetime import datetime

#Dependencias de wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#Crear el objeto Flask
app = Flask(__name__)

#Definir la 'cadena de conexión' o en inglés = (connectionstring) para la base de datos del proyecto
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ficha2687340'

#Crear el objeto para crear modelos
db = SQLAlchemy(app)

#Crear el objeto de la migración
migrate = Migrate(app, db) #Este pide el objeto flask y el db

#Crear formulario de registro de productos
class ProductosForm(FlaskForm):
    nombre = StringField('Ingresa nombre de producto')
    precio = StringField('ingresa precio de producto')
    submit = SubmitField('Registrar Producto')


#Crear lo modelos
class Cliente(db.Model):
    #Definir los atributos
    __tablename__ = "clientes"
    id = db.Column(db.Integer , primary_key = True)
    user = db.Column(db.String(120) , nullable = True)
    password = db.Column(db.String(128) , nullable = True)
    email = db.Column(db.String(120) , nullable = True)
    #Relaciones SQL alchemy
    #Relaciones se hacen con el código de abajo
    #El backref es por cada instancia habra una relación o por su vez al reves
    venta = db.relationship('Venta' , backref = "cliente" , lazy = "dynamic")

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

#Rutas: 
@app.route('/productos', methods = ['GET', 'POST'])
def nuevo_producto():
    form = ProductosForm()
    if form.validate_on_submit():
        #Creamos un nuevo Producto
        p = Producto(nombre = form.nombre.data, precio = form.precio.data)
        db.session.add(p)
        db.session.commit()
        return "Produto Registrado"
    return render_template('nuevo_producto.html', form = form)


#ORM Tipo de componente que te permite hacer lo siguiente = "Dado los registros convertirlos en un objeto o modelo y viseversa"

#Las subconsola de python es espcial para las intrucciones que este mismo necesite, solo funcionara en esta

#No hay qu poner las id, debido a que se iran ingresando automaticamente

#query.get() obtener instancia +

#Se agregan así = p3 = Producto(nombre = "Nintendo Switch", precio = 1.40)

#Se insetan así = db.session.add(p3)  
#>>> db.session.commit()

#Se pueden editar los datos ingresados: >>> p1.nombre = "XBOX serie X" , con el código anterior 

#Con este se consulta = >>> productos = Producto.query.all()

"""
>>> productos = Producto.query.all()
>>> productos  
[<Producto 1>, <Producto 2>, <Producto 3>, <Producto 4>]
>>>
"""

#en python no se usa la nomenclatura camelCase estilizado como camelCase