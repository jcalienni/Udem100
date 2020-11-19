archivo = open('mi_archivo.txt','w')
archivo.write('Hola mundo!\n')
archivo.write('Tutorial de Python 3\n')
dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
archivo.writelines(dias)
for i in dias:
    archivo.write(i+'\n')
archivo.close()
#---------------------------------------
archivo = open('mi_archivo.txt','r')

#print(archivo.read(5))
#print(archivo.read(3))
#print(archivo.read())

while True:
    mi_linea = archivo.readline()
    if not mi_linea:
        break
    print(mi_linea)

archivo.close()
