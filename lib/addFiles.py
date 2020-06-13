from . import selectFile
import datetime
from . import Query
from . import tts
import pymongo

try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
except:
        print("error connecting with database")

db = client["voice_assistant"]

""" use add app to add application which is accessable by your voice assistance"""

def addApp():
        collection = db['apps']
        add = selectFile.selectFile()
        print(add)
        if(add != ""):
                name = input("enter application name\n")
                ret = collection.insert_one({name:add})
                print(ret,end="\n")
        

def addMusic():
        add = selectFile.selectFile()
        if(add != ""):
                name = input("enter music file name\n")
                collection = db['musics']
                ret = collection.insert_one({name:add})
                print(ret,"\n")


def addToDoNotes():
        date = str(datetime.datetime.now()).split(" ")[0]
        while(True):
                tts.tts("what is the title of the ToDo Note ?")
                title = Query.getQuery()
                tts.tts('is title final')
                flag = Query.getQuery()
                if(flag == 'yes'):
                        tts.tts("please input the description..")
                        desc = input('write your description here')
                        print('saving...')

                        collection = db["notes"]
                        ret = collection.insert_one({title:desc,"date":date})
                        print(ret,end="\n")

                        break


def toList(coll_name):
        l = []
        try:
                collection = db[coll_name]
        except :
                print("no connection with database")
        for res in collection.find({},{"_id":0}):
                l.append(res)
        return l
def delete(coll_name,filters):
        try:
                collection = db[coll_name]
        except:
                print("no connection with database")
        ack = collection.delete_one(filter = filters)
        print(ack)


def showToDoNotes():
        print("TODO NOTES")
        todo_list = toList('notes')
        print(todo_list)
def showMusics():
        musics = toList('musics')
        print(musics)
def showApps():
        apps = toList('apps')
        print(apps)     

def handleFiles(string):
        if('add' in string):
                if('notes' in string):
                        addToDoNotes()
                if('musics' in string):
                        addMusic()
                if('app' in string):
                        addApp()
        if('display' in string):
                if('notes' in string):
                        showToDoNotes()
                if('musics' in string):
                        showMusics()
                if('app' in string):
                        showApps()




        