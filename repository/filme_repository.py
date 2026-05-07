from db.database import get_connection
from model.filme import Filme


class FilmeRepository:

    def salvar(self, filme: Filme):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filmes (titulo, duracao_min, genero, diretor, elenco) VALUES (?, ?, ?, ?, ?)",
            (filme.titulo, filme.duracao_min, filme.genero, filme.diretor, filme.elenco)
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, duracao_min, genero, diretor, elenco FROM filmes")
        rows = cursor.fetchall()
        conn.close()
        return [Filme(r[1], r[2], r[3], r[4], r[5], r[0]) for r in rows]

    def buscar_por_id(self, filme_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, duracao_min, genero, diretor, elenco FROM filmes WHERE id = ?", (filme_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Filme(row[1], row[2], row[3], row[4], row[5], row[0])
        return None
