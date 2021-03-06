from os import error
import verificar


class User: # estrutura para cadastrar um novo usuário. 
    nome = None
    email = None
    senha = None
    conf_senha = None
    cpf = None
    saldo = None

class Cadastro: # classe para criar novos usuario, aqui sera soliciado e verificado todas as informações do usuário.
    def __init__(self) -> None:
        self.novo_usuario = User()
        self.novo_usuario.saldo = 1000
        while True:
            a = self.novo_usuario.nome = input('Digite seu nome: ')
            if verificar.verificar_nome(a):
                break
            else:
                print('Digite um nome valido!')
                
        while True:
            a = self.novo_usuario.email = input('Digite seu email: ')
            if verificar.verificar_email(a) and self.ler_email_existente(a):
                break
            elif not self.ler_email_existente(a):
                print('Email já cadastrado.')
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
            elif not self.ler_cpf_existente(self.novo_usuario.cpf):
                print('Cpf já cadastrado.')
            else:
                print('Digite um cpf valido!')
        print('Cadastro realizado com sucesso.')
        self.registrar_usuario()


    def registrar_usuario(self): # salvar informações solicitadas do novo usuário.
        with open('a_user_register.txt','a') as arquivo:
            arquivo.write(str(f'{self.novo_usuario.nome},{self.novo_usuario.senha},{self.novo_usuario.email},{self.novo_usuario.cpf.replace("-", "").replace(".", "").replace(" ", "")},{self.novo_usuario.saldo}')+'\n')
            
    
    def ler_cpf_existente(self, cpf): # função para verificar se o cpf informado ja está cadastrado.
        r_user = []
        
        with open('a_user_register.txt','r') as arquivo:
            for l in arquivo:
                r_user.append(l.split(','))

        for user in r_user:
            try:
                if str(user[3].replace('\n', '')) == str(cpf):
                    return False
            except IndexError:
                pass
        return True     
    

    def ler_email_existente(self, email): # função para verificar se o email informado ja está cadastrado.
        r_user = []
        
        with open('a_user_register.txt','r') as arquivo:
            for l in arquivo:
                r_user.append(l.split(','))

        for user in r_user:
            try:
                if str(user[2].replace('\n', '')) == str(email):
                    return False
            except IndexError:
                pass
        return True    