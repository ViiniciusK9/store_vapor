from os import error
from user import Cadastro


class Store:
    def __init__(self):
        self.logo()
        self.menu_inicial()


    def menu_inicial(self):
        print('''
        [1] - CADASTRAR
        [2] - LOGIN
        [0] - SAIR
        ''')
        print(self.linha())

        while True:
            self.op = input('Digite uma opção: ')
            
            if self.op == '1':
                Cadastro()
            elif self.op == '2':
                a = self.logar()
                if a:
                    self.menu_loja()
            elif self.op == '0':
                self.exit()
            else:
                print('Opção não encontrada.')

    def menu_loja(self):
        print('''
        [1] - VER PRODUTOS
        [2] - VER CARRINHO
        [3] - PAGAR CONTA
        [0] - SAIR
        ''')
        print(self.linha())

        while True:
            self.op = input('Digite uma opção: ')
            
            if self.op == '1':
                pass
            elif self.op == '2':
                pass
            elif self.op == '3':
                pass
            elif self.op == '0':
                self.exit()
            else:
                print('Opção não encontrada.')


    def logo(self):
        print(f'''{self.linha()}
    __   __                          
    \ \ / /  __ _   _ __   ___   _ _ 
     \ V /  / _` | | '_ \ / _ \ | '_|
      \_/   \__,_| | .__/ \___/ |_|  
                   |_|               
{self.linha()}''')


    def linha(self):
        return "=="*21


    def exit(self):
        exit()


    def logar(self):
        while True:
            self.cpf = input('Digite seu cpf: ')
            self.senha = input('Digite sua senha: ')
            if self.verificar_usuario(self.cpf, self.senha):
                print('Usuario logado com sucesso.')
                break
            else:
                print('Cpf ou senha invalida.')
        return True
        

    def verificar_usuario(self, cpf, senha):
        r_user = []
        
        with open('user_register.txt','r') as arquivo:
            for l in arquivo:
                r_user.append(l.split(','))

        for user in r_user:
            try:
                if str(user[3].replace('\n', '')) == str(cpf) and str(user[1].replace('\n', '')) == str(senha):
                    return True
            except IndexError:
                pass
        return False    