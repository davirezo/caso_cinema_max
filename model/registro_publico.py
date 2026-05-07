class RegistroPublico:
    def __init__(self, sessao_id: int, quantidade: int, data_registro: str, id: int = None):
        self.id = id
        self.sessao_id = sessao_id
        self.quantidade = quantidade
        self.data_registro = data_registro
