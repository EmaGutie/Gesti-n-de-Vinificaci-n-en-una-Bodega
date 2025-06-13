from flask import Flask
from routes.routes_embotellado import embotellado_bp
from routes.routes_vinos import vinos_bp
from routes.ruta_crianza import crianza_bp
from routes.ruta_fermentacion import fermentacion_bp
from routes.ruta_lote_uva import lote_bp
from config.data import DATA_BASE_URL
app=Flask(__name__)
app.config["DATA_BASE_URL"]=DATA_BASE_URL
app.config["DATA_TRACK_MODIFICATION"]=False
app.register_blueprint(embotellado_bp)
app.register_blueprint(vinos_bp)
app.register_blueprint(crianza_bp)
app.register_blueprint(fermentacion_bp)
app.register_blueprint(lote_bp)
@app.route("/index")
def home():
    return 
if __name__=="__main__":
    app.run(debug=True)