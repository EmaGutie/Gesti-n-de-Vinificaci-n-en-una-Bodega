from config.data import db
class Crianza(db.Model):
    __tablename__ = 'crianzas'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    lote_id = db.Column(db.String(36), db.ForeignKey('lotes_uva.id'), nullable=False)
    tipo_recipiente = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    observaciones = db.Column(db.Text)
