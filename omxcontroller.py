from omxplayer.player import OMXPlayer
from time import sleep
import os
import subprocess

def PLAY(url):
    proc = subprocess.Popen(['youtube-dl','-f','mp4', '-g', url], stdout=subprocess.PIPE)
    realurl = proc.stdout.read()
    player = OMXPlayer(realurl.decode("utf-8", "strict")[:-1])

PLAY('')
