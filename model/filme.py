class Filme:
    def __init__(self, titulo: str, duracao_min: int, genero: str, diretor: str, elenco: str = "", id: int = None):
        self.id = id
        self.titulo = titulo
        self.duracao_min = duracao_min
        self.genero = genero
        self.diretor = diretor
        self.elenco = elenco
