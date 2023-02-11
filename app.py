from flask import Flask,render_template,request
app = Flask(__name__)



@app.route("/FormPrueba")
def FormPrueba():
    return render_template("FormPrueba.html")



if __name__ == '__main__':
    app.run(debug=True)
# http://127.0.0.1:5000
# Guion bajo es pa indicar que es pribado el archivo/dato