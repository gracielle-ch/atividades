minutos=int(input('Minutos: '))
if minutos < 200:
    Tminutos = 0.2
elif minutos <= 400:
    Tminutos= 0.18
elif minutos <= 800:
        Tminutos = 0.15
else:
        Tminutos= 0.08
print("conta a ser paga : R$ %6.2f " % (minutos * Tminutos))
    ### o util do ELIF é que ele nao precisa de identação, igual o if
