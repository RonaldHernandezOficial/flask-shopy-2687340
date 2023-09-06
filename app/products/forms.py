from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import  InputRequired, NumberRange
#Esto es para poder agregar imagenes
from flask_wtf.file import FileField, FileRequired, FileAllowed

# Formulario de registro de nuevo producto
class NewProductForm (FlaskForm):
    nombre = StringField(validators = [ InputRequired( message="Falta el nombre" ) ], label = "Ingrese nombre: ")
    precio = IntegerField(label = "Ingrese precio: " , validators = [ InputRequired( message = "Falta el precio" ),
                                                                     NumberRange( message = "Precio fuera de rango", 
                                                                                 min = 1000, 
                                                                                 max = 10000 )])
    imagen = FileField(label = "Cargue imagén del producto " , validators = [ FileRequired( message = "Falta la imagén, suba una imagén" ) ,
                                                                             FileAllowed(["jpg" , "png"],
                                                                                         message = "Tipo de archivo incorrecto")])
    submit = SubmitField("Registrar")
