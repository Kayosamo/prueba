#para utilizar gmail se debe instalar pip install yagmail
from flask import Flask, render_template, request
import yagmail
app=Flask(__name__)

@app.route("/")
def home():
    return "Hola"

@app.route("/saludo")
def home2():
    return "Buenos días"

#RUTA DINAMICA...PIDE EL NOMBRE 
@app.route("/saludo/<nom>")
def saludo_personal(nom):
    return f"Binevenid@, {nom}"

@app.route("/saludo/<nom>/<ciudad>")
def saludo_personal2(nom,ciudad):
    return f"Binevenid@, {nom}, te saludamos desde {ciudad}"

#RUTA DINAMICA...PIDE LA VARIABLE CON EL TIPO DE DATO
@app.route("/productos/<int:cod>")
def producto (cod):
    return f"La manzana tiene codigo, {cod}"

#ejecuta el archivo html prod
@app.route("/prod")
def home3():
    return render_template("prod.html")

#capturar los datos de la caja y los envia con GET (se dejan ver en la url)
@app.route("/producto/save")
def guardar_producto():
    cod = request.args.get("codigo")
    nom = request.args.get("nombre")
    pre = request.args.get("precio")

    return f"Código: {cod}, Nombre: {nom}, Precio: {pre}"

#capturar los datos de la caja y los envia con POST (NO se dejan ver en la url)
@app.route("/producto/save", methods=["POST"])
def guardar_producto_conpost():
    cod = request.form["codigo"]
    nom = request.form["nombre"]
    pre = request.form["precio"]

    return f"Código: {cod}, Nombre: {nom}, Precio: {pre}"

#envio de correo
#se debe permitir el envio https://myaccount.google.com/lesssecureapps
@app.route("/correo")
def enviar_correo():
    correo=yagmail.SMTP("kysanchez@uninorte.edu.co","Alejandro2009")
    correo.send("kysanchez@uninorte.edu.co", "Prueba desde Python", "Prueba")
    return "Correo enviado"