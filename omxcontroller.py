import os

def PLAY(URL):
    playurl = os.popen('youtube-dl -g -f mp4 ' + URL).read()
    OMXPlayer(playurl)

PLAY('https://youtu.be/ZqtyQuXo9zM')
