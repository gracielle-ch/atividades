i = 1
fat = 1
n = int(input("Digite o numero: "))
while i <= n:
    fat = fat * i
    i = i + 1
print("Fat(%d) = %d" %(n,fat))