from flask import Flask,render_template,request
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY']="ESTA ES UNA CLAVE SECRETA"
csrf=CSRFProtect()


@app.route("/FormPrueba")
def FormPrueba():
    return render_template("FormPrueba.html")


@app.route("/Alumnos", methods=['GET','POST'])
def Alumnos():
    reg_alum = forms.UserForm(request.form)
    if request.method == 'POST':
        print(reg_alum.nombre.data)
        print(reg_alum.matricula.data)

    return render_template("Alumnos.html",form=reg_alum)



@app.route("/CajasDinamicas", methods=['GET','POST'])
def CajasDinamicas():
    reg_alum = forms.UserForm(request.form)
    if request.method == 'POST':
        print(reg_alum.nombre.data)
        print(reg_alum.matricula.data)

    return render_template("Alumnos.html",form=reg_alum)


if __name__ == '__main__':
    app.run(debug=True)
# http://127.0.0.1:5000
# Guion bajo es pa indicar que es pribado el archivo/dato