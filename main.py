import time
import pyautogui as p
import random
import webbrowser

for i in range (100) :
    sites = random.choice([ 'youtube.com','youtube.com'])
    visit = 'https://youtu.be/1005WB0A6lc'. format(sites)
    webbrowser . open(visit)
    time.sleep(1)
