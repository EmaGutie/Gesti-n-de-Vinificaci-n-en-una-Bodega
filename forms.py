from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class VariedadForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    origen = StringField('Origen', validators=[DataRequired()])
    foto = FileField('Foto', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imágenes.')])
    submit = SubmitField('Guardar')
