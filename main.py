from sklearn.utils import shuffle
from random import randint
from time import sleep

class VinteUm:

    def __init__(self):
        self.baralho = []
        self.descarte = None
        self.jogador_humano = []
        self.jogador_maquina = []
    
    def inicio(self):
        self.criar_montante() #criar as cartas do baralho
        self.baralho = shuffle(self.baralho) #EMBARALHAR cartas
        self.dividir_cartas() #tirar do baralho 3 cartas para cada um

        x = True
        while x == True:
            self.acoes() #dar opcoes para o jogador humano
            #Jogadas do jogador Maquina
            print("\n\033[1m"+"Maquina jogando...\n"+"\033[0;0m")
            sleep(4)
            self.comprar_carta(2)
            som_comb = self.somar_combinacoes(2) #somar as cartas apos a compra
            #se tiver dados 21
            if som_comb != False:
                print("\n\033[32m"+"JOGADOR MAQUINA VENCEU!"+"\033[0;0m")
                print("CARTAS: {}".format(self.jogador_maquina))
                print("Descarte: {}".format(som_comb))
                x = False
            else:
                self.descartar(2)

    def acoes(self):
        """Dar as opcoes para o usuario humano."""

        print("Suas cartas: {}".format(self.jogador_humano))
        if self.descarte != None:
            print("Carta descartada: {}".format(self.descarte))

        print("\n1) Comprar carta\n2) Pegar descarte\n3) Descartar\n4) Bater jogo")
        opcao = int(input("> "))

        if opcao == 1:
            self.comprar_carta(1)
            self.acoes()
        if opcao == 2:
            self.pegar_descarte()
            self.acoes()
        if opcao == 3:
            self.descartar(1)
        if opcao == 4:
            self.bater_jogo()
            self.acoes()

    def criar_montante(self):
        """Criar o conjunto de cartas do baralho."""

        #insere 4 cartas de 1 a 9
        for i in range(1, 10):
            for g in range(4):
                self.baralho.append(i)
        #insere 16 cartas do valor 10
        for i in range(1, 16):
            self.baralho.append(10)
    
    def dividir_cartas(self):
        """Retirar 3 cartas do baralho para cada jogador."""
        copia_baralho = self.baralho  #copia por causa do POP
        for i in range(3):
            self.jogador_humano.append(self.baralho.pop())
            self.jogador_maquina.append(self.baralho.pop())
        
        #Para que  o jogo nunca comece com as cartas ja valendo 21
        #se dividir as cartas e for 21, dividira novamente
        if sum(self.jogador_humano) == 21 or sum(self.jogador_maquina) == 21:
            self.jogador_humano = self.jogador_maquina = []
            self.baralho = copia_baralho
            self.dividir_cartas()

    def comprar_carta(self, jogador):
        """Retira +1 carta do baralho para um dos jogadores."""

        if jogador == 1: #Humano
            self.jogador_humano.append(self.baralho.pop())
        else: #Maquina
            self.jogador_maquina.append(self.baralho.pop())
    
    def pegar_descarte(self):
        """Pega a carta que está no descarte para o ojogador humano."""

        if self.descarte == None:
            return False
        else:
            self.jogador_humano.append(self.descarte)
            self.descarte = None

            return True
    
    def descartar(self, jogador):
        """Retirar uma carta de um dos jogadores."""

        if jogador == 1: #Humano
            carta = int(input("Carta para descartar: "))
            try:
                posicao_carta = self.jogador_humano.index(carta)
                self.descarte = self.jogador_humano.pop(posicao_carta)
            except:
                print("\nNao existe essa carta com voce!\n")
                self.descartar(jogador)
        else:
            self.descarte = self.jogador_maquina.pop(randint(0,3))
    
    def bater_jogo(self):
        resultado = self.somar_combinacoes(1)
        if resultado != False:
            print("\n\033[32m"+"JOGADOR HUMANO VENCEU!"+"\033[0;0m")
            print("Cartas: {}".format(self.jogador_humano))
            exit(0)
    
    def somar_combinacoes(self, jogador):
        """Com as 4 cartas, a funcao tenta se de alguma forma e possivel dar 21 usando 3 cartas."""
        if jogador == 1:
            for i in self.jogador_humano:
                if (sum(self.jogador_humano) - i) == 21:
                    posix = self.jogador_humano.index(i)
                    self.jogador_humano.pop(posix)
                    return i
        else:
            for i in self.jogador_maquina:
                if (sum(self.jogador_maquina) - i) == 21:
                    posix = self.jogador_maquina.index(i)
                    self.jogador_maquina.pop(posix)
                    return i
        
        return False

jogo = VinteUm()
jogo.inicio()