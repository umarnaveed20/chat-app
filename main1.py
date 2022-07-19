# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

HOST = '127.0.0.1'
PORT = 1234

DARK_GREY = '#000000'
MEDIUM_GREY = '#000000'
OCEAN_BLUE = '#000000'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


main = tk.Tk()
main.geometry("600x600")
main.title("CHAT APP -Add User")
main.resizable(False, False)

main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=4)
main.grid_rowconfigure(2, weight=1)

l1 = tk.Label(main,text='Upload Profile Picture',width=30,font=FONT)  
l1.pack(side=TOP)
b1 = tk.Button(main, text='Upload Files', 
   width=20,command = lambda:upload_file())
b1.pack(side=TOP)
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=False,filetypes=f_types)
    print(filename)
    img=Image.open(filename) # read the image file
    img=img.resize((200,200)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(main)
    e1.pack(side=TOP)
    e1.image = img
    e1['image']=img # garbage collection 
 
# main function
def main():
    

    main.mainloop()
