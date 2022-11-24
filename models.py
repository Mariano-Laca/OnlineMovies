from flask_login import UserMixin #Importamos la clase UserMixin
from werkzeug.security import generate_password_hash, check_password_hash #Password
from datetime import datetime #Importamos "datetime" para las fechas.

from flask_sqlalchemy import SQLAlchemy #Importamos SQLAlchemy
db = SQLAlchemy() #Creamos la instancia db

class Usuarios(db.Model, UserMixin):
    __tablename__="Usuarios"
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(45), nullable=False)
    Apellido = db.Column(db.String(45), nullable = False)
    Edad = db.Column(db.Integer, nullable = False, default = 0)
    Genero = db.Column(db.String(45), nullable = True, default = ('None'))
    Correo = db.Column(db.String(45), nullable = False)
    Pais = db.Column(db.String(45), nullable = True, default = ('None'))
    Password = db.Column(db.String(250), nullable = False)
    Rango = db.Column(db.Integer, nullable = False, default = 0)
    
    #Referencia del usuario - Mostrar el correo.
    def __repr__(self):
        return f'<Usuario {self.Correo}>'
    #Generar un Hash del password
    def set_Password(self, Password):
        self.Password = generate_password_hash(Password)
    #Comprobar que el hash del password coincida
    def check_password(self, password):
        return check_password_hash(self.Password, password)
    #Guardar en la base de datos
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


class Movies(db.Model):
    __tablename__="Movies"
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, nullable = False)
    id_movie = db.Column(db.Integer, nullable = False)
    action = db.Column(db.Integer, nullable = True)
    date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    def __init__(self,id_user, id_movie, action):
        self.id_user = id_user
        self.id_movie = id_movie
        self.action = action
        self.date = datetime.utcnow()
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
