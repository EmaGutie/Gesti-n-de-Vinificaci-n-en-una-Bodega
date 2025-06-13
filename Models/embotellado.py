from config.data import db,engine
class Embotellado(db.Model):
    __tablename__ = 'embotellados'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    lote_id = db.Column(db.String(36), db.ForeignKey('lotes_uva.id'), nullable=False)
    fecha_embotellado = db.Column(db.Date, nullable=False)
    cantidad_botellas = db.Column(db.Integer,nullable=False)
    notas = db.Column(db.Text)
db.metadata.create_all(engine)