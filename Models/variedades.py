from config.data import db
class VariedadUva(db.Model):
    __tablename__ = 'variedades_uva'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    nombre = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    foto_path = db.Column(db.String(255), nullable=True)  # Ruta a la imagen

    # Relaciones
    lotes = db.relationship('LoteUva', backref='variedad', lazy=True)
