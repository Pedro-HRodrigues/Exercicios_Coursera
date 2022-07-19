def menor_nome(lista_nome):
    nomes = []
    for i in lista_nome:
        i = i.strip()
        nomes.append(i)
        
    i = 0
    menor_nome = nomes[0]
    while i < len(nomes):
        if len(menor_nome) > len(nomes[i]):
            menor_nome = nomes[i]
            i += 1
        else:
            i += 1

    return menor_nome.capitalize()
        
                                 
