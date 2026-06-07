⚔️ jogo_RPG — Batalha entre pastas

Projeto Python com dois personagens de RPG que vivem em pastas separadas e se comunicam através de um orquestrador central.

Sobre o projeto

A ideia começou simples: dois personagens de RPG brigando em Python com classes. Mas resolvi complicar de propósito — cada personagem mora em uma pasta diferente, e o objetivo foi aprender a fazer essas pastas se comunicarem.

Desnecessário? Sim. Valeu a experiência? Com certeza.

O que aprendi

— Como o Python resolve imports usando sys.path
— Como adicionar caminhos personalizados com sys.path.append()
— O problema de importação circular e como evitá-lo
— O padrão de orquestrador com um main.py central
— Separação de responsabilidades: cada arquivo faz uma coisa só

Estrutura

jogo_RPG/
├── Personagem_1/
│   └── personagem_1.py
├── Personagem_2/
│   └── personagem_2.py
└── main.py
Feito como exercício prático de Python — foco no aprendizado, não no resultado.