from app.app import app
from Models.Crianza import Crianza
from config.data import db
from flask import session,request, render_template,redirect,url_for
@app.route("/crianza",methods=["POST"])
def cargar():
    if request.method=="POST":
        tipo_de_recipiente= request.form.get("tipo_de_recipiente")
        fecha_de_inicio= request.form.get("fecha_de_iniio")
        observaciones=request.form.get("observaciones")
        nueva_carga=Crianza(tipo_de_recipiente=tipo_de_recipiente,fecha_de_inicio=fecha_de_inicio,observaciones=observaciones)
        db.session.add(nueva_carga)
        db.session.commit()
    return render_template("carga_crianza.html")


@app.route("/obtener_datos_crianza", methods=["GET"])
def obtener_datos():
    datos = Crianza.query.all()
    

    return render_template("mostrar_datos_crianza.html",datos=datos)

@app.route("/embotellado/<int:id>",methods=["POST","GET"])
def modificar(id):
    datos=Crianza.query.get_or_404(id)
    if request.method=="POST":
        datos.tipo_de_recipiente= request.form.get(" tipo_de_recipiente")
        datos.fecha_de_inicio=request.form.get("fecha_de_inicio")
        datos.observaciones=request.form.get("observaciones")
        db.session.commit()
        return redirect(url_for("carga_crianza"))
    return render_template("mostrar_datos_crianza.html",datos=datos)

@app.route("/embotellado/<int:id>", methods=["DELETE"])
def borrar(id):
    datos = Crianza.query.get_or_404(id)
    
    
    db.session.delete(datos)
    db.session.commit()  
    return render_template("mostrar_datos_crianza.html",datos=datos)
