from flask import render_template
from . import products
from . forms import NewProductForm
import app
#Carpeta "os" para la manipulación de carpetas a nivel de sistema operativo
import os

@products.route('/create' , methods = ["GET" , "POST"])
def crear_producto():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        #LLenar atributos del objeto producto con el formulario
        form.populate_obj(p)
        #Registrar producto en bd
        #Con este objeto es como se hace la inserción del crud
        app.db.session.add(p)
        p.imagen = form.imagen.data.filename
        #Este es para que quede insertado en la bd
        app.db.session.commit()


        #Trasladar la imagén cargada a la carpeta app/productos/imagenes
        archivo = form.imagen.data
        #Save no funciona con scripts, solo con rutas os
        archivo.save( os.path.abspath( os.getcwd() + '/app/products/imagenes/' + p.imagen ) )

        return os.getcwd()
        return "producto registrado"
    return render_template('new.html',
                           form = form)
