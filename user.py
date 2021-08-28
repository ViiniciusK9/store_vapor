from os import error
import verificar


class User:
    nome = None
    email = None
    senha = None
    conf_senha = None
    cpf = None

class Cadastro:
    def __init__(self) -> None:
        self.novo_usuario = User()
        
        while True:
            a = self.novo_usuario.nome = input('Digite seu nome: ')
            if verificar.verificar_nome(a):
                break
            else:
                print('Digite um nome valido!')
                
        while True:
            a = self.novo_usuario.email = input('Digite seu email: ')
            if verificar.verificar_email(a):
                break
            else:
                print('Digite um email valido!')

        while True:
            self.novo_usuario.senha = input('Digite sua senha: ')

            self.novo_usuario.conf_senha = input('Confirme sua senha: ')
            if self.novo_usuario.senha == self.novo_usuario.conf_senha and len(self.novo_usuario.senha) >= 6:
                break
            else:
                print('Digite e confirme sua senha corretamente!')    

        while True:
            self.novo_usuario.cpf = input('Digite seu cpf: ')
            if verificar.verificar_cpf(self.novo_usuario.cpf) and self.ler_cpf_existente(self.novo_usuario.cpf):
                break
            else:
                print('Digite um cpf valido!')
        
        self.registrar_usuario()


    def registrar_usuario(self):
        with open('user_register.txt','a') as arquivo:
            arquivo.write(str(f'{self.novo_usuario.nome},{self.novo_usuario.senha},{self.novo_usuario.email},{self.novo_usuario.cpf}')+'\n')
            
    '''
    def ler_cpf_existente(self, cpf):
        r_user = []
        
        with open('user_register.txt','r') as arquivo:
            for l in arquivo:
                r_user.append(l.split(','))
        for user in r_user:
            if str(user[3].replace('\n', '')) == str(cpf):
                return False
        return True     
    '''        

    





