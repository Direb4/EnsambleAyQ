from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/proyectos")
def proyectos():
    return render_template("proyectos.html")

@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

