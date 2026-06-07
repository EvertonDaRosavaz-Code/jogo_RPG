import sys

path_personmagem1 = r"C:\Users\evert\OneDrive\Desktop\Jogo_RPG_EntrePastas\Personagem_1"
path_personmagem2 = r"C:\Users\evert\OneDrive\Desktop\Jogo_RPG_EntrePastas\Personagem_2"

sys.path.append(path_personmagem1)
sys.path.append(path_personmagem2)

from personagem_1 import Objeto_Personagem1
from personagem_2 import Objeto_Personagem2

print(Objeto_Personagem1.nome)
print(Objeto_Personagem2.nome)