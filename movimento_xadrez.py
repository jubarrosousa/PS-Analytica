### terceira atividade de programação P2 ##################
#### movimentação do cavalo no xadrez #####################

### Por Juliana Barros ###

class Erro (Exception):
    #Classe base para outras exceções
    pass

class FormatoInvalido(Erro):
    #Erro para quando o formato da entrada é inadequado
    pass

def possiveis_posicoes (pos1):
    possiveis_posicoes = []
    letra = pos1[0]
    numero = pos1[1]

    # todos os possiveis acrescimos nas linhas e colunas que levam as posições validas
    list = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [-1,2],[ 1,-2], [-1,-2]]
    for item in list:
        #como a coluna é determinada por uma letra, mudamos o codigo ascii da letra
        letraAux = chr(ord(letra)+ item[0]) 
        numeroAux1 = numero + item[1]

        # para não selecionar uma posição que não existe no tabuleiro
        if numeroAux1 < 9 and 'A' <= letraAux < 'I':    
            possiveis_posicoes.append(letraAux + str(numeroAux1))

    return possiveis_posicoes
        

def main():
    print("Entre com a posição inicial e final do cavalo: ")

    FINAL = False
    while FINAL == False:
                                    
        x = input()
        
        # o programa não é sensível a letras maiúsculas e minúsculas
        if (x.upper() == 'F' ):
            FINAL = True
            
        else:
            try:
                [pos1, pos2] = x.split()
                num1 = int(pos1[1])
                num2 = int(pos2[1])
                letra1 = pos1[0].upper()
                letra2 = pos2[0].upper()

                if len(pos1) == 2 and len(pos2) == 2:

                    if 0 < num1 < 9 and 'A' <= letra1 < 'I' and 0 < num2 < 9 and 'A' <= letra2 < 'I':
                        posicoes = possiveis_posicoes([letra1, num1])

                        if (letra2+ str(num2)) in posicoes:
                            print('VÁLIDO') 
                        else:
                            print("INVÁLIDO")

            # se houver erro em qualquer uma das funções acima, levantamos um erro 
                    else:
                        raise FormatoInvalido
                else:
                    raise FormatoInvalido    

            
            except:
                print("INVÁLIDO")

    print("FIM")

main()