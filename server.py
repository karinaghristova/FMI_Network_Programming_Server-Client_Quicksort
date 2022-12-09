import socket
import re
from quicksort import quicksort as sort
from _thread import *
from datetime import datetime

def server_program():
    host = socket.gethostname() #Getting the host name
    port = 5000 #Inititating port
    clients_count = 0

    #Instantiating
    server_socket = socket.socket() 
    #Binding the port and the host address
    server_socket.bind((host, port)) 
    #Starting to listen for connections
    server_socket.listen() 
    print("Waiting for clients to connect...")

    def multi_thread_client(conn, count):
        """
        This function connects every client from the address provided by the server simultaneously
        """
        #Informing the client that the connection was successfull and asking him to enter numbers
        conn.send(('Successfully connected to server...\nPlease enter the numbers you want to sort').encode())

        while True:
            arr = []
            #Getting the message sent by the client 
            #(Will not accept data packet larger than 2048, no specific reason for the number, just chose it, you can always change it)
            data = conn.recv(2048).decode()
            #Extracting all the numbers from the client's message with the help of reggular expression
            arr = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', data)

            #Checking if the client ended the connection by saying bye
            if 'bye' in data.lower().strip() or not data:
                print('Connection with client ' + str(count) + " ended")
                break
            
            #Checking to see if the client gave any numbers to be sorted
            if len(arr) != 0:
                print("Unsorted numbers of client " + str(count) + ": " + ' '.join(arr))
                #Sorting the numbers using quicksort
                sort(arr, 0, len(arr) - 1)
                print("Sorted numbers of client " + str(count) + ': ' + ' '.join(arr))
                #Sending the result after sorting the numbers to the client and also sending 'bye' to end the connection
                conn.send(("Sorted numbers: "+ ' '.join(arr) + " bye").encode())
                break

            #If the client didn't enter numbers we display the message that was sent instead
            print("Client " + str(count) + ": " + str(data))
            #Again asking the client to enter numbers because we're only interested in sorting them. Not here to talk nonsense :/
            conn.send(('Please enter the numbers you want to sort').encode())

        print("Closing connection with client " + str(count))
        #Closing the connection
        conn.close()  
            
    while True:
        #Accepting new connection
        conn, address = server_socket.accept()  
        print("Connection made from: " + str(address) + ' at ' + str(datetime.now().time()))
        clients_count += 1
        #Handling the connection
        start_new_thread(multi_thread_client, (conn, clients_count))
        print('Number of clients that connected to the server successfully since start: ' + str(clients_count))
    
    server_socket.close()


if __name__ == '__main__':
    server_program()