import sys
paht_main = r"C:\Users\evert\OneDrive\Desktop\Jogo_RPG_EntrePastas"
sys.path.append(paht_main)






class Personagem:
    def __init__(self, nome,HP):
        self.nome = nome
        self.HP = HP
    
    def atacar(self):
        dano = 20
        return dano



Objeto_Personagem1 = Personagem('Gabriel', 250)



if __name__ ==  '__main__':
   
    print(Objeto_Personagem1.atacar())