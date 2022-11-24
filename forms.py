from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Email, Length
from static.Lista_de_paises import Paises

#Formulario de registro
class Registro(FlaskForm):
    Nombre = StringField('Nombre', validators=[DataRequired(), Length(max=45)])
    Apellido = StringField('Apellido', validators=[DataRequired(), Length(max=45)])
    Edad = IntegerField('¿Qué edad tienes?', validators=[DataRequired()])
    Genero = SelectMultipleField('Selecciona genero con el que te identificas:', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], validators=[DataRequired(), Length(max=45)])
    Correo = StringField('Correo', validators=[DataRequired(), Email()])
    Pais = SelectMultipleField('Selecciona país de recidencia:', choices=Paises, validators=[DataRequired(), Length(max=45)])
    Password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registro')
