from flask import Flask
from flask import request
from flask import render_template
from Queue import Queue
import threading

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

class flaskThread (threading.Thread):
   def __init__(self, threadID, name, appName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.appName = appName
   def run(self):
      self.appName.run()
      
# Create new threads
flaskthread = flaskThread(1, "mainflask", app)

# Start new Threads
flaskthread.start()
