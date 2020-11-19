helados = ["chocolate","limon","dulce de leche","vainilla","frutilla"]

for helado in helados:
    if helado == "vainilla":
        print ("No me gusta el elado de vainilla")
        continue #Continue con la proxima iteracion, el break corta el for.
    print ("Quiero un helado de "+helado)
else: #Solo pasa por el Else si no se corta el for.
    print ("Me comi todos los helados")
print ("Fin del pedido")
