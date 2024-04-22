import random


def GetCidades():
    return [
        "Fortaleza",
        "São Paulo",
        "Vitória",
        "Vila Velha",
        "Bauru",
        "Americana",
        "Cariacica",
        "Amsterdam",
        "New York",
        "Minnesota",
        "Pindamonhagaba",
        "Domingos Martins",
        "Cidade de Deus",
        "Rio De Janeiro",
        "Teresópolis"
    ]


def GetNome_Livros():
    return [
        ["Astro", "Astronomia", "Agropecuária", "Agricultura"],
        ["Brasil", "Briga", "Bill", "Burguer", "Brenos"],
        ["Canela", "Carreira", "Crime", "Caindo", "Canalizando"],
        ["Dinheiro", "Dinamismo", "Democracia", "Dados"],
        ["Estorno", "Estrondo", "Emanuel", "Estilo"],
        ["Feijão", "Fração", "Feitiço", "Farinha"],
        ["Galinha", "Gálio", "Genero", "Games"],
        ["Horario", "Hemisferio", "Humildade"],
        ["Incendio", "Imaginação", "Inaudível"],
        ["Joao", "Jiboia", "Jacaré"],
        ["Kate", "Kilo", "KickBoxing"],
        ["Leao", "Leonardo", "Lama"],
        ["Maria", "Mercado", "Mecanico"],
        ["Negocios", "Negação", "Nilo"],
        ["Oswaldo", "Olhar", "Oculos"],
        ["Paragrafo", "Perigoso", "Palmito"],
        ["Querer", "Quasimodo", "Quase"],
        ["Remoer", "Refazer", "Reaprender"],
        ["Salto", "Santo", "Segunda"],
        ["Texto", "Tutorial", "Termômetro"],
        ["Universo", "Universal", "Unico"],
        ["Vasto", "Vermelho", "Vazio"],
        ["Wander", "Waldinei", "Wow"],
        ["Xarope", "Xadrez", "Xeque-mate"],
        ["Zebra", "Zagueiro", "Zangado"]
    ]

def GetNomes():
    return [
            "Oswaldo",
            "Cleber",
            "Reginaldo",
            "Clara",
            "Mauricio",
            "Meireless",
            "Paula",
            "Rodrigo",
            "Pernambuco",
            "Roger",
            "Marcia",
            "Clarisse",
            "Amanda",
            "Carlos",
            "Carla",
            "Francisco",
            "Frederico",
            "Thiago",
            "Carol"
        ]

def GetSobrenomes():
    return [
            "Guimaraes",
            "Souza",
            "Rodrigues",
            "Rocha",
            "Santos",
            "Augusto",
            "Francisco",
            "Santana",
            "Cunha",
            "Pedra",
            "Carvalho",
            "Eucalipto",
            "Abeto",
            "Silva",
            "Salva",
            "Americano"
        ]

def GerarNomeAleatorio():
    random.choice(GetNomes()) + " " + random.choice(GetSobrenomes())