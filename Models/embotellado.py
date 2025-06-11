<<<<<<< HEAD
from config.data import db,engine
=======
from uuid import uuid4
from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid():
    return str(uuid4())

>>>>>>> 59ff88af4df3e4b4d36f4ffeaa25143a0dd7792a
class Embotellado(db.Model):
    __tablename__ = 'embotellados'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    lote_id = db.Column(db.String(36), db.ForeignKey('lotes_uva.id'), nullable=False)
<<<<<<< HEAD
    fecha_embotellado = db.Column(db.Date, nullable=False)
    cantidad_botellas = db.Column(db.Integer,nullable=False)
    notas = db.Column(db.Text)
db.metadata.create_all(engine)
=======
    fecha_embotellado = db.Column(db.Date, nullable=False, default=date.today)
    cantidad_botellas = db.Column(db.Integer)
    notas = db.Column(db.Text)
>>>>>>> 59ff88af4df3e4b4d36f4ffeaa25143a0dd7792a
