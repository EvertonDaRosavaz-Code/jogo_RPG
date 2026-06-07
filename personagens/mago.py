import sys
sys.path.append(r"C:\Users\evert\OneDrive\Desktop\Jogo_RPG_EntrePastas")
from classePai import Personagem
hp = 120
mana = 180
resistencia = 20
dano = 20


class ObjMago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, hp, mana, resistencia, dano)
        self.nome = nome
