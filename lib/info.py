from . import tts
import datetime
from playsound import playsound


months= ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
def date():
    date =  (str(datetime.datetime.now()).split(" ")[0])
    date = date.split("-")
    current = date[2]+" "+months[int(date[1])] + " " + date[0]
    playsound('./Data/audio/today_Date.mp3')
    tts.tts(current)

def time():
    time =  (str(datetime.datetime.now()).split(" ")[1])
    tts.tts("time is :"+str(time))

def intro():
    tts.tts("my name is bliss and I'm your voice assistance")
    tts.tts("you can ask me for playing song , about today's date and time , search someting in google , opening aplication in your computer ,taking notes and so much more")
