import os
import sqlite3

db_filename = 'sqlite3.db'
schema_filename = 'schema.sql'

def getdb():
    return sqlite3.connect(db_filename)

if __name__ == "__main__":
    with sqlite3.connect(db_filename) as conn:
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

