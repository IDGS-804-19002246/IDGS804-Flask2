from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/resistencia", methods=['GET','POST'])
def resistencia():
    colores=[
        ['Negro',0,1,'#000'],#0
        ['Cafe',1,10,'#582b03'],#1
        ['Rojo',2,100,'#f00'],#2
        ['Naranja',3,1000,'#ff6600'],#3
        ['Amarillo',4,10000,'#ff0'],#4
        ['Verde',5,100000,'#007e0f'],#5
        ['Azul',6,1000000,'#005990'],#6
        ['Violeta',7,10000000,'#710090'],#7
        ['Gris',8,100000000,'#606060'],#8
        ['Blanco',9,1000000000,'#fff']#9
    ]
    salida = []
    if request.method == 'POST':
        if request.form.get('envio') == 'gua':
            b1 = str(request.form.get('barra1'))
            b2 = str(request.form.get('barra2'))
            b3 = int(request.form.get('barra3'))
            tol = int(request.form.get('tol'))
            
            if b1 == '0': b1 = b1.replace('0','')
            valor = int(b1+b2)*b3
            min = '{:.2f}'.format( valor*(1-(tol/100)) )
            max = '{:.2f}'.format( valor*(1+(tol/100)) )
            if b1 == '': b1 = b1.replace('','0')

            salida.append([int(b1),int(b2),len(str(b3))-1,tol,str(valor),str(max),str(min)])

            e=open('resistencia.txt','a')
            e.write(str([int(b1),int(b2),len(str(b3))-1,tol,str(valor),str(max),str(min)])+'\n')
        else:
            e = open('resistencia.txt','r')
            arrays = e.readlines()
            for a in arrays:
                salida.append(eval(a.replace('\n','')))

    return render_template("resistencia.html",c=colores,salida=salida)


if __name__ == '__main__':
    app.run(debug=True)