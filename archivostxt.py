# f=open('alumno.txt','r')
    # # alumnos = f.read() #regresa string
    # # print(alumnos)
    # # f.seek(20) #te mueve a la linea del txt, pongo 0 te manda al inicio
    # # alumnos2 = f.read()
    # # print(alumnos)


    # # alumnos2 = f.readlines() #regresa array
    # # print(alumnos2)
    # # # print(alumnos2[0])
    # # for item in alumnos2:
    # #     print(item,end='')


    # # alumnos2 = f.readline() #regresa string linea en donde se encuentre 0=linea 1
    # # print(alumnos2)
# f.close()

# #reemplarar el contenido anterior, si el archivo no existe lo crea
# f=open('alumno2.txt','w')
# f.write('Hola perro')
# f.write('Hola de nuevo')

#si el archivo no existe lo crea, pero no reemplaza
f=open('alumno2.txt','a')
f.write(' - _-')
f.write('\n:3')
