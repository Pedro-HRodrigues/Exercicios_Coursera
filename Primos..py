# essa funçao diz se um numero n é primo ou não 
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

def imprime_primos():
    limite = int(input("Digite o limite maximo : "))
    n = 2
    while n < limite:
        if eprimo(n):
            print(n, end = ", ")
        n = n + 1
    print("Fim!")
