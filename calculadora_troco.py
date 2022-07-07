### terceira atividade de programação P2 ##################
############ calculadora de troco #########################

def conversao_quantia (quantia):

    valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    total =[]

#'total' armazena a quantidade de notas e moedas das quantias em 'valores' na mesma ordem    
    for item in valores:
        total.append(quantia//item)
        quantia = round(quantia % item, 2)  
        #necessário arredondar devido a forma que o pc faz operações aritméticas com float

    return total

def printar_resposta (total):
        
    notas = ['100.00', '50.00', '20.00', '10.00', '5.00', '2.00']  
    moedas = ['1,00', '0.50', '0.25', '0.10', '0.05', '0.01']

    print ("\nNOTAS:\n")

    for cedula in range (0, len(notas)):
        print (f"{total[cedula]} nota(s) de R$ {notas[cedula]}")
    
    print ("\nMOEDAS:\n")

    cedula += 1
    
    for moeda in range (0, len(moedas)):
        print (f"{total[cedula + moeda]} moeda(s) de R$ {moedas[moeda]}")

class Erro (Exception):
    #Classe base para outras exceções
    pass

class FormatoErrado(Erro):
    #Erro para quando o formato da entrada é inadequado
    pass

def main ():

    dinheiro = input ("Entre com a quantia: ")
    try:
        [reais, centavos] = dinheiro.split(".")

        reais = int (reais)

        if len(centavos) == 2 and reais >= 0:            
            centavos = int (centavos)
            total = conversao_quantia(reais + 0.01 * centavos)
            printar_resposta(total)
        
        else:
            raise FormatoErrado
        
    except:
        print ("Erro: Formato da entrada inválido")
        print ("Entre com um valor positivo com duas casas decimais: 0.00")

main ()