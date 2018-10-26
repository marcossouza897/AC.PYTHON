'''
════════════════════════════════════════════════════════════════════════════════
 Instituição   :  Faculdade Impacta Tecnologia
 Curso         :  Análise e Desenvolvimento de Sistemas
 Disciplina    :  Linguagem de Programação 2
 Turma         :  2A (manhã)
 Professor     :  Lucio Nunes de Lira
 Aluno (1)     :  Jose Luis Merma Pinedo
 Aluno (2)     :  
 Aluno (3)     :  
 Matrícula (1) :  1800780
 Matrícula (2) :
 Matrícula (3) : 
 Entrega       :  27/10/2018
════════════════════════════════════════════════════════════════════════════════
 Programa      :  AC8 (Padrões de Projeto)
════════════════════════════════════════════════════════════════════════════════
'''

'''─────────────────────────────────────────────────────────────────────────────
Com base nos arquivo gerados na aula de 24/10/2018, construa um programa que use
um dos padrões de projeto que foram discutidos e implementados.
Obs.: Note que cada equipe já tem o padrão definido nas instruções da AC.
─────────────────────────────────────────────────────────────────────────────'''
class Jogar:
    def __init__(self):
        print("O que é preciso pra jogar RPG?")
    def Organicao(self):
        print("Você como jogador deve escolher uma raça e uma classe para o seu personagem.\n")
        self.clas=Classes()
        self.clas.babaro()
        self.clas.bardo()
        self.clas.clerigo()
        self.clas.druida()
        self.clas.Feiticeiro()
        self.clas.Guerreiro()
        
        self.cen=Cenarios()
        self.cen.dungeons()
        self.cen.story()
        self.cen.Shadowrun()
        
        self.jo=Jogando()
        self.jo.etapas()
        

class Classes:
    def __init__(self):
        print ('Algumas Classes:\n')
    def babaro(self):
        print('-Bárbaro:\nVocê primeiro bate e depois pergunta o que tá acontencendo. Um Bárbaro é uma fonte bruta de poder físico,um ignorante intelectual, nascido apenas para matar e pilhar.')
    def bardo(self):
        print("-Bardo:\nSe inspira e elabora magias com seu alaúde mágico, flauta ou voz. Acima de tudo um estudioso das ondas sonoras. E sabe o poder que elas tem.Também pode ser um pé no saco do grupo!")
    def clerigo(self):
        print("-Clérigo:\nVocê é a mão dos deuses sagrados. Além de curar e proteger seu time, também arrebata de vez os mortos-vivos.Nada de demoníaco e maligno passará por você.")
    def druida(self):
        print("-Druida:\nUma classe de servos da natureza, a reverenciam acima de tudo, adquirindoseus poderes mágicos através dela ou de uma divindade.")
    def Feiticeiro(self):
        print("-Feiticeiro:\nPessoas com poder mágico fluindo em suas veias. De maneira hereditária ou por uma origem mística e obscura.")
    def Guerreiro(self):
        print("-Guerreiro:\nA classe mais jogada e diversificada, você pode fazer bastante coisa em relação ao combate, indicado para principiantes de jogadores experientes")
class Cenarios:
    def __init__(self):
        print("\nAonde você gostaria de jogar seu RPG? Em um futuro apocalíptico como em Walking Dead, ou em uma galáxia distante de Star Wars? Ou quem sabe em Westeros de Game of Thrones ou na Terra Média de Senhor dos Anéis?.por exemplo:")
              
    def dungeons(self):
        print("Dungeons & Dragons:\nPerfeito pra jogar em um mundo Medieval/Fantasia, com dragões e criaturas mágicas. ")
    def story(self):
        print("Storyteller:\nNos anos 90 eles criaram, Vampiro A Máscara, Mago: A Ascensão e Lobisomem: O Apocalipse. Os nomes já são auto-explicativos. ")
    def Shadowrun(self):
        print("Shadowrun/cyberpunk2020:\n Em um futuro cyberpunk  a moda é usar implantes para melhorar suas habilidades e hackers que invadem sistemas de segurança de mega-corporações criminosas.")
class Jogando:
    def __init__(self):
        print("\nQual será a missão do grupo de aventureiros? Salvar uma princesa de um mago sinistro? Resolver um problema diplomático entre dois reinos? Roubar os planos da estrela da morte? ")
    def etapas(self):
        print("Crie  etapas pelas quais os jogadores irão passa, armadilhas,inimigos e tesouros.Pense em pequenas side-quests caso os jogadores se desviarem do caminho.")


class RPG:
    def __init__(self):
        print("O que é um RPG de mesa ?")
    def como_jogar(self):
        print("É um jogo de interpretação de personagens.O mestre narra uma historia,descreve cenários e seus acontecimentos.Os jogadores(2-6),falam o que gostariam de fazer.dessa maneira o jogo se desenrola dentro da imaginação de cada um!\n")
        self.rpg=Jogar()
        self.rpg.Organicao()

vs=RPG()
vs.como_jogar()

