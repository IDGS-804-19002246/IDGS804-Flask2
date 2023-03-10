from flask import Flask,render_template,request
from flask import flash,make_response
import forms
import traductor
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# app.config['SECRET_KEY']="ESTA ES UNA CLAVE SECRETA"
# csrf=CSRFProtect()


@app.route("/FormPrueba")
def FormPrueba():
    return render_template("FormPrueba.html")

@app.route("/Alumnos", methods=['GET','POST'])
def Alumnos():
    reg_alum = forms.UserForm(request.form)
    datos = list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)

        print(reg_alum.nombre.data)
        print(reg_alum.matricula.data)


    return render_template("Alumnos.html",form=reg_alum, datos=datos)

@app.route("/cookie", methods=['GET','POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template("cookie.html",form=reg_user))
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.Username.data
        password = reg_user.Password.data
        datos = user+'@'+password
        succes_message = 'Hola {}'.format(user)
        response.set_cookie('datos_usuario',datos)
        flash(succes_message)
    return response


@app.route("/traducir", methods=['GET','POST'])
def traducir():
    req_in = traductor.traducirIn(request.form)
    req_out = traductor.traducirOut(request.form)
    datos = list()
    pal2 = ''
    # if request.method == 'POST' and req_in.validate():
    if request.method == 'POST':
        if req_out.envio.data == 'tra' and req_out.validate():
            palabra = ''
            for d in req_out.pal.data:
                palabra += d.lower()

            e=open('traductor_esp.txt','r')
            i=open('traductor_ing.txt','r')
            dicionarioE = e.readlines()
            dicionarioI = i.readlines()

            if req_out.idioma.data == 'esp':
                
                for item in dicionarioE:
                    if palabra == item.replace('\n',''):
                        pal2 = dicionarioI[dicionarioE.index(item)].replace('\n','')
            else:
                for item in dicionarioI:
                    if palabra == item.replace('\n',''):
                        pal2 = dicionarioE[dicionarioI.index(item)].replace('\n','')
                        
            e.close()
            i.close()
            datos.append('La palabra traducida fue: "'+palabra+'"')

        # if request.form.get('envio') == 'tra':
            # datos.append(request.form.get('palabra'))
            # datos.append(request.form.get('idioma'))

        if req_in.envio.data == 'gua' and req_in.validate():
            esp = ''
            ing = ''
            for d in req_in.esp.data:
                esp += d.lower()
            for d in req_in.ing.data:
                ing += d.lower()
            datos.append('Palabra guardada (esp) '+esp)
            datos.append('Palabra guardada (ing) '+ing)
            e=open('traductor_esp.txt','a')
            i=open('traductor_ing.txt','a')
            e.write(esp+'\n')
            i.write(ing+'\n')
            e.close()
            i.close()

    return render_template("traductor.html",formIn=req_in,formOut=req_out, datos=datos,pal2 = pal2)

@app.route("/CajasDinamicas", methods=['GET','POST'])
def CajasDinamicas():
    if request.method == 'POST':
        num0 = int(request.form.get('num0'))
        sumar = 0
        numList = []
        repetidos = []
        repetidos2 = {}
        for x in range(num0):
            n = int(request.form.get('num'+str(x+1)))
            if n in numList:
                repetidos2[n] += 1
            else:
                repetidos2[n] = 1

            numList.append(n)
            repetidos.append(1)
            sumar += n
            
        mayor = max(numList)
        menor = min(numList)




        for n1 in range(len(numList)):
            for n2 in range(len(numList)):
                if numList[n1] == numList[n2] and n1!=n2 and n1<n2:
                    repetidos[n1] += 1

        return render_template("CajasDinamicas2.html",
            s=sumar, p= float("{:.2f}".format(sumar/num0)) , ma=mayor, me=menor, r = repetidos2, numList=numList)
    else:
        return render_template("CajasDinamicas.html")

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
                obj = eval(a.replace('\n',''))

                b1 = obj[0]
                b2 = obj[1]
                b3 = obj[2]
                tol = obj[3]
                
                if b1 == '0': b1 = b1.replace('0','')
                valor = int(b1+b2)*b3
                min = '{:.2f}'.format( valor*(1-(tol/100)) )
                max = '{:.2f}'.format( valor*(1+(tol/100)) )
                if b1 == '': b1 = b1.replace('','0')

                salida.append([int(b1),int(b2),len(str(b3))-1,tol,str(valor),str(max),str(min)])
    return render_template("resistencia.html",c=colores,salida=salida)

if __name__ == '__main__':
    # app.run(debug=True)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
# http://127.0.0.1:5000/Alumnos
# Guion bajo es pa indicar que es pribado el archivo/dato