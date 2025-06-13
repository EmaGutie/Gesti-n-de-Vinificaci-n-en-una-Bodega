import os
import uuid
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename 
from routes.routes_embotellado import embotellado_bp
from routes.routes_vinos import vinos_bp
from routes.ruta_crianza import crianza_bp
from routes.ruta_fermentacion import fermentacion_bp
from routes.ruta_lote_uva import lote_bp
from config.data import DATA_BASE_URL
app = Flask(__name__)


app=Flask(__name__)
app.config["DATA_BASE_URL"]=DATA_BASE_URL
app.config["DATA_TRACK_MODIFICATION"]=False
app.register_blueprint(embotellado_bp)
app.register_blueprint(vinos_bp)
app.register_blueprint(crianza_bp)
app.register_blueprint(fermentacion_bp)
app.register_blueprint(lote_bp)

UPLOAD_FOLDER = 'static/uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


grape_varieties_db = []
process_records_db = {
    'reception': [],
    'fermentation': [],
    'aging': [],
    'bottling': []
}

def allowed_file(filename):
    """Verifica si la extensión del archivo es permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Ruta principal: renderiza la página HTML."""
    return render_template('index.html')


@app.route('/api/varieties', methods=['GET', 'POST'])
def handle_varieties():
    """
    GET: Retorna todas las variedades de uva registradas.
    POST: Registra una nueva variedad de uva.
    """
    if request.method == 'POST':
        data = request.json
        if not data or 'nombre' not in data or 'origen' not in data:
            return jsonify({'error': 'Faltan datos (nombre, origen)'}), 400

        new_variety = {
            'id': str(uuid.uuid4()), 
            'nombre': data['nombre'],
            'origen': data['origen'],
            'foto': data.get('foto', '') 
        }
        grape_varieties_db.append(new_variety)
        return jsonify({'message': 'Variedad registrada con éxito', 'variety': new_variety}), 201
    else: 
        return jsonify(grape_varieties_db)

@app.route('/api/upload_photo', methods=['POST'])
def upload_photo():
    """Sube una imagen al servidor y retorna su nombre de archivo."""
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró el archivo en la solicitud'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = str(uuid.uuid4()) + '_' + filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        return jsonify({'filename': unique_filename, 'url': f'/{app.config["UPLOAD_FOLDER"]}/{unique_filename}'}), 200
    else:
        return jsonify({'error': 'Tipo de archivo no permitido'}), 400


@app.route('/api/process_records', methods=['GET', 'POST'])
def handle_process_records():
    """
    GET: Retorna todos los registros de proceso.
    POST: Registra un nuevo dato de etapa de proceso.
    """
    if request.method == 'POST':
        data = request.json
        stage = data.get('stage')
        if not stage or stage not in process_records_db:
            return jsonify({'error': 'Etapa de proceso inválida'}), 400

        record_id = str(uuid.uuid4())
        record_data = {
            'id': record_id,
            **{k: v for k, v in data.items() if k != 'stage'} 
        }
        process_records_db[stage].append(record_data)

        return jsonify({'message': f'Registro de {stage} guardado con éxito', 'record': record_data}), 201
    else: 
        return jsonify(process_records_db)

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    """Sirve los archivos subidos desde la carpeta de uploads."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)



