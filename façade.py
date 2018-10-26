
class Jogar:
    def __init__(self):
        print("O que é preciso pra jogar RPG?")
    def Organicao(self):
        print("Você como jogador deve escolher uma raça e uma classe para o seu personagem, por exemplo:\n")
        self.clas=Classes()
        self.clas.babaro()
        self.clas.bardo()
        self.clas.clerigo()
        self.clas.druida()
#subclasse
class Classes:
    def __init__(self):kk
    
        print ('Algumas Classes:')
    def babaro(self):
        print('Bárbaro: Você primeiro bate e depois pergunta o que tá acontencendo. Um Bárbaro é uma fonte bruta de poder físico,um ignorante intelectual, nascido apenas para matar e pilhar.')
    def bardo(self):
        print("Bardo: Se inspira e elabora magias com seu alaúde mágico, flauta ou voz. Acima de tudo um estudioso das ondas sonoras. E sabe o poder que elas tem.Também pode ser um pé no saco do grupo!")
    def clerigo(self):
        print("Clérigo: Você é a mão dos deuses sagrados. Além de curar e proteger seu time, também arrebata de vez os mortos-vivos.Nada de demoníaco e maligno passará por você.")
    def druida(self):
        print("Druida: Uma classe de servos da natureza, a reverenciam acima de tudo, adquirindoseus poderes mágicos através dela ou de uma divindade.")
class RPG:
    def __init__(self):
        print("O que é um RPG de mesa ?")
    def como_jogar(self):
        print("É um jogo de interpretação de personagens.O mestre narra uma historia,descreve cenários e seus acontecimentos.Os jogadores(2-6),falam o que gostariam de fazer.dessa maneira o jogo se desenrola dentro da imaginação de cada um!\n")
        self.rpg=Jogar()
        self.rpg.Organicao()

vs=RPG()
vs.como_jogar()

