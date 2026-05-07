from flask import Flask, request, render_template_string
from service.cinema_service import CinemaService
from service.filme_service import FilmeService
from service.sessao_service import SessaoService
from service.registro_publico_service import RegistroPublicoService

TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rede de Cinemas</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; background: #f5f5f5; color: #333; }
    h1 { color: #1a1a2e; border-bottom: 3px solid #e94560; padding-bottom: 10px; }
    h2 { color: #16213e; margin-top: 30px; }
    .card { background: #fff; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    form label { display: block; margin-top: 10px; font-weight: bold; font-size: 13px; }
    form input, form select { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; margin-top: 4px; box-sizing: border-box; }
    button { margin-top: 14px; padding: 10px 24px; background: #e94560; color: #fff; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; }
    button:hover { background: #c73652; }
    .alert-ok  { background: #d4edda; color: #155724; padding: 10px; border-radius: 4px; margin-bottom: 10px; }
    .alert-err { background: #f8d7da; color: #721c24; padding: 10px; border-radius: 4px; margin-bottom: 10px; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; }
    th { background: #16213e; color: #fff; padding: 8px 12px; text-align: left; }
    td { padding: 7px 12px; border-bottom: 1px solid #eee; }
    tr:hover td { background: #f0f4ff; }
    .tabs { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }
    .tabs a { padding: 8px 16px; background: #16213e; color: #fff; text-decoration: none; border-radius: 4px; font-size: 13px; }
    .tabs a:hover { background: #e94560; }
    .total-box { background: #16213e; color: #fff; padding: 16px 20px; border-radius: 8px; font-size: 18px; display: inline-block; }
  </style>
</head>
<body>
  <h1>🎬 Rede de Cinemas</h1>
  <div class="tabs">
    <a href="/">Cinemas</a>
    <a href="/filmes">Filmes</a>
    <a href="/sessoes">Sessões</a>
    <a href="/registros">Registrar Público</a>
    <a href="/totalizacoes">Totalizações</a>
  </div>

  {% if mensagem %}<div class="alert-ok">✔ {{ mensagem }}</div>{% endif %}
  {% if erro %}<div class="alert-err">✘ {{ erro }}</div>{% endif %}

  {{ conteudo | safe }}
</body>
</html>
"""


class CinemaViewWeb:

    def __init__(self):
        self.app = Flask(__name__)
        self.cinema_svc = CinemaService()
        self.filme_svc = FilmeService()
        self.sessao_svc = SessaoService()
        self.registro_svc = RegistroPublicoService()
        self._registrar_rotas()

    def _render(self, conteudo, mensagem=None, erro=None):
        return render_template_string(TEMPLATE, conteudo=conteudo, mensagem=mensagem, erro=erro)

    def _registrar_rotas(self):

        @self.app.route("/", methods=["GET", "POST"])
        def cinemas():
            mensagem = erro = None
            if request.method == "POST":
                try:
                    self.cinema_svc.criar_cinema(
                        request.form["nome"], request.form["cidade"],
                        request.form["estado"], int(request.form["capacidade"])
                    )
                    mensagem = "Cinema cadastrado com sucesso!"
                except Exception as e:
                    erro = str(e)
            lista = self.cinema_svc.listar_cinemas()
            rows = "".join(
                f"<tr><td>{c.id}</td><td>{c.nome}</td><td>{c.cidade}</td><td>{c.estado}</td><td>{c.capacidade}</td></tr>"
                for c in lista
            )
            conteudo = f"""
            <div class="card">
              <h2>Cadastrar Cinema</h2>
              <form method="POST">
                <label>Nome</label><input name="nome" required>
                <label>Cidade</label><input name="cidade" required>
                <label>Estado (UF)</label><input name="estado" maxlength="2" required>
                <label>Capacidade</label><input name="capacidade" type="number" min="1" required>
                <button type="submit">Cadastrar</button>
              </form>
            </div>
            <div class="card">
              <h2>Cinemas cadastrados</h2>
              <table><tr><th>ID</th><th>Nome</th><th>Cidade</th><th>Estado</th><th>Capacidade</th></tr>{rows}</table>
            </div>
            """
            return self._render(conteudo, mensagem, erro)

        @self.app.route("/filmes", methods=["GET", "POST"])
        def filmes():
            mensagem = erro = None
            if request.method == "POST":
                try:
                    self.filme_svc.criar_filme(
                        request.form["titulo"], int(request.form["duracao"]),
                        request.form["genero"], request.form["diretor"], request.form.get("elenco", "")
                    )
                    mensagem = "Filme cadastrado com sucesso!"
                except Exception as e:
                    erro = str(e)
            lista = self.filme_svc.listar_filmes()
            rows = "".join(
                f"<tr><td>{f.id}</td><td>{f.titulo}</td><td>{f.genero}</td><td>{f.diretor}</td><td>{f.duracao_min} min</td></tr>"
                for f in lista
            )
            conteudo = f"""
            <div class="card">
              <h2>Cadastrar Filme</h2>
              <form method="POST">
                <label>Título</label><input name="titulo" required>
                <label>Duração (min)</label><input name="duracao" type="number" min="1" required>
                <label>Gênero</label><input name="genero" required>
                <label>Diretor</label><input name="diretor" required>
                <label>Elenco</label><input name="elenco">
                <button type="submit">Cadastrar</button>
              </form>
            </div>
            <div class="card">
              <h2>Filmes cadastrados</h2>
              <table><tr><th>ID</th><th>Título</th><th>Gênero</th><th>Diretor</th><th>Duração</th></tr>{rows}</table>
            </div>
            """
            return self._render(conteudo, mensagem, erro)

        @self.app.route("/sessoes", methods=["GET", "POST"])
        def sessoes():
            mensagem = erro = None
            if request.method == "POST":
                try:
                    self.sessao_svc.criar_sessao(
                        int(request.form["cinema_id"]), int(request.form["filme_id"]),
                        request.form["data"], request.form["horario"], request.form["sala"]
                    )
                    mensagem = "Sessão cadastrada com sucesso!"
                except Exception as e:
                    erro = str(e)
            lista = self.sessao_svc.listar_sessoes()
            rows = "".join(
                f"<tr><td>{s[0]}</td><td>{s[6]}</td><td>{s[7]}</td><td>{s[3]}</td><td>{s[4]}</td><td>{s[5]}</td></tr>"
                for s in lista
            )
            conteudo = f"""
            <div class="card">
              <h2>Cadastrar Sessão</h2>
              <form method="POST">
                <label>ID do Cinema</label><input name="cinema_id" type="number" required>
                <label>ID do Filme</label><input name="filme_id" type="number" required>
                <label>Data</label><input name="data" type="date" required>
                <label>Horário</label><input name="horario" type="time" required>
                <label>Sala</label><input name="sala" required>
                <button type="submit">Cadastrar</button>
              </form>
            </div>
            <div class="card">
              <h2>Sessões cadastradas</h2>
              <table><tr><th>ID</th><th>Cinema</th><th>Filme</th><th>Data</th><th>Horário</th><th>Sala</th></tr>{rows}</table>
            </div>
            """
            return self._render(conteudo, mensagem, erro)

        @self.app.route("/registros", methods=["GET", "POST"])
        def registros():
            mensagem = erro = None
            if request.method == "POST":
                try:
                    self.registro_svc.registrar(
                        int(request.form["sessao_id"]),
                        int(request.form["quantidade"])
                    )
                    mensagem = "Público registrado com sucesso!"
                except Exception as e:
                    erro = str(e)
            conteudo = """
            <div class="card">
              <h2>Registrar Público de Sessão</h2>
              <form method="POST">
                <label>ID da Sessão</label><input name="sessao_id" type="number" required>
                <label>Quantidade de Público</label><input name="quantidade" type="number" min="1" required>
                <button type="submit">Registrar</button>
              </form>
            </div>
            """
            return self._render(conteudo, mensagem, erro)

        @self.app.route("/totalizacoes", methods=["GET", "POST"])
        def totalizacoes():
            mensagem = erro = None
            total_html = ""
            if request.method == "POST":
                try:
                    tipo = request.form["tipo"]
                    id_val = int(request.form["id_val"])
                    if tipo == "sessao":
                        total = self.registro_svc.total_por_sessao(id_val)
                        label = f"Total de público – Sessão #{id_val}"
                    elif tipo == "filme":
                        total = self.registro_svc.total_por_filme(id_val)
                        label = f"Total de público – Filme #{id_val}"
                    else:
                        total = self.registro_svc.total_por_cinema(id_val)
                        label = f"Total de público – Cinema #{id_val}"
                    total_html = f'<div class="total-box">{label}: <strong>{total} pessoas</strong></div>'
                except Exception as e:
                    erro = str(e)
            conteudo = f"""
            <div class="card">
              <h2>Consultar Totalização de Público</h2>
              <form method="POST">
                <label>Consultar por</label>
                <select name="tipo">
                  <option value="sessao">Sessão</option>
                  <option value="filme">Filme</option>
                  <option value="cinema">Cinema</option>
                </select>
                <label>ID</label><input name="id_val" type="number" required>
                <button type="submit">Consultar</button>
              </form>
            </div>
            {('<div class="card">' + total_html + '</div>') if total_html else ''}
            """
            return self._render(conteudo, mensagem, erro)

    def run(self):
        self.app.run(debug=True)
