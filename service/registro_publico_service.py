from datetime import date
from model.registro_publico import RegistroPublico
from repository.registro_publico_repository import RegistroPublicoRepository
from repository.sessao_repository import SessaoRepository
from repository.cinema_repository import CinemaRepository


class RegistroPublicoService:

    def __init__(self):
        self.repository = RegistroPublicoRepository()
        self.sessao_repo = SessaoRepository()
        self.cinema_repo = CinemaRepository()

    def registrar(self, sessao_id: int, quantidade: int):
        sessao = self.sessao_repo.buscar_por_id(sessao_id)
        if not sessao:
            raise ValueError("Sessão não encontrada.")

        cinema = self.cinema_repo.buscar_por_id(sessao.cinema_id)
        if quantidade > cinema.capacidade:
            raise ValueError(
                f"Quantidade ({quantidade}) excede a capacidade do cinema ({cinema.capacidade})."
            )
        if quantidade <= 0:
            raise ValueError("A quantidade de público deve ser maior que zero.")

        registro = RegistroPublico(
            sessao_id=sessao_id,
            quantidade=quantidade,
            data_registro=date.today().isoformat()
        )
        self.repository.salvar(registro)

    def total_por_sessao(self, sessao_id: int) -> int:
        return self.repository.total_por_sessao(sessao_id)

    def total_por_filme(self, filme_id: int) -> int:
        return self.repository.total_por_filme(filme_id)

    def total_por_cinema(self, cinema_id: int) -> int:
        return self.repository.total_por_cinema(cinema_id)
