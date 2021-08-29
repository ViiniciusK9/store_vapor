

produtos = []

with open('a_produtos.txt', 'r') as arquivo:
    for l in arquivo:
        produtos.append(l.split(','))
print('='*66)      
print('|Cód|  |Descrição|                                         |Preço|')
print('='*66)
for l in produtos:
    a = l[2].replace('\n', '')
    print(f'  {l[0]:<5}{a:<50}{l[1]}')
print('='*66)

