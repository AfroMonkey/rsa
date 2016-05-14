primes = list(range(2, 1000))
for number in primes:
    for mult in primes:
        if mult != number and mult % number == 0:
            primes.remove(mult)

while True:
    p = int(input("Ingrese un numero primo 'p'>"))
    if p in primes:
        break

while True:
    q = int(input("Ingrese un numero primo 'q'>"))
    if q in primes:
        break

n = p * q
phin = (p - 1) * (q - 1)

cop = list(range(2, phin))
for number in cop:
    if n != number and n % number == 0:
        cop.remove(number)

while True:
    e = int(input("Ingrese un numero coprimo de " + str(n) + " y menor que " + str(phin) + " 'e'>"))
    if e in cop:
        break

for i in range(1, phin):
    if (e * i) % phin == 1:
        d = i
        break;

print("Clave publica: " + str(n) + ", " + str(e))
print("Clave privada: " + str(n) + ", " + str(d))
