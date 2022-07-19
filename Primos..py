import time 
def eprimo(n):
    x = 2
    y = 1
    while y != 0:
        y = n % x
        x += 1
    if x - 1 == n:
        primo = True
    else:
        primo = False
    return primo

inicio = time.time()
limite = int(input("Digite o limite maximo : "))
n = 2
while n < limite:
    if eprimo(n):
        print(n, end = ", ")
    n = n + 1
print("Fim!")
fim = time.time()
tempo =  fim - inicio
print ("demorou", tempo, "segundos")

235 / 60 