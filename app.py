from flask import Flask
from flask import request
from flask import render_template
from Queue import Queue
from database import psqldatabase
import threading
import time

app = Flask(__name__)

# Global Queue
q = Queue()

#db = psqldatabase()

@app.route('/')
def render_home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    song = request.form['song']
    url = request.form['url']
    #cleanurl = db.FORMAT_URL()
    sf = {"song": song,"url": url}
    q.put(sf)
    return "Great choice ;) Thanks for submitting: " + song


class flaskThread (threading.Thread):
   def __init__(self, threadID, name, appName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.appName = appName
   def run(self):
      self.appName.run()

class queueThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        # Infinite while loop to continuously check for new songs in queue
        while True:
            count = 10
            # Temporarily using count to imitate waiting for song to complete
            while count != 0:
                print count
                time.sleep(1)
                count -= 1
            if not q.empty():
                nextsong = q.get()
                url = str(nextsong['url'])
                print nextsong
            else:
                print "Queue is empty"

# Create new threads
flaskthread = flaskThread(1, "mainflask", app)
queuethread = queueThread(2, "mainqueue")

# Start new Threads
flaskthread.start()
queuethread.start()
