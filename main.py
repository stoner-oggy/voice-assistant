from playsound import playsound
from bin import Query
import sys
def main():
    while(True):
        sys.stdout.flush()
        flag  = input("enter start or exit\n")
        if(flag=='exit'):
            break
        playsound('./Data/audio/welcomeGreeting.mp3')
        query = Query.getQuery()
        Query.handleQuery(query)

if __name__ == "__main__":
    main()