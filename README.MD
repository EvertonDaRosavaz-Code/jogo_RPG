⚔️ jogo_RPG — Batalha entre pastas

Projeto Python com personagens de RPG de tipos diferentes que vivem em pastas separadas e se comunicam através de um orquestrador central.

Sobre o projeto

A ideia começou simples: dois personagens de RPG brigando em Python com classes. Mas resolvi complicar de propósito — cada personagem mora em uma pasta diferente, e o objetivo foi aprender a fazer essas pastas se comunicarem.

Depois evoluiu: pensei em criar tipos de personagens como Mago, Tank e Assassino, cada um com atributos padrão diferentes. Desnecessário? Sim. Valeu a experiência? Com certeza.

O que aprendi

— Como o Python resolve imports usando sys.path
— Como adicionar caminhos personalizados com sys.path.append()
— O problema de importação circular e como evitá-lo
— O padrão de orquestrador com um main.py central
— Separação de responsabilidades: cada arquivo faz uma coisa só
— Herança em Python: como uma classe filha herda atributos e métodos da classe pai
— Uso do super() para reaproveitar o __init__ da classe pai

Estrutura

jogo_RPG/
├── personagens/
│   ├── assasino.py
│   ├── mago.py
│   └── tank.py
├── classePai.py
├── main.py
└── README.md
Feito como exercício prático de Python — foco no aprendizado, não no resultado.