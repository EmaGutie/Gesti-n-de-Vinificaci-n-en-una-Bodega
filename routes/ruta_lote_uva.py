
from Models.lote_uva import LoteUva
from config.data import db
from flask import session,request,jsonify, render_template,redirect,url_for,Blueprint
import os
from werkzeug.utils import secure_filename
lote_bp=Blueprint("lote",__name__)
@lote_bp.route("/nuevo_lote",method=["POST"])
def nuevos_usuarios():
    if request.method=="POST":
        fecha_recepcion=request.form.get("fecha_recepcion")
       
        nuevo= LoteUva(fecha_recepcion=fecha_recepcion)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for("mostrar_lote"))
    return render_template("agregar_lote.html")
@lote_bp.route("/mostrar_lote",method="GET")
def obtener_registro():
    
    if request.method=="GET":
        registro=LoteUva.query.get()
       
    return render_template("mostrar_lote.html",registro=registro)
@lote_bp.route("/nuevo_lote/<int:id>",method=["POST","GET"])
def  modificar(id):
    
    variedad=LoteUva.query.get_or_404(id)
    if request.method=="POST":  
        variedad.fecha_recepcion= request.form.get("fecha_recepion")
       
        return redirect(url_for("nuevo"))
    return render_template("mostrar_lote.html",variedad=variedad)
    
    
@lote_bp.route("/nuevo_lote/<int:id>",method=["DELETE"])
def borrar(id):
    variedad=LoteUva.query.get_or_404(id)
    db.session.delete(variedad)
    db.session.commit()
    return render_template("mostrar_lote.html",variedad=variedad)

     