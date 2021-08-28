# verificando validação do cpf

j = 10
k = 11
sum = 0
a = '11144477735'
for num in range(len(a)-2):
    #print(a[num])
    sum += int(a[num]) * j
    j -= 1
j = sum % 11
if str(j) in '01':
    j = 0
else:
    j = 11 - j 
print(j)

