import psycopg2

class psqldatabase:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=karaoke_songs user=")
        self.cur = conn.cursor()

    def CTABLE(self):
        self.cur.execute("CREATE TABLE songs (id serial PRIMARY KEY, title varchar, url varchar);")

    def GET_ALL(self):
        self.cur.execute("SELECT * FROM songs;")
        self.cur.fetchone()
