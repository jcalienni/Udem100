datos = {'nombre' : 'Pedro','edad': 40, 'peso': 82.5, 'entrenamientos': ['corre','natacion','bicileta']}

print (datos['nombre'])
print (datos['edad'])
print (datos['peso'])
print (datos['entrenamientos'][0:3])

mis_claves = datos.keys()
print (mis_claves)
print (list(mis_claves))
print (sorted(mis_claves))
print ("---------------------")
mis_valores = datos.values()
print (mis_valores)
print (list(mis_valores))
print ("---------------------")
print(datos.get('nombre'))
print(datos.get('entrenamientos'))

datos2 = datos.copy()
print (datos2)
tupla_de_datos = datos2.items()
print(tupla_de_datos)
del datos2['peso'] #elimina peso
print (datos2)
print (datos2.pop('edad')) #elimina edad
print (datos2)
datos2.clear() #vacia el diccionario
print (datos2)
