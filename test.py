nombre = input ("Introduzca su nombre:")
edad = int(input ("Introduzca su edad:"))
print (nombre)
print (edad)

#Mayor de edad?
if edad>=18:
    print ("Es mayor de edad.")
else:
    print ("Es menor de edad.")
        
if nombre == "Jorge":
    print ("UUsted va a la sala 1")
elif nombre=="Pedro":
    print ("Usted va a la sala 2")
elif nombre=="Paola":
    print ("Usted va a la sala 3")
elif nombre=="Romina":
    print ("Usted va a la sala 4")
else:
    print ("Usted va a la sala 5")
