import random, sys, os

class Gems: 
    def  __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

class Mine:
    def __init__ (self):
        self.gem = []

    def add_gem(self, gem):
        self.gem.append(gem)

    def show_gems(self):
        return self.gem

    def pick_gem(self):
        return self.gem.pop(0)
    
    def shuffle(self):
        for i in range(len(self.gem) -1,0,-1):
            r = random.randint(0,i)
            self.gem[i], self.gem[r] = self.gem[r], self.gem[i]
    
    def remove_gem(self, Gems):
        self.pick_gem()
        qtd_atual = Gems.quantidade = Gems.quantidade - 1
        return qtd_atual

    def show_quanties(self, Gems):
        return Gems.quantidade

class Player:

    def __init__(self, nome):
        self.nome = nome
        self.inventario = []
        self.dia = 1

    def minerar(self, Mine):
        self.inventario.append(Mine.pick_gem())

    def encerrar_dia(self):
        self.dia += 1

    def pontuacao(self, Gems):
        return sum(Gems.pontos(self.inventario))

    def discard(self):
        try:
            return self.inventario.pop(0)
        except:
            print ("ERRO DISCARD")

    def showInventory(self):
        return self.inventario

    def removeInventory(self, Mina):
        for i in range(len(self.inventario)):
            Mina.add_gem(self.inventario.pop(0))
        # self.inventario.clear()

class Game:
    player = Player("Alvaro")
    mina = Mine()
    instavel = Gems("Instável" , 0, 18)
    branca   = Gems("Quartzo"  , 1, 15)
    roxa     = Gems("Ametista" , 2, 12)
    verde    = Gems("Esmeralda", 3, 10)
    azul     = Gems("Safira"   , 4, 7)
    vermelha = Gems("Ruby"     , 6, 4)
    amarela  = Gems("Ambar"    , 8, 2)
    
    def initialize(self):

        for i in range(0, self.instavel.quantidade):
            self.mina.add_gem(self.instavel.nome)
        for i in range(0, self.branca.quantidade):
            self.mina.add_gem(self.branca.nome)
        for i in range(0, self.roxa.quantidade):
            self.mina.add_gem(self.roxa.nome)
        for i in range(0, self.verde.quantidade):
            self.mina.add_gem(self.verde.nome)
        for i in range(0, self.azul.quantidade):
            self.mina.add_gem(self.azul.nome)
        for i in range(0, self.vermelha.quantidade):
            self.mina.add_gem(self.vermelha.nome)
        for i in range(0, self.amarela.quantidade):
            self.mina.add_gem(self.amarela.nome)

        self.mina.shuffle()
        self.opcoes()

    def opcoes(self):
        opcao = 1
        while (opcao != 3):
            opcao = int(input("O que você deseja fazer?\n(0) - Minerar \n(1) - Encerrar o dia\n(3) - Sair\n\n"))
            if (opcao == 0):
                self.player.minerar(self.mina)
                # print ("\nInventário: {}".format(self.player.showInventory()))
                self.count_duplicates(self.player.showInventory())
            elif (opcao == 1):
                self.player.encerrar_dia()
        else:
            sys.exit()
            
    def count_duplicates (self,list): 
        
        flag = False
    
        # To append Duplicate elements in list 
        coll_list = []   
        coll_cnt = 0
        for t in list: 
            
            # To check if Duplicate exist 
            if t in coll_list:   
                flag = True
                continue
            
            else: 
                coll_cnt = 0
                for b in list: 
                    if b[0] == t[0] and b[1] == t[1]: 
                        coll_cnt = coll_cnt + 1
                
                # To print count if Duplicate of element exist 
                # if(coll_cnt > 1):  
                    # print(t, "-", coll_cnt) 
                coll_list.append(t) 
                if (t == 'Instável' and coll_cnt == 2):
                    os.system('cls')
                    self.player.removeInventory(self.mina)
                    print("\n\n Lista: ", self.player.showInventory())

        # if flag == False: 
        #     print("No Duplicates") 
    
g = Game()
g.initialize()