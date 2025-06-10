from uuid import uuid4
from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid():
    return str(uuid4())


class Crianza(db.Model):
    __tablename__ = 'crianzas'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    lote_id = db.Column(db.String(36), db.ForeignKey('lotes_uva.id'), nullable=False)
    tipo_recipiente = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False, default=date.today)
    observaciones = db.Column(db.Text)

lote = db.relationship('lote_uva', backref=db.backref('crianza', lazy=True))