from flask import Flask, redirect, render_template, request
from cs50 import SQL
import smtplib
from email.mime.text import MIMEText

# Configure application
app = Flask(__name__)
db = SQL("sqlite:///ensamble.db")

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/proyectos")
def proyectos():
    proyectos = db.execute("SELECT nombre FROM proyectos")
    proyectos = [d['nombre'] for d in proyectos]
    seleccion = request.args.get("proyecto")
    return render_template("proyectos.html", proyectos=proyectos)

@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")

@app.route("/contacto", methods=['GET','POST'])
def contacto():
    if request.method == "GET":
        return render_template("contacto.html")
    else:
        def send_email(subject, body, sender, recipient, password):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipient
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipient, msg.as_string())
        de = request.form.get("email")
        nl = '\n'
        nombre = request.form.get("fullname")
        telefono = request.form.get("phone")
        mensaje = f'Mensaje enviado por: {nombre}{nl}Correo: {de}{nl}Número de teléfono: {telefono}{nl}Mensaje: {request.form.get("message")}'
        asunto = request.form.get("subject")
        correo = "drebolledotome@gmail.com"
        password = "rafx bgnp fahi cuoz"
        send_email(asunto, mensaje, correo, correo, password)
        return redirect("/contacto")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

if __name__ == '__main__':
    app.run() 
