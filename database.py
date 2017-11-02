import psycopg2

class psqldatabase:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=karaoke user=postgres")
        self.cur = conn.cursor()

    def CTABLE(self):
        self.cur.execute("CREATE TABLE songs (id serial PRIMARY KEY, title varchar, url varchar);")

    def GET_ALL(self):
        self.cur.execute("SELECT * FROM songs;")
        return self.cur.fetchall()

    def GET_SONG_URL(self, title):
        self.cur.execute("SELECT url FROM songs WHERE title=" + title)
        return self.cur.fetchone()

    def STORE_SONG(self, title, url):
        self.cur.execute("INSERT INTO songs (title, url) \
                VALUES ('" + title + "', '" + url "');")
