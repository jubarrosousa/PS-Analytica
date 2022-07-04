### primeira atividade de programação P2 ##################
### calculadora de ângulo entre os ponteiros do relogio ###

### Por Juliana Barros ###

def calcAng (hora, minutos):
    if hora > 12:
        hora -= 12
    
    # angulo em relacao ao 12 do relogio dos ponteiros de horas e minutos
    angHora = hora * 30
    angMin = minutos * 6

    angTotal = abs (angHora - angMin)

    # Calculando o seu replemento, e escolhendo ele caso seja menor
    angTotal2 = 360 - angTotal

    return (min (angTotal, angTotal2))

class Erro (Exception):
    #Classe base para outras exceções
    pass

class FormatoErrado(Erro):
    #Erro para quando o formato da entrada é inadequado
    pass

def main ():

    horario = input ("Entre com o horario: ")

    if horario.upper() == "F":
        return (print ("fim do programa"))

    try:
        [hora, minutos] = horario.split(":")

        if len (hora) == 2 and len(minutos) == 2:
            hora = int(hora)
            minutos = int(minutos)
            
            if (hora < 25) and (minutos < 60):
                angulo = calcAng (hora, minutos)
                print ("O ângulo entre os ponteiros é: ", angulo)
            else:
                raise FormatoErrado

        else:
            raise FormatoErrado
    
    except:
        print("Erro: Formato do horário inválido")
        print("Entre com uma entrada no formato- hh:mm")


main ()