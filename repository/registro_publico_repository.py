from db.database import get_connection
from model.registro_publico import RegistroPublico


class RegistroPublicoRepository:

    def salvar(self, registro: RegistroPublico):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registros_publico (sessao_id, quantidade, data_registro) VALUES (?, ?, ?)",
            (registro.sessao_id, registro.quantidade, registro.data_registro)
        )
        conn.commit()
        conn.close()

    def total_por_sessao(self, sessao_id: int) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COALESCE(SUM(quantidade), 0) FROM registros_publico WHERE sessao_id = ?",
            (sessao_id,)
        )
        total = cursor.fetchone()[0]
        conn.close()
        return total

    def total_por_filme(self, filme_id: int) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COALESCE(SUM(r.quantidade), 0)
            FROM registros_publico r
            JOIN sessoes s ON s.id = r.sessao_id
            WHERE s.filme_id = ?
        """, (filme_id,))
        total = cursor.fetchone()[0]
        conn.close()
        return total

    def total_por_cinema(self, cinema_id: int) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COALESCE(SUM(r.quantidade), 0)
            FROM registros_publico r
            JOIN sessoes s ON s.id = r.sessao_id
            WHERE s.cinema_id = ?
        """, (cinema_id,))
        total = cursor.fetchone()[0]
        conn.close()
        return total
