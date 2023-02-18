from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, RadioField, SelectField

from wtforms.fields import EmailField

class UserForm(Form):
    matricula = StringField ('Matricula')
    nombre = StringField('Nombre')
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno')
    emal = EmailField('Correo')