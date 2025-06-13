
from Models.embotellado import Embotellado
from config.data import db
from flask import session,request, render_template,redirect,url_for,Blueprint
embotellado_bp=Blueprint("embotellado",__name__)
@embotellado_bp.route("/embotellado",methods=["POST"])

def cargar():
    if request.method=="POST":
        fecha_embotellado= request.form.get("fecha_embotellado")
        cantidad_botellas= request.form.get("cantidad_botellas")
        notas=request.form.get("notas")
        nueva_carga=Embotellado(fecha_embotellado=fecha_embotellado,cantidad_botellas=cantidad_botellas,notas=notas)
        db.session.add(nueva_carga)
        db.session.commit()
    return render_template("carga_embotellado.html")


@embotellado_bp.route("/obtener", methods=["GET"])
def obtener_datos():
    datos = Embotellado.query.all()
    

    return render_template("mostrar_datos.html",datos=datos)

@embotellado_bp.route("/embotellado/<int:id>",methods=["POST","GET"])
def modificar(id):
    datos=Embotellado.query.get_or_404(id)
    if request.method=="POST":
        datos.fecha_embotellado= request.form.get("fecha_embotellado")
        datos.cantidad_botellas=request.form.get("cantidad_botellas")
        datos.notas=request.form.get("notas")
        db.session.commit()
        return redirect(url_for("carga_embotellado"))
    return render_template("mostrar_datos.html",datos=datos)

@embotellado_bp.route("/embotellado/<int:id>", methods=["DELETE"])
def borrar(id):
    datos = Embotellado.query.get_or_404(id)
    
    
    db.session.delete(datos)
    db.session.commit()  
    return render_template("mostrar_datos.html",datos=datos)

