ganha = float(input('Quanto voce ganha por hora? '))
horas = int(input('Número de horas trabalhadas no mes: '))
Tsalario = ganha*horas
print('Seu salário bruto é R$ %.2f'  %Tsalario)
ir = Tsalario*11/100
print('Pagou de Imposto de Renda RS : \t %.2f' %ir)
inss = Tsalario*8/100
print('Pagou de INSS RS : \t\t %.2f' %inss)
sind= Tsalario*5/100
print('Pagou de Sindicato RS : \t %.2f'  %sind)
salarioliq= Tsalario-(ir+inss+sind)
print('Sobrou RS : \t\t %.2f'  % salarioliq)
