from model.sessao import Sessao
from repository.sessao_repository import SessaoRepository
from repository.cinema_repository import CinemaRepository
from repository.filme_repository import FilmeRepository


class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()
        self.cinema_repo = CinemaRepository()
        self.filme_repo = FilmeRepository()

    def criar_sessao(self, cinema_id: int, filme_id: int, data: str, horario: str, sala: str):
        if not self.cinema_repo.buscar_por_id(cinema_id):
            raise ValueError("Cinema não encontrado.")
        if not self.filme_repo.buscar_por_id(filme_id):
            raise ValueError("Filme não encontrado.")
        sessao = Sessao(cinema_id, filme_id, data, horario, sala)
        self.repository.salvar(sessao)

    def listar_sessoes(self):
        return self.repository.listar()

    def buscar_por_id(self, sessao_id: int):
        return self.repository.buscar_por_id(sessao_id)
