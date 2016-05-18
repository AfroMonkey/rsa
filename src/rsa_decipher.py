n = int(input("Ingrese 'n'>"))
d = int(input("Ingrese 'd'>"))
c = int(input("Ingrese el dato a descifrar>"))

c **= d
c %= n

print("El dato descifrado es: " + str(c))
