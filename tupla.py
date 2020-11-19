tupla = ('a','b','c','d','e')
print(tupla[0])
print(tupla[-1])
print(tupla[1:3])
subtupla = tupla[1:3]
print (subtupla)
subtupla2 = tupla[:3]
print (subtupla2)
supertupla = (tupla,subtupla,subtupla2)
print (supertupla)
print (supertupla[1][0])
print (supertupla[0][-2])
