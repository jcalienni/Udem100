helados = ['Chocolate','Dulce de leche','Limon','Vainilla']
print (helados.count('Crema'))
helados.append('Crema')
print(helados)
helados.insert(2,'Granizado')
print(helados)
print(helados.count('Crema'))
helados.remove('Dulce de leche')
print(helados)
print (helados.index('Limon'))
helados.reverse()
print(helados)
print("*----------------------------------------------*")
helados.sort()
print(helados)
print(helados.pop()) #Borra el ulitmo item del arreglo
print(helados)
print(helados.pop(1)) #Borra el item en pos 1 del arreglo
print(helados)
new_helados = helados.copy() #copia en new_helados el arreglo helados
print(new_helados)
helados.clear() #borra los elementos del arreglo helados
print(helados)
print(new_helados)
print(new_helados.index('Granizado',1))#Busca granizado desde el elemento 1
#print(new_helados.index('Granizado',2))#Busca granizado desde el elemento 2
print("*----------------------------------------------*")
crema = ['Chocolate','Dulce de leche','Vainilla']
agua = ['Frutilla','Limon','Naranja']
helados = [crema,agua]
print (helados)
print (helados[0])
print (helados[0][1])
myList = [1,"Manzana",2.15]
print (myList[0])

