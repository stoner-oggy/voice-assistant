import sys
from playsound import playsound
from lib import addFiles

from lib import Query
# from lib import Query
import sys

def main():
    while(True):
        sys.stdout.flush()
        flag  = input("enter start or exit\n")
        if(flag=='exit'):
            break
        playsound('./Data/audio/welcomeGreeting.mp3')
        try:
            query = Query.getQuery()
        except:
            print("ERROR : Seems like you are offline")
        
        Query.handleQuery(query)
        
if __name__ == "__main__":
    main()



# you can ask for google search  example: search something
# you can ask for todays date or time example: what is today's date , what is the time now
# you can do much more 