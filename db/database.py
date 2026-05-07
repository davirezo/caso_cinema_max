import sqlite3

DB_PATH = "cinema.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            nome      TEXT NOT NULL,
            cidade    TEXT NOT NULL,
            estado    TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo      TEXT NOT NULL,
            duracao_min INTEGER NOT NULL,
            genero      TEXT NOT NULL,
            diretor     TEXT NOT NULL,
            elenco      TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sessoes (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id  INTEGER NOT NULL REFERENCES cinemas(id),
            filme_id   INTEGER NOT NULL REFERENCES filmes(id),
            data       TEXT NOT NULL,
            horario    TEXT NOT NULL,
            sala       TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS registros_publico (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id      INTEGER NOT NULL REFERENCES sessoes(id),
            quantidade     INTEGER NOT NULL,
            data_registro  TEXT NOT NULL
        )
    """)

    conn.commit()
    return conn
