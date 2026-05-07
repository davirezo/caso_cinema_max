class Sessao:
    def __init__(self, cinema_id: int, filme_id: int, data: str, horario: str, sala: str, id: int = None):
        self.id = id
        self.cinema_id = cinema_id
        self.filme_id = filme_id
        self.data = data
        self.horario = horario
        self.sala = sala
