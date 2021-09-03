novo_saldo = '1000\n'

conta = []

with open('a_user_register.txt','r') as arquivo:
    for linha in arquivo:
        a = linha.split(',')
        if len(a) < 5:
            continue
        if a[3] == '15157477007':
            a[4] = novo_saldo
            print('batatinha')
        conta.append(a)

with open('a_user_register.txt','w') as arquivo:
    for c in conta:
        arquivo.write(str(f'{c[0]},{c[1]},{c[2]},{c[3]},{c[4]}')+'\n')
