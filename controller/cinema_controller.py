from service.cinema_service import CinemaService
from service.filme_service import FilmeService
from service.sessao_service import SessaoService
from service.registro_publico_service import RegistroPublicoService


class CinemaController:

    def __init__(self, view):
        self.service = CinemaService()
        self.view = view

    def criar_cinema(self):
        nome, cidade, estado, capacidade = self.view.obter_dados_cinema()
        self.service.criar_cinema(nome, cidade, estado, int(capacidade))
        self.view.mostrar_mensagem("Cinema cadastrado com sucesso!")

    def listar_cinemas(self):
        cinemas = self.service.listar_cinemas()
        self.view.mostrar_cinemas(cinemas)


class FilmeController:

    def __init__(self, view):
        self.service = FilmeService()
        self.view = view

    def criar_filme(self):
        titulo, duracao, genero, diretor, elenco = self.view.obter_dados_filme()
        self.service.criar_filme(titulo, int(duracao), genero, diretor, elenco)
        self.view.mostrar_mensagem("Filme cadastrado com sucesso!")

    def listar_filmes(self):
        filmes = self.service.listar_filmes()
        self.view.mostrar_filmes(filmes)


class SessaoController:

    def __init__(self, view):
        self.service = SessaoService()
        self.view = view

    def criar_sessao(self):
        cinema_id, filme_id, data, horario, sala = self.view.obter_dados_sessao()
        self.service.criar_sessao(int(cinema_id), int(filme_id), data, horario, sala)
        self.view.mostrar_mensagem("Sessão cadastrada com sucesso!")

    def listar_sessoes(self):
        sessoes = self.service.listar_sessoes()
        self.view.mostrar_sessoes(sessoes)


class RegistroPublicoController:

    def __init__(self, view):
        self.service = RegistroPublicoService()
        self.view = view

    def registrar_publico(self):
        sessao_id, quantidade = self.view.obter_dados_registro()
        self.service.registrar(int(sessao_id), int(quantidade))
        self.view.mostrar_mensagem("Público registrado com sucesso!")

    def consultar_totalizacoes(self):
        tipo, id_val = self.view.obter_tipo_totalizacao()
        if tipo == "1":
            total = self.service.total_por_sessao(int(id_val))
            self.view.mostrar_mensagem(f"Total de público na sessão {id_val}: {total} pessoas")
        elif tipo == "2":
            total = self.service.total_por_filme(int(id_val))
            self.view.mostrar_mensagem(f"Total de público no filme {id_val}: {total} pessoas")
        elif tipo == "3":
            total = self.service.total_por_cinema(int(id_val))
            self.view.mostrar_mensagem(f"Total de público no cinema {id_val}: {total} pessoas")
        else:
            self.view.mostrar_mensagem("Opção inválida.")
