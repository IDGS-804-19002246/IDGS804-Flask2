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


@app.route('/', methods=['GET', 'POST'])
def root():
  form = ResistenciaForm(request.form)
  if request.method == 'POST' and form.validate():
    banda1 = form.banda1.data
    banda2 = form.banda2.data
    banda3 = form.banda3.data
    tolerancia = form.tolerancia.data

    color_banda1 = Resistencia.colores()[int(banda1)]
    color_banda2 = Resistencia.colores()[int(banda2)]
    color_banda3 = Resistencia.colores()[int(banda3)]
    color_tolerancia = Resistencia.colorTolerancias()[int(tolerancia)]

    clase_banda1 = Resistencia.clases()[int(banda1)]
    clase_banda2 = Resistencia.clases()[int(banda2)]
    clase_banda3 = Resistencia.clases()[int(banda3)]
    clase_tolerancia = Resistencia.clasesTolerancia()[int(tolerancia)]

    banda1 = '' if banda1 == '0' else banda1
    banda3 = Resistencia.multiplicadores()[int(banda3)]
    resultado = f'{banda1}{banda2}{banda3}'
    tolerancia = Resistencia.tolerancias[int(tolerancia)].get('valor')
    maximo = float(resultado) * float(tolerancia)
    minimo = round(float(resultado) / float(tolerancia), 2)
    # print(f'resultado: {resultado}, maximo: {maximo}, minimo: {minimo}')

    resp = make_response(redirect(url_for('root')))
    resp.set_cookie('color_banda1', color_banda1)
    resp.set_cookie('color_banda2', color_banda2)
    resp.set_cookie('color_banda3', color_banda3)
    resp.set_cookie('color_tolerancia', color_tolerancia)

    resp.set_cookie('clase_banda1', clase_banda1)
    resp.set_cookie('clase_banda2', clase_banda2)
    resp.set_cookie('clase_banda3', clase_banda3)
    resp.set_cookie('clase_tolerancia', clase_tolerancia)
    resp.set_cookie('resultado', resultado)
    resp.set_cookie('minimo', str(minimo))
    resp.set_cookie('maximo', str(maximo))

    
    return resp
  return view('resistencias.j2',
              form=form,
              colores = Resistencia.colores(),
              valores = Resistencia.valores(),
              tolerancias = Resistencia.colorTolerancias()
              )






if __name__ == '__main__':
    # app.run(debug=True)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
# http://127.0.0.1:5000/Alumnos
# Guion bajo es pa indicar que es pribado el archivo/dato