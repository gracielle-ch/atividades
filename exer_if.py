vel = int(input('Velocodidade do carro: '))
if vel > 110:
    print('seu carro foi multado')
    multa = (vel-110)*5
    print('valor da multa: R$ %5.2f ' %multa)


    ################################
    minutos = int(input('Minutos: '))
    if minutos < 200:
        Tminutos = minutos*0.2
        print(Tminutos)
    else:
        if  minutos <= 400:
            Tminutos= minutos*0.18
            print (Tminutos)

        else:
            Tminutos= minutos*0.15
            print (Tminutos)