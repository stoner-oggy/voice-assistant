import tts
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

date()