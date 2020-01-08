dia = int(input('digite com o dia: '))
horas = int(input('digite com as horas: '))
minutos = int(input('digite os minutos: '))
segundos = int(input('digite os segundos: '))


segundosF= (dia*24*60*60) + (horas*60*60) + (minutos*60) + segundos
print ('Numero em segundos é ', segundosF)