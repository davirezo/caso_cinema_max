class Cinema:
    def __init__(self, nome: str, cidade: str, estado: str, capacidade: int, id: int = None):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.capacidade = capacidade
