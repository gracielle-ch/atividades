l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3 :"))
if l1 < l2+l3 and l1 > abs(l2 - l3) and l2 < l1+l3 and l1 > abs(l1 - l3) and l3 < l1+l2 and l1 > abs(l1 - l2):
    print("É um triangulo")
else:
    print("Os números nao formam um triangulo")



