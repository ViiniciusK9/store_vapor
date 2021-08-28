from os import error
from user import Cadastro

class Store:
    def __init__(self):
        self.logo()
        self.menu()


    def menu(self):
        print('''
        [1] - CADASTRAR
        [2] - LOGIN
        [3] - CONSULTAR CLIENTE 
        [4] - COMPRAR
        [5] - MOSTRAR CARRINHO
        [6] - EFETUAR PAGAMENTO
        [0] - SAIR
        ''')
        print(self.linha())

        while True:
            self.op = input('Digite uma opção: ')
            
            if self.op == '1':
                Cadastro()
            elif self.op == '2':
                pass
            elif self.op == '3':
                pass
            elif self.op == '4':
                pass
            elif self.op == '5':
                pass
            elif self.op == '6':
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