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
        self.criar_montante()
        self.baralho = self.embaralhar()
        self.dividir_cartas()

        x = True
        while x == True:
            self.acoes()
            resultado = self.verificar_soma()
            if resultado:
                print("\n\033[32m"+"JOGADOR MAQUINA VENCEU!"+"\033[0;0m")
                print("CARTAS: {}".format(self.jogador_maquina))
                x = False
            else:
                print("\n\033[1m"+"Maquina jogando...\n"+"\033[0;0m")
                sleep(4)
                self.comprar_carta(2)
                som_comb = self.somar_combinacoes(2)
                if som_comb != False:
                    print("\n\033[32m"+"JOGADOR MAQUINA VENCEU!"+"\033[0;0m")
                    print("CARTAS: {}".format(self.jogador_maquina))
                    print("Descarte: {}".format(som_comb))
                    x = False
                else:
                    self.descartar(2)

    def acoes(self):
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
        for i in range(1, 11):
            if i != 10:
                for g in range(4):
                    self.baralho.append(i)
            else:
                for h in range(16):
                    self.baralho.append(i)
    
    def embaralhar(self):
        return shuffle(self.baralho)
    
    def dividir_cartas(self):        
        for i in range(3):
            self.jogador_humano.append(self.baralho.pop())
            self.jogador_maquina.append(self.baralho.pop())
        
        if sum(self.jogador_humano) == 21 or sum(self.jogador_maquina) == 21:
            self.dividir_cartas
    
    def verificar_soma(self):
        if sum(self.jogador_maquina) == 21:
            return True
        else:
            return False

    def comprar_carta(self, jogador):
        if jogador == 1: #Humano
            self.jogador_humano.append(self.baralho.pop())
        else: #Maquina
            self.jogador_maquina.append(self.baralho.pop())
    
    def pegar_descarte(self, jogador):
        if self.descarte == None:
            return False
        else:
            if jogador == 1: #Humano
                self.jogador_humano.append(self.descarte)
                self.descarte = None
            else: #Maquina
                self.jogador_maquina.append(self.descarte)
                self.descarte = None
            return True
    
    def descartar(self, jogador):
        if jogador == 1: #Humano
            carta = int(input("Carta para descartar: "))
            posicao_carta = self.jogador_humano.index(carta)
            self.jogador_humano.pop(posicao_carta)
        else:
            self.jogador_maquina.pop(randint(0,3))
    
    def bater_jogo(self):
        resultado = self.somar_combinacoes(1)
        if resultado != False:
            print("\n\033[32m"+"JOGADOR HUMANO VENCEU!"+"\033[0;0m")
            print("Cartas: {}".format(self.jogador_humano))
            exit(0)
    
    def somar_combinacoes(self, jogador):
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
"""

1. Criar montante de cartas (baralho)
2. Embaralhar
3. Tirar 3 cartas para cada participante

Jogando...

1. Verificar se o valor das cartas somam 21
    Sim: Bater o jogo (Ganhar e encerrar)
    NAO: continua...
2. Pegar a carta descartada
    SIM: executa o passo 4
    NAO: continua...
3. Comprar uma carta
4. Verificar se o valor das cartas somam 21
    Sim: Bater o jogo (Ganhar e encerrar)
    NAO: continua...
5. Descartar uma carta

"""