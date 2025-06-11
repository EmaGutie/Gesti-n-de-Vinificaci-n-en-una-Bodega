<<<<<<< HEAD
from config.data import db,engine
=======
>>>>>>> 59ff88af4df3e4b4d36f4ffeaa25143a0dd7792a
class VariedadUva(db.Model):
    __tablename__ = 'variedades_uva'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    nombre = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    foto_path = db.Column(db.String(255), nullable=True)  # Ruta a la imagen

    # Relaciones
    lotes = db.relationship('LoteUva', backref='variedad', lazy=True)
<<<<<<< HEAD
db.metadata.create_all(engine)
=======
>>>>>>> 59ff88af4df3e4b4d36f4ffeaa25143a0dd7792a
