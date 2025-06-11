from app.app import app
from Models.Fermentacion import Fermentacion
from config.data import db
from flask import session,request, render_template,redirect,url_for
@app.route("/fermentacion",methods=["POST"])
def cargar():
    if request.method=="POST":
       
        fecha_inicio= request.form.get("fecha_inicio")
        fecha_fin=request.form.get("fecha_fin")
        temperatura= request.form.get("temeperatura")
        densidad=request.form.get("densidad")
        ph=request.form.get("ph")
        acidez_total=request.form.get("acidez_total")
        nueva_carga=Fermentacion(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,temperatura=temperatura,densidad=densidad,ph=ph,acidez_total=acidez_total)
        db.session.add(nueva_carga)
        db.session.commit()
    return render_template("carga_fermentacion.html")


@app.route("/obtener_datos_fermentacion", methods=["GET"])
def obtener_datos():
    datos = Fermentacion.query.all()
    

    return render_template("mostrar_datos_fermentacion.html",datos=datos)

@app.route("/fermentacion/<int:id>",methods=["POST","GET"])
def modificar(id):
    datos=Fermentacion.query.get_or_404(id)
    if request.method=="POST":
        datos.fecha_inicio= request.form.get(" fecha_inicio")
        datos.fecha_fin=request.form.get("fecha_fin")
        datos.temperatura=request.form.get("temperatura")
        datos.densidad=request.form.get("densidad")
        datos.ph=request.form.get("ph")
        datos.acidez_total=request.form.get("acidez_total")
        db.session.commit()
        return redirect(url_for("carga_fermentacion"))
    return render_template("mostrar_datos_fermentacion.html",datos=datos)

@app.route("/fermentacion/<int:id>", methods=["DELETE"])
def borrar(id):
    datos = Fermentacion.query.get_or_404(id)
    
    
    db.session.delete(datos)
    db.session.commit()  
    return render_template("mostrar_datos_fermentacion.html",datos=datos)