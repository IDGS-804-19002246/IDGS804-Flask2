from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, FieldList, FormField, RadioField, SelectField
from wtforms.fields import EmailField

from wtforms import validators
def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',
        [validators.DataRequired('El campo es requerido'),
            validators.length(min=5,max=10,message='Ingresa un min 5 y max 10')])
    nombre = StringField('Nombre',
        [validators.DataRequired('El campo es requerido')])

    # matricula = StringField ('Matricula')
    # nombre = StringField('Nombre')
    apaterno = StringField('Apaterno',[
        mi_validacion
    ])
    amaterno = StringField('Amaterno')
    email = EmailField('Correo')

class LoginForm(Form):
    Username = StringField('Usuario',
        [validators.DataRequired('El campo Usuario es requerido'),
            validators.length(min=5,max=10,message='Ingresa un min 5 y max 10')])
    Password = PasswordField('Contraceña',
        [validators.DataRequired('El campo Contraceña es requerido'),
            validators.length(min=5,max=10,message='Ingresa un min 5 y max 10')])
