def get_primes(n):
    primes = list(range(2, n))
    for number in primes:
        for mult in list(range(number*number, n, number + number):
            primes.remove(mult)
    return primes

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def inverse(e, n):
    i = 1
    while (i * e) % n != 1:
        i += 1
    return i

# Main #
primes = get_primes(1000)

if input("Ver una lista de primos? (y/n)>") == "y":
    print(primes)

p = 0
while not p in primes:
    p = int(input("Ingrese un numero primo 'p'>"))

q = 0
while not q in primes or p == q:
    q = int(input("Ingrese un numero primo 'q'>"))

n = p * q

phi_n = (p - 1) * (q - 1)

public_keys = [number for number in range(2, phi_n) if gcd(number, phi_n) == 1]

if input("Ver una lista de coprimos de " + str(phi_n) + "? (y/n)>") == "y":
    print(public_keys)

e = 0
while not e in public_keys:
    e = int(input("Ingrese un numero coprimo de " + str(phi_n) + " 'e'>"))

d = inverse(e, phi_n)

print("Clave publica: n=" + str(n) + ", e=" + str(e))
print("Clave privada: n=" + str(n) + ", d=" + str(d))
