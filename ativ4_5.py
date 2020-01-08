salario = float(input('digite o salario: ' ))
porcent = int(input('digite a porcentagem: ' ))
Vaumento= salario*porcent/100
print('O valor do aumento é: ', Vaumento)
Nsalario= salario + Vaumento
print('O valor do novo salario é: ', Nsalario)

###########################################################5

Pmercadoria = float(input('digite o preco da mercadoria: ' ))
porcentD = float(input('digite o porcentual de desconto: ' ))
Vdesconto= Pmercadoria*porcentD/100
print('O valor do desconto é: ', Vdesconto)
Ppagar= Pmercadoria - Vdesconto
print('O valor do novo salario é: ', Ppagar)