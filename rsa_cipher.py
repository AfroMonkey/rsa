n = int(input("Ingrese 'n'>"))
e = int(input("Ingrese 'e'>"))
c = int(input("Ingrese el dato a cifrar>"))

c **= e
c %= n

print("El dato cifrado es: " + str(c))
