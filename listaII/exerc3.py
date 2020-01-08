peso = float(input('Peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso*4
    print('%.2f kg (s) excesso e o valor da multa é R$: %.2f' %(excesso,multa) )
else:
    excesso = 0
    peso = 0
    print ('excesso e peso 0 ' )
       