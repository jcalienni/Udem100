class matematica:
    def sumar(self,nro1,nro2):
        try:
            if nro1<0:
                raise Exception("los numeros tienen que ser positivos")
        except:
            return "señor, no pede poner un numero menor a cero en el primer"
        else:
            return nro1+nro2

    def restar(self, nro1, nro2):
        return nro1-nro2

    def multiplicar(self,nro1, nro2):
        try:
            if not type(nro1) is int:
                raise TypeError("only integers")
        except TypeError:
            return("No puedo multiplicar")
        else:
            return nro1*nro2

    def dividir(self,nro1,nro2):
        n1 = nro1 - 5
        n2 = nro2 - 3
        n3 = 0.0
        try:
            n3 = n1/n2
        except ZeroDivisionError:
            return "No puedo dividir por 0"
        except TypeError:
            return "Debe ingresar numeros"
        else:
            return n3
        finally:
            print ("Hola, quiero dividir")


class mapas:
    def get_item(self,mapa,item):
        try:
            return mapa[item]
        except KeyError:
            return ('No existe la Key')
mi_calculadora = matematica()

print (mi_calculadora.dividir(-1, 5))
print (mi_calculadora.sumar(-1, 5))
print (mi_calculadora.multiplicar(3,2.2))

mi_mapa = mapas()
print (mi_mapa.get_item({'id':0, 'nombre':'pablo'},'apell'))

# mi_mapa = {'id':0, 'nombre':'pablo'}
# print (mi_mapa['id'])
# print(mi_mapa['apellido'])