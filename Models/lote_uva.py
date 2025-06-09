class LoteUva(db.Model):
    __tablename__ = 'lotes_uva'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    fecha_recepcion = db.Column(db.Date, nullable=False)
    variedad_id = db.Column(db.String(36), db.ForeignKey('variedades_uva.id'), nullable=False)

    # Relaciones
    fermentacion = db.relationship('Fermentacion', uselist=False, backref='lote')
    crianza = db.relationship('Crianza', uselist=False, backref='lote')
    embotellado = db.relationship('Embotellado', uselist=False, backref='lote')
