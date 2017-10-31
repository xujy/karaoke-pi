from flask import Flask
from flask import request
from flask import render_template
from Queue import Queue

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    song = request.form['song']
    url = request.form['url']
    sf = {"song": song,"url": url}
    q.put(sf)
    for elem in list(q.queue):
        print elem
    return "Great choice ;) Thanks for submitting: " + song

# Global Queue
q = Queue()

if __name__ == '__main__':
    app.run()
