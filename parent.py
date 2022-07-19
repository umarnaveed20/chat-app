
# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from main import *
from client import *
from server import *

HOST = '127.0.0.1'
PORT = 1234

DARK_GREY = '#000000'
MEDIUM_GREY = '#000000'
OCEAN_BLUE = '#000000'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.geometry("600x600")
        self.title("CHAT APP")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=1)

        self.l1 = tk.Label(self,text='REAL TIME CHAT',height=10,font=FONT)  
        self.l1.pack(side=TOP)
        #l1.grid(row = 0, column = 2, pady = 2,padx=200)
        self.b1 = tk.Button(self, text='Start Chat',width=20,height=3,command = lambda:self.StartChat())
        self.b1.pack(side=TOP)
        #b1.grid(row = 1, column = 2, padx = 200)
        self.b2 = tk.Button(self, text='Add User',width=20,height=3,command = lambda:self.AddUser())
        #b1.grid(row = 2, column = 2,  padx = 200)
        self.b2.pack(side=TOP)  
    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')
    def StartChat():
        pass
    def AddUser():
    
        main()

if __name__ == "__main__":
  app = HomeScreen()
  app.mainloop()
