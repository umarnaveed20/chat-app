# Import required modules
# import required modules
import socket
import threading

class Server():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 1234 # You can use any port between 0 to 65535
        self.LISTENER_LIMIT = 5
        self.active_clients = [] # List of all currently connected users
    # Function to listen for upcoming messages from a client

    def listen_for_messages(self,client, username):
        while 1:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                
                final_msg = username + '~' + message
                self.send_messages_to_all(final_msg)

            else:
                print(f"The message send from client {username} is empty")


    # Function to send message to a single client
    def send_message_to_client(self,client, message):
        client.sendall(message.encode())

    # Function to send any new message to all the clients that
    # are currently connected to this server
    def send_messages_to_all(self,message):
        
        for user in self.active_clients:

            self.send_message_to_client(user[1], message)

    # Function to handle client
    def client_handler(self,client):
        
        # Server will listen for client message that will
        # Contain the username
        while 1:

            username = client.recv(2048).decode('utf-8')
            if username != '':
                self.active_clients.append((username, client))
                prompt_message = "SERVER~" + f"{username} added to the chat"
                self.send_messages_to_all(prompt_message)
                break
            else:
                print("Client username is empty")

        threading.Thread(target=self.listen_for_messages, args=(client, username, )).start()

    # Main function
    def main(self):

        # Creating the socket class object
        # AF_INET: we are going to use IPv4 addresses
        # SOCK_STREAM: we are using TCP packets for communication
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Creating a try catch block
        try:
            # Provide the server with an address in the form of
            # host IP and port
            server.bind((self.HOST, self.PORT))
            print(f"Running the server on {self.HOST} {self.PORT}")
        except:
            print(f"Unable to bind to host {self.HOST} and port {self.PORT}")

        # Set server limit
        server.listen(self.LISTENER_LIMIT)

        # This while loop will keep listening to client connections
        while 1:

            client, address = server.accept()
            print(f"Successfully connected to client {address[0]} {address[1]}")

            threading.Thread(target=self.client_handler, args=(client, )).start()


if __name__ == '__main__':
    o=Server()
    o.main()
