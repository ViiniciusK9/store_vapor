def verificar_cpf(num_cpf):

    
    cpf = num_cpf.replace(' ', '').replace('-', '').replace('.', '') # limpa entrada.

    if len(cpf) != 11: # verifica se o cpf possui os número nescessarios.
        return False

    if cpf == cpf[::-1]: # verifica se o cpf não possui digitos identicos.
        return False

    j = 10 # verifica validade do cpf.
    k = 11
    sum = 0
    for num in range(len(cpf)-2):
        sum += int(cpf[num]) * j
        j -= 1
    j = sum % 11
    if str(j) in '01':
        j = 0
    else:
        j = 11 - j 
    sum = 0
    for num in range(len(cpf)-1):
        sum += int(cpf[num]) * k
        k -= 1
    k = sum % 11
    if str(k) in '01':
        k = 0
    else:
        k = 11 - k
    if j == int(cpf[9]) and k == int(cpf[10]):
        return True
    else:
        return False


def verificar_email(email): # verifica se o email é valido.
    if '@' in email and len(email) > 5 and ' ' not in email:
        return True
    else:
        return False


def verificar_nome(nome): # verifica se o nome é valido.
    if nome.isalpha():
        return True
    return False

    