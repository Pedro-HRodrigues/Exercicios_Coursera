def acha_minimo(lista):
    minimo = True
    i = 0
    while minimo:
        if min(lista) == lista[i]: 
            return i
            minimo = False
        else:
            i = i + 1
    
        
        
