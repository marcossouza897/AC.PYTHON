# Esse é o nosso façade
class Organizador_eventos:
    def __init__(self):
        print('Organizador: Falarei com o pessoal')

    def organizar(self):
        self.hoteleiro = Hoteleiro()
        Hoteleiro().reseva_hotel()
        
        self.fornecedor = Fornecedor()
        self.fornecedor.set_cozinha()
        
        self.florista = Florista()
        self.florista.set_requisitos_flor()
        
        self.musico = Musico()
        self.musico.set_tipo_musica()

#Subsistema 1
class Hoteleiro:
    def __init__(self):
        print('Organizador o Hotel para um casamento ?')
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
class Voce:
    def __init__(self):
        print('Você é o responsável pelo casamento ?')

    def pergunte_organizador_eventos(self):
        print('Vamos ligar para o Organizador de Eventos!')
        org_eventos = Organizador_eventos()
        org_eventos.organizar()

    def __del__(self):
        print('Obrigado organizar de eventos, deu tudo certo')

vc = Voce()
vc.pergunte_organizador_eventos()
              
