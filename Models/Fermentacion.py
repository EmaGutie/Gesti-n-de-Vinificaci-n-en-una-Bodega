from config.data import db
class Fermentacion(db.Model):
    __tablename__ = 'fermentaciones'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    lote_id = db.Column(db.String(36), db.ForeignKey('lotes_uva.id'), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=True)
    temperatura = db.Column(db.Float)
    densidad = db.Column(db.Float)
    pH = db.Column(db.Float)
    acidez_total = db.Column(db.Float)
