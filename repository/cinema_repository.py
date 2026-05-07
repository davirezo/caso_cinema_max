from db.database import get_connection
from model.cinema import Cinema


class CinemaRepository:

    def salvar(self, cinema: Cinema):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cinemas (nome, cidade, estado, capacidade) VALUES (?, ?, ?, ?)",
            (cinema.nome, cinema.cidade, cinema.estado, cinema.capacidade)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cidade, estado, capacidade FROM cinemas")
        rows = cursor.fetchall()
        conn.close()
        return [Cinema(r[1], r[2], r[3], r[4], r[0]) for r in rows]

    def buscar_por_id(self, cinema_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cidade, estado, capacidade FROM cinemas WHERE id = ?", (cinema_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Cinema(row[1], row[2], row[3], row[4], row[0])
        return None
