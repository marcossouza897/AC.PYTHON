# Esse é o nosso façade
class como_jogar:
    def __init__(self):
        print('O que é preciso pra jogar RPG?')

    def organizar(self):
        self.hoteleiro = Hoteleiro().reseva_hotel()
        
        self.fornecedor = Fornecedor()
        self.fornecedor.set_cozinha()
        
        self.florista = Florista()
        self.florista.set_requisitos_flor()
        
        self.musico = Musico()
        self.musico.set_tipo_musica()

#Subsistema 1
class Hoteleiro:
    def __init__(self):
        print('OrganizaNDO O  Hotel para um casamento')
    def __esta_disponivel(self):
        print('O Hotel esta livre para o evento neste dia ?')
        return True
    def reseva_hotel(self):
        if self.__esta_disponivel():
            print('Registrou a reseva')


#Subsitema 2
class Florista:
    def __init__(self):
        print('Decoração de flores para o evento ?')
    def set_requisitos_flor(self):
        print('Rosas e lírios serão usadas')


#Subsistema 3
class Fornecedor:
    def __init__(self):
        print('Organização da comida para o evento ?')
    def set_cozinha(self):
        print('Comida chinesa e regional será servida')


#Subsistema 4
class Musico:
    def __init__(self):
        print('Organização de musica para o evento ?')
    def set_tipo_musica(self):
        print('Rock  musica pop será tocada')


#Cliente
class RPG:
    def __init__(self):
        print('U QUE É UM RPG DE MESA ?')

    def como_jogar(self):
        print('RPG ou Role Playing Game é um jogo de interpretação de personagens. o Mestre da masmorra (DM, ou Dungeon Master) que é \npraticamente Deus, narra uma história, descrevendo cada cenário e seus acontecimentos. Os jogadores (2-6 jogadores é o indicado) por sua vez, falam o que gostariam de fazer. Para cada ação mais complexa, dados precisam ser rolados para saber se a ação foi bem sucedida. Dessa maneira o jogo se desenrola dentro na imaginação de cada um!')
        org_eventos = como_jogar()
        org_eventos.Hoteleiro()

    def __del__(self):
        print('Obrigado organizar de eventos, deu tudo certo')

vc = RPG()
vc.como_jogar()
              
