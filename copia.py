    def ver_produtos(self,):

        a_produtos = []

        with open('a_produtos.txt', 'r') as arquivo:
            for l in arquivo:
                a_produtos.append(l.split(','))
        print('='*66)      
        print('|Cód|  |Descrição|                                         |Preço|')
        print('='*66)
        for l in a_produtos:
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
                self.comprar(int(self.op), un, produtos, carrinho)
            elif self.op == '99':
                self.ver_carrinho(carrinho)
            elif self.op == '0':
                self.menu_loja()
            else:
                print('Opção não encontrada.')


    def ver_carrinho(self, vetor):
        cod = []
        for i in vetor:
            if i == list():
                cod.append(i[0])
        a_produtos = []
        sum = 0
        with open('a_produtos.txt', 'r') as arquivo:
            for l in arquivo:
                produtos.append(l.split(','))
        
        print('='*66)      
        print('|Cód|  |Descrição|                                    |un| |Preço|')
        print('='*66)
            
        for i in cod:
            for l in a_produtos:
                if i == int(l[0]):  
                    a = l[2].replace('\n', '')
                    sum += (u[1] * (float(l[1].replace('R$ ', ''))))
                    print(f'  {l[0]:<5}{a:<47}{u[1]}  {l[1]}')
        

        print('='*66)      
        print(f'|Total:  {sum:>56.2f}|')
        print('='*66)
        
        
    def comprar(self, cod, un, prod, carrinho):
        if len(carrinho) == 0:
            carrinho.append(0)
        sum = carrinho[0]
        registro = []
        for l in prod:
            if cod == int(l[0]):  
                sum += (un * l[1])
        if sum > 1000:
            print(f'Você ultrapassou o limite de R$ 1000.00')
            return
        
        existe = 0
        for i in carrinho:
            if i[1] == cod:
                i[2] += un
                existe = 1
                i[0] += sum
        if existe == 0:
            i[0] += sum
            registro.append(cod)
            registro.append(un)
            registro.append(sum)
            carrinho.append(registro)