area = int(input("Digite o tamanho da área a ser pintada: "))
totalLT =  area/3
if totalLT <= 18:
   print("Você precisará de 1 lata de tinta que custa RS80,00")
else:
    latas = int(totalLT/18)+1
    preco = latas*80
    print("Voce precisará de %d " % latas , "latas e o preco sera R$ %.2f "  %preco )

'''
1 - 3
x - 900
3x = 900
python3 exerc7.py 
Digite o tamanho da área a ser pintada: 900
300
Voce precisará de 16  latas e o preco sera 1333.33
'''
'''
area = int(input("Digite o tamanho da área a ser pintada: "))
if area % 54 != 0:
    latas= int(area/54) +1
else:
    latas = area/54
valor = latas * 80 

print('%d latas e preco sera %.2f ' %(latas,valor))
'''