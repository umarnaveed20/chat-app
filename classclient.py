# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 1234

DARK_GREY = '#000000'
MEDIUM_GREY = '#000000'
OCEAN_BLUE = '#000000'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


class Client(tk.Tk):
    def __init__(self,username="hello"):
        super().__init__()
        self.username=username
        # AF_INET: we are going to use IPv4 addresses
        # SOCK_STREAM: we are using TCP packets for communication
        self.HOST = '127.0.0.1'
        self.PORT = 1234
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # configure the root window
        self.title("Messenger Client")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=1)
##        self.top_frame = tk.Frame(self, width=600, height=100, bg=DARK_GREY)
##        self.top_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.middle_frame = tk.Frame(self, width=600, height=400, bg=MEDIUM_GREY)
        self.middle_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.bottom_frame = tk.Frame(self, width=600, height=100, bg=DARK_GREY)
        self.bottom_frame.grid(row=1, column=0, sticky=tk.NSEW)

##        self.username_label = tk.Label(self.top_frame, text="Enter username:", font=FONT, bg=DARK_GREY, fg=WHITE)
##        self.username_label.pack(side=tk.LEFT, padx=10)
##
##        self.username_textbox = tk.Entry(self.top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
##        self.username_textbox.pack(side=tk.LEFT)
##
##        self.username_button = tk.Button(self.top_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=self.connect)
##        self.username_button.pack(side=tk.LEFT, padx=15)

        self.message_textbox = tk.Entry(self.bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)
        self.message_textbox.pack(side=tk.LEFT, padx=10)

        self.message_button = tk.Button(self.bottom_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=self.send_message)
        self.message_button.pack(side=tk.LEFT, padx=10)

        self.message_box = scrolledtext.ScrolledText(self.middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)
        self.message_box.config(state=tk.DISABLED)
        self.message_box.pack(side=tk.TOP)
    def add_message(self,message):
        self.message_box.config(state=tk.NORMAL)
        self.message_box.insert(tk.END, message + '\n')
        self.message_box.config(state=tk.DISABLED)

    def connect(self):

        # try except block
        try:

            # Connect to the server
            self.client.connect((self.HOST, self.PORT))
            print("Successfully connected to server")
            self.add_message("[SERVER] Successfully connected to the server")
        except:
            self.messagebox.showerror("Unable to connect to server", f"Unable to connect to server {self.HOST} {self.PORT}")

        if self.username != '':
            self.client.sendall(self.username.encode())
        else:
            self.messagebox.showerror("Invalid username", "Username cannot be empty")

        threading.Thread(target=self.listen_for_messages_from_server, args=(self.client, )).start()

    
    def send_message(self):
        self.message = self.message_textbox.get()
        if self.message != '':
            self.client.sendall(self.message.encode())
            self.message_textbox.delete(0, len(self.message))
        else:
            self.messagebox.showerrorowerror("Empty message", "Message cannot be empty")
    

    def listen_for_messages_from_server(self,client):

        while 1:

            self.message = client.recv(2048).decode('utf-8')
            if self.message != '':
                self.username = self.message.split("~")[0]
                self.content = self.message.split('~')[1]

                self.add_message(f"[{self.username}] {self.content}")
                
            else:
                self.messagebox.showerror("Error", "Message recevied from client is empty")





##if __name__ == "__main__":
####  app = Client()
##  app.mainloop()
