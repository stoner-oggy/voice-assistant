""" one function module  "selectFile()"
    you can use selectFile() function for importing file from file system
"""
from tkinter import Tk
from tkinter import filedialog

def selectFile():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("select file","*.*"),("all files","*.*")))
    root.destroy()
    print (root.filename)
    return root.filename