import selectFile
import datetime
import getQuery
import tts

""" use add app to add application which is accessable by your voice assistance"""

def addApp():
        add = selectFile.selectFile()
        name = input("enter application name\n")
        file = open('./Data/applications.txt','a+')
        file.write(name +'$$'+ add+"\n")

def addMusic():
        add = selectFile.selectFile()
        name = input("enter music file name\n")
        file = open('./Data/musics/music.txt','a+')
        file.write(name +"$$"+ add+"\n")

def addToDoNotes():
        date = str(datetime.datetime.now()).split(" ")[0]
        while(True):
                tts.tts("what is the title of the ToDo Note ?")
                title = getQuery.getQuery()
                tts.tts('is title final')
                flag = getQuery.getQuery()
                if(flag == 'yes'):
                        tts.tts("please input the description..")
                        desc = input('write your description here')
                        print('saving...')
                        file = open('./Data/notes/notes{}.txt'.format(date),'w+')
                        file.write(title+" $$ "+desc)
                        file.close()
                        break

def list(filename):
        if('notes' in filename):
                fileDir = "./Data/notes/"+filename
        if('music' in filename):
                fileDir = "./Data/"+filename
        if('applications' in filename):
                fileDir = "./Data/"+filename

        title = []
        desc = []
        with open(fileDir) as file:
                data = file.readlines()
                for line in data:
                        info = line.split('$$')
                        title.append(info[0])
                        desc.append(info[1])
                
                for i in range(0,len(title)):
                        print(50*'-')
                        print("({})".format(i+1),title[i]+":\n")
                        print(desc[i],"\n")
                        print(50*'-')


def showToDoNotes():
        print("TODO NOTES")
        date = str(datetime.datetime.now()).split(" ")[0]
        list('notes{}.txt'.format(date))
def showMusic():
        list('music.txt')
def showApplications():
        list('applications.txt')
            




        