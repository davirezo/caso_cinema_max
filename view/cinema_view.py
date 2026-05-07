class CinemaView:

    def mostrar_menu(self):
        print("\n========== REDE DE CINEMAS ==========")
        print("1 - Cadastrar Cinema")
        print("2 - Listar Cinemas")
        print("3 - Cadastrar Filme")
        print("4 - Listar Filmes")
        print("5 - Cadastrar Sessão")
        print("6 - Listar Sessões")
        print("7 - Registrar Público de Sessão")
        print("8 - Consultar Totalizações de Público")
        print("0 - Sair")
        print("=====================================")

    def obter_dados_cinema(self):
        nome = input("Nome do cinema: ")
        cidade = input("Cidade: ")
        estado = input("Estado (UF): ")
        capacidade = input("Capacidade (nº de lugares): ")
        return nome, cidade, estado, capacidade

    def obter_dados_filme(self):
        titulo = input("Título do filme: ")
        duracao = input("Duração (minutos): ")
        genero = input("Gênero: ")
        diretor = input("Diretor: ")
        elenco = input("Elenco (separado por vírgulas): ")
        return titulo, duracao, genero, diretor, elenco

    def obter_dados_sessao(self):
        cinema_id = input("ID do cinema: ")
        filme_id = input("ID do filme: ")
        data = input("Data (YYYY-MM-DD): ")
        horario = input("Horário (HH:MM): ")
        sala = input("Sala: ")
        return cinema_id, filme_id, data, horario, sala

    def obter_dados_registro(self):
        sessao_id = input("ID da sessão: ")
        quantidade = input("Quantidade de público: ")
        return sessao_id, quantidade

    def obter_tipo_totalizacao(self):
        print("\nConsultar total por:")
        print("1 - Sessão")
        print("2 - Filme")
        print("3 - Cinema")
        tipo = input("Escolha: ")
        id_val = input("Informe o ID: ")
        return tipo, id_val

    def mostrar_cinemas(self, cinemas):
        print("\n=== CINEMAS ===")
        for c in cinemas:
            print(f"[{c.id}] {c.nome} – {c.cidade}/{c.estado} – Cap.: {c.capacidade}")
        print("===============")

    def mostrar_filmes(self, filmes):
        print("\n=== FILMES ===")
        for f in filmes:
            print(f"[{f.id}] {f.titulo} ({f.genero}) – Dir.: {f.diretor} – {f.duracao_min} min")
        print("==============")

    def mostrar_sessoes(self, sessoes):
        print("\n=== SESSÕES ===")
        for s in sessoes:
            print(f"[{s[0]}] {s[6]} exibe '{s[7]}' em {s[3]} às {s[4]} – Sala: {s[5]}")
        print("===============")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n>> {mensagem}")
