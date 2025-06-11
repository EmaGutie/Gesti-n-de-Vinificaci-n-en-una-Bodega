from app.app import app
from Models.variedades import VariedadUva
from config.data import db,engine
from flask import session,request,jsonify, render_template,redirect,url_for
import os
from werkzeug.utils import secure_filename

@app.route("/nuevo",method=["POST"])
def nuevos_usuarios():
    if request.method=="POST":
        nombre=request.form["nombre"]
        origen=request.form["origen"]
        tanque=request.form["tanque"]
        nuevo= VariedadUva(nombre=nombre,origen=origen,tanque=tanque)
        db.session.add(nuevo)
        db.session.commit()
        return render_template("agregar_usuarios.html")
    return redirect(url_for("mostrar_datos"))
@app.route("/index",method="GET")
def obtener_registro():
    
    if request.method=="GET":
        registro=VariedadUva.query.get()
       
    return render_template("mostrar_datos.html",registro=registro)
@app.route("/nuevo/<int:id>",method=["POST","GET"])
def  modificar(id):
    
    variedad=VariedadUva.query.get_or_404(id)
    if request.method=="POST":  
        variedad.nombre= request.form.get("nombre")
        variedad.origen=request.form.get("origne")
        imagen= request.files.get("foto_patch")
        if imagen and imagen.filename:
            filename= secure_filename(imagen.filename)
            imagen.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            variedad.imagen=filename
        db.session.commit
        return redirect(url_for("nuevo"))
    return render_template("mostrar_datos.html",variedad=variedad)
    
    
app.route("/nuevo/<int:id>",method=["DELETE"])
def borrar(id):
    variedad=VariedadUva.query.get_or_404(id)
    db.session.delete(variedad)
    db.session.commit()
    return render_template("mostrar_datos.html",variedad=variedad)
db.metadata.create_all(engine)     
          
        
        
        
