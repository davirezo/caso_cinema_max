from view.cinema_view import CinemaView
from controller.cinema_controller import (
    CinemaController, FilmeController,
    SessaoController, RegistroPublicoController
)


def main():
    view = CinemaView()
    cinema_ctrl = CinemaController(view)
    filme_ctrl = FilmeController(view)
    sessao_ctrl = SessaoController(view)
    registro_ctrl = RegistroPublicoController(view)

    while True:
        view.mostrar_menu()
        opcao = input("Opção: ").strip()

        try:
            if opcao == "1":
                cinema_ctrl.criar_cinema()
            elif opcao == "2":
                cinema_ctrl.listar_cinemas()
            elif opcao == "3":
                filme_ctrl.criar_filme()
            elif opcao == "4":
                filme_ctrl.listar_filmes()
            elif opcao == "5":
                sessao_ctrl.criar_sessao()
            elif opcao == "6":
                sessao_ctrl.listar_sessoes()
            elif opcao == "7":
                registro_ctrl.registrar_publico()
            elif opcao == "8":
                registro_ctrl.consultar_totalizacoes()
            elif opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                view.mostrar_mensagem("Opção inválida.")
        except ValueError as e:
            view.mostrar_mensagem(f"Erro: {e}")


if __name__ == "__main__":
    main()
