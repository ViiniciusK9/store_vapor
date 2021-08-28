def verificar_cpf(num_cpf):

    # limpar entrada
    cpf = num_cpf.replace(' ', '').replace('-', '').replace('.', '')

    # verifica se o cpf possui os número nescessarios
    if len(cpf) != 11:
        return False

    # verifica se o cpf não possui digitos identicos
    if cpf == cpf[::-1]:
        return False

    # verifica validade do cpf
    j = 10
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


def verificar_email(email):
    if '@' in email and len(email) > 1:
        return True
    else:
        return False



