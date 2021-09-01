from os import error
from user import Cadastro

carrinho = []
produtos = []
class Store:
    def __init__(self):
        self.i_produtos()
        self.logo()
        self.menu_inicial()


    def i_produtos(self):
        with open('a_produtos.txt', 'r') as arquivo:
            for l in arquivo:
                x = l.split(',')
                x[2] = x[2].replace('\n', '')
                x[1] = float(x[1].replace('R$ ', ''))
                produtos.append(x)
        

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
        [0] - LOGOUT
        ''')
        print(self.linha())

        while True:
            self.op = input('Digite uma opção: ')
            
            if self.op == '1':
                self.ver_produtos(produtos)
            elif self.op == '2':
                pass
            elif self.op == '3':
                pass
            elif self.op == '0':
                self.menu_inicial()
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
        
        with open('a_user_register.txt','r') as arquivo:
            for l in arquivo:
                r_user.append(l.split(','))

        for user in r_user:
            try:
                if str(user[3].replace('\n', '')) == str(cpf) and str(user[1].replace('\n', '')) == str(senha):
                    return True
            except IndexError:
                pass
        return False

    
    def ver_produtos(self, produtos):
        
        print('='*66)      
        print('|Cód|  |Descrição|                                         |Preço|')
        print('='*66)

        for produto in produtos:
            print(f'  {produto[0]:<5}{produto[2]:<50}R$ {produto[1]}')
        
        print('='*66)

        print('''
        [CÓD 1-20] - COLOCAR NO CARRINHO
        [99] - VER CARRINHO
        [0] - VOLTAR
        ''')
        print(self.linha())

        while True:
            self.op = input('Digite uma opção: ')
            
            if 1 <= int(self.op) <= 20 :
                un = int(input(f'[{self.op}] - QUANTIDADE DE UNIDADES: '))
                self.colocar_carrinho(self.op, un, produtos)
            elif self.op == '99':
                pass
            elif self.op == '0':
                self.menu_loja()
            else:
                print('Opção não encontrada.')


    def colocar_carrinho(self, cod, un, produtos):
        
        for produto in produtos:
            if produto[0] == cod:
                
        pass