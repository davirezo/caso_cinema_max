from model.filme import Filme
from repository.filme_repository import FilmeRepository


class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def criar_filme(self, titulo: str, duracao_min: int, genero: str, diretor: str, elenco: str = ""):
        if not titulo.strip():
            raise ValueError("Título do filme não pode ser vazio.")
        if duracao_min <= 0:
            raise ValueError("Duração deve ser maior que zero.")
        filme = Filme(titulo, duracao_min, genero, diretor, elenco)
        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar()

    def buscar_por_id(self, filme_id: int):
        return self.repository.buscar_por_id(filme_id)
