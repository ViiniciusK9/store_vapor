from os import error
from user import Cadastro

carrinho = []

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
        [0] - LOGOUT
        ''')
        print(self.linha())

        while True:
            self.op = input('Digite uma opção: ')
            
            if self.op == '1':
                self.ver_produtos()
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

    
    def ver_produtos(self,):

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
                self.comprar(int(self.op), un)
            elif self.op == '99':
                self.ver_carrinho(carrinho)
            elif self.op == '0':
                self.menu_loja()
            else:
                print('Opção não encontrada.')

    def ver_carrinho(self, vetor):
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
        

    def comprar(self, cod, un):
        existe = 0
        registro = []
        for i in carrinho:
            if i[0] == cod:
                i[1] += un
                existe = 1

        if existe == 0:
            registro.append(cod)
            registro.append(un)
            carrinho.append(registro)
