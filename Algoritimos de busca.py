#Algoritimo de busca sequencial 
def busca_sequencial(lista, x):
    #(list, float) -> bool
    for i in range(len(lista)):
        if lista[i] == x :
            return True
    
    return False
# algoritimo de busca binaria 
def busca(lista, x):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)// 2
        print(meio)
        if lista[meio] == x:  
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio - 1 
            else:
                primeiro = meio + 1 
    return False

# Algoritimo de busca bubble sort 
def  bubble_sort(lista):
    fim = len(lista)
    for i in range (fim - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    return lista 
