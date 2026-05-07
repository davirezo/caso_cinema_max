from db.database import get_connection
from model.sessao import Sessao


class SessaoRepository:

    def salvar(self, sessao: Sessao):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sessoes (cinema_id, filme_id, data, horario, sala) VALUES (?, ?, ?, ?, ?)",
            (sessao.cinema_id, sessao.filme_id, sessao.data, sessao.horario, sessao.sala)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, s.cinema_id, s.filme_id, s.data, s.horario, s.sala,
                   c.nome AS cinema_nome, f.titulo AS filme_titulo
            FROM sessoes s
            JOIN cinemas c ON c.id = s.cinema_id
            JOIN filmes f ON f.id = s.filme_id
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def buscar_por_id(self, sessao_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, cinema_id, filme_id, data, horario, sala FROM sessoes WHERE id = ?",
            (sessao_id,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Sessao(row[1], row[2], row[3], row[4], row[5], row[0])
        return None
