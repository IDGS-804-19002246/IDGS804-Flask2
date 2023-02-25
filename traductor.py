# esp {input}
# ing {input}
# save {save}
# --------------
# esp {radio}
# ing {radio}

# traducir {input}
# traducir {button}

from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, RadioField, SelectField
from wtforms import validators

def NoVacio(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')
def NoNumeros(form,field):
    if len(field.data) != 0:
        for c in str(field.data):
            if c.isalpha() != True or c == ' ':
                raise validators.ValidationError('El campo no debe contener números ni espacios')
    
class traducirIn(Form):
    ing = StringField('ing',[NoVacio,NoNumeros])
    esp = StringField('esp',[NoVacio,NoNumeros])
    envio = StringField('envio')

class traducirOut(Form):
    pal = StringField('pal',[NoVacio,NoNumeros])
    idioma = StringField('idioma')
    envio = StringField('envio')