#Import
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import config #importamos el archivo de configuración "config.py"
from forms import Registro#Importamos el formulario de registro
from models import db, Usuarios, Movies #Importamos la DB

#Instancia +config 
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(config)
db.init_app(app)

#Rutas
@app.route('/')
def inicio():
    return ('Hola esta es la página de inicio')

@app.route('/registro', methods = ['GET','POST'])
def registro():
    form = Registro()
    if form.validate_on_submit():
        Nombre = form.Nombre.data
        Apellido = form.Apellido.data
        Edad = form.Edad.data
        Genero = form.Genero.data
        Correo = form.Correo.data
        Pais = form.Pais.data
        Password = form.Password.data

        user = Usuarios(Nombre=Nombre, Apellido = Apellido, Edad = Edad, Genero = Genero, Correo=Correo, Pais = Pais, Password = Password)
        user.set_Password(Password)
        user.save()
            # Dejamos al usuario logueado
    return render_template('registro.html', form=form)

with app.app_context():
    db.create_all()
    db.session.commit()
    
    users = Usuarios.query.all()
    print(users)
#Run
if __name__ == '__main__':
    app.run(debug=True)
