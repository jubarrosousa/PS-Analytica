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
    angTotal2 = 360 - angTotal
    return (min (angTotal, angTotal2))

def main ():

    horario = input ("Entre com o horario: ")
    print(horario)
    if horario.upper() == "F":
        return (print ("fim do programa"))

    [hora, minutos] = horario.split(":")
    hora = int(hora)
    minutos = int(minutos)
    angulo = calcAng (hora, minutos)
    print (angulo)

main ()