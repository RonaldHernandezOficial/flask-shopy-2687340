# Dependencia del flask
from flask import Flask, render_template
# Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
# Dependencia de migraciones
from flask_migrate import Migrate
# Dependencia para fecha y hora
from datetime import datetime
# Dependencia de wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# Crear el objeto flask
app = Flask(__name__)


# Definir la cadena de conexion(conection string)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = 'so'

# Crear el objeto de modelos
db = SQLAlchemy(app)

# Crear el objeto de migracion
migrate = Migrate(app, db)

# Formulario Registro de productos
class ProductosForm(FlaskForm):
    nombre = StringField('ingrese nombre producto')
    precio = StringField('ingrese precio producto')
    submit = SubmitField('ingrese registrar producto')

# Crear los modelos
class Cliente(db.Model):
    # Definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(120), nullable = True)

    # Relaciones SQL alchemy
    ventas = db.relationship('Venta' , backref = "cliente" , lazy = "dynamic")

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

 # Rutas
@app.route('/productos',  methods = ['GET' ,'POST'])
def nuevo_producto():
    form = ProductosForm()
    if form.validate_on_submit():
        # Creamos un nuevo producto
        p = Producto(nombre = form.nombre.data, precio = form.precio.data)
        db.session.add(p)
        db.session.commit()
        return "Producto registrado :)"
    return render_template('nuevo_producto.html' , form = form)