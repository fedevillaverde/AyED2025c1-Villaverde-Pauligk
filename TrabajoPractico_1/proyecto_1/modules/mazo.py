from modules.lista_doble_enlazada import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta 
class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.__mazo = ListaDobleEnlazada()
    @property
    def mazo(self):
        return self.__mazo
    @mazo.setter
    def mazo(self, mazo_nuevo):
        self.__mazo = mazo_nuevo
    def sacar_carta_arriba(self,mostrar=False):
        if self.__mazo.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        else:
            if mostrar:
                print(self.__mazo.cabeza.dato)
            return self.__mazo.extraer(0)  # Extrae la carta de la cabeza

    def poner_carta_abajo(self, nueva_carta):
        if type(nueva_carta) != Carta:
            raise TypeError("El elemento a agregar debe ser una carta")
        self.__mazo.agregar_al_final(nueva_carta)
    def poner_carta_arriba(self, nueva_carta):
        if type(nueva_carta) != Carta:
            raise TypeError("El elemento a agregar debe ser una carta")
        self.__mazo.agregar_al_inicio(nueva_carta)
    def __len__(self):
        return self.__mazo.tamano
    def esta_vacio(self):
        return self.__mazo.esta_vacia()

    