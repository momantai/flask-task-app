from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User

# Ejemplo de función que puede ser utilizada para validar un campo.
# Recibe el formulario y el campo.
def codi_validator(form, field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('El username codi no es permitido.')

# Validación que un bot no puede pasar, anti-spam.
def length_honeypot(form, field):
    if  len(field.data) > 0:
        raise validators.ValidationError('Solo humanos pueden registrarse.')

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango.')
    ])
    password = PasswordField('Password', [
        validators.Required(message='El password es requerido.')
    ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50),
        codi_validator
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    password = PasswordField('Password', [
        validators.Required('El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coinciden.')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField([
        validators.DataRequired()
    ])
    honeypot = HiddenField("", [length_honeypot])

    # Validación por metodo para un campo.
    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username: '+ username.data +', ya esta en uso.')
    
    # Validar si un correo ya existe en la base de datos.
    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('Este email ya existe.')
    
    # Sobre escribiendo el metodo validate para generar nuestras propias palidaciones
    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password.data) < 3:
            self.password.errors.append('El password es muy corto.')
            return False

        return True

class TaskForm(Form):
    title = StringField('Titulo', [
        validators.length(min=4, max=50, message='Fuera de rango.'),
        validators.DataRequired(message='Este campo es requerido.')
    ])
    description = TextAreaField('Descripción', [
        validators.DataRequired(message='La descripción es requerida.')
    ], render_kw={'rows':5})