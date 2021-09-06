

def meus_dados():
    a = cpf_formatado("15157477007")
    print(f'        Cpf cadastrado: {a}')
 

def cpf_formatado(cpf):
    cpf_f = ''
    c = 0
    for i in cpf:
        cpf_f += i
        c+=1
        if c == 3:
            cpf_f += '.'
        if c == 6:
            cpf_f += '.'
        if c == 9:
            cpf_f += '-'
    return cpf_f

meus_dados()