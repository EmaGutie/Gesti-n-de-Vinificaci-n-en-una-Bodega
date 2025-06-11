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
class Crianza(db.Model):
    __tablename__ = 'crianzas'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    lote_id = db.Column(db.String(36), db.ForeignKey('lotes_uva.id'), nullable=False)
    tipo_recipiente = db.Column(db.String(100), nullable=False)
<<<<<<< HEAD
    fecha_inicio = db.Column(db.Date, nullable=False)
    observaciones = db.Column(db.Text)
db.metadata.create_all(engine)
=======
    fecha_inicio = db.Column(db.Date, nullable=False, default=date.today)
    observaciones = db.Column(db.Text)

lote = db.relationship('lote_uva', backref=db.backref('crianza', lazy=True))
>>>>>>> 59ff88af4df3e4b4d36f4ffeaa25143a0dd7792a
