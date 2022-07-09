### terceira atividade de programação P2 ##################
############ frequencia de numeros ########################

### Por Juliana Barros ###

def frequencia_lista(lista_numeros):

    frequencia_numeros = [] # lista com a frequencia de cada numero

    aux = 0
    freq_item = 1

    while aux < len (lista_numeros):  # aux passa por todos os valores da lista de numeros

        freq_item = 1 #frequencia de cada item vai ser sempre 1 no minimo

        # se o numero seguinte for igual ao anterior, a frequencia do numero aumenta em 1
        while (aux+1 < len(lista_numeros)) and (lista_numeros[aux] == lista_numeros[aux + 1]):
            freq_item += 1
            aux +=1
            
        frequencia_numeros.append(freq_item)
        aux += 1

    return frequencia_numeros

def printar_resultado(frequencia, lista_numeros):

    aux = 0 # variavel que passa pelos diferentes numeros da lista, pulando os que já apareceram

    for i in range (0, len(frequencia)):    # i é a quantidade de números diferentes que apareceram

        if frequencia[i] == 1:
            plural = ''
        else:
            plural = 'es'

        if i==0:
            print (f"O número {lista_numeros[i]} apareceu {frequencia[i]} vez{plural}")
            aux += frequencia[i]
        else:
            print (f"O número {lista_numeros[aux]} apareceu {frequencia[i]} vez{plural}")
            aux += frequencia[i]

    print("Fim")         


def main ():

    lista_numeros = []
    
    print("Entre com números inteiros: ")

    FINAL = False
    while FINAL == False:
        x = input()
        
        if (x.upper() == 'F' ):
            FINAL = True
            lista_numeros = sorted(lista_numeros)
            frequencia_numeros = frequencia_lista(lista_numeros)
            printar_resultado(frequencia_numeros, lista_numeros)

        else:
            try:
                x = int(x)
                lista_numeros.append(x)

            except:
                pass

main()