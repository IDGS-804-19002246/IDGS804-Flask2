from flask import Flask,render_template,request
app = Flask(__name__)


# sumar, promedio, mayor, menor y cuantas veces se repite 
@app.route("/CajasDinamicas", methods=['GET','POST'])
def CajasDinamicas():
    if request.method == 'POST':
        num0 = int(request.form.get('num0'))
        sumar = 0
        numList = []
        repetidos = []

        for x in range(num0):
            n = int(request.form.get('num'+str(x+1)))
            numList.append(n)
            repetidos.append(1)
            sumar += n

        mayor = max(numList)
        menor = min(numList)

        for n1 in range(len(numList)):
            for n2 in range(len(numList)):
                if numList[n1] == numList[n2] and n1!=n2:
                    repetidos[n1] += 1

        return render_template("CajasDinamicas2.html",
            s=sumar, p= float("{:.2f}".format(sumar/num0)) , ma=mayor, me=menor, r = repetidos)
    else:
        return render_template("CajasDinamicas.html")
    


if __name__ == '__main__':
    app.run(debug=True)