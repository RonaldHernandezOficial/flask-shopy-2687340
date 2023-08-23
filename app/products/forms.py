from flask_wtf import FlaskFrom
from wtform import StringField, SubmitField


# Formulario de registro de nuevo producto
class NewFroductForm (FlaskFrom):
    nombre=StringField("ingrese nombre: ")
    precio=StringField("ingrese precio: ")
    submit=SubmitField("Registrar")
