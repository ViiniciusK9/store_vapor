
vetor = [[20, 2], [17, 1]]


def ver_carrinho(vetor):
    produtos = []
    sum = 0
    with open('a_produtos.txt', 'r') as arquivo:
        for l in arquivo:
            produtos.append(l.split(','))
    
    print('='*66)      
    print('|Cód|  |Descrição|                                    |un| |Preço|')
    print('='*66)
        
    for u in vetor:
        for l in produtos:
            if u[0] == int(l[0]):  
                a = l[2].replace('\n', '')
                sum += (u[1] * (float(l[1].replace('R$ ', ''))))
                print(f'  {l[0]:<5}{a:<48}{u[1]}  {l[1]}')
    

    print('='*66)      
    print(f'|Total:                                                 R$ {sum:.2f}|')
    print('='*66)
        



ver_carrinho(vetor)




'''
print('='*66)      
print('|Cód|  |Descrição|                                     |un||Preço|')
print('='*66)
print('='*66)
'''