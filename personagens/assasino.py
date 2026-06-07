import sys
sys.path.append(r"C:\Users\evert\OneDrive\Desktop\Jogo_RPG_EntrePastas")
from classePai import Personagem
hp = 200
mana = 0
resistencia = 40
dano = 100


class ObjAssasino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, hp, mana, resistencia, dano)
        self.nome = nome








