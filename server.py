import socket
import re
from quicksort import quicksort as sort
from _thread import *
from datetime import datetime

def server_program():
    host = socket.gethostname()
    port = 5000 
    clients_count = 0

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen()
    print("Waiting for clients to connect...")

    def multi_thread_client(conn, count):
        conn.send(('Successfully connected to server...\nPlease enter the numbers you want to sort').encode())

        while True:
            arr = []
            data = conn.recv(2048).decode()
            arr = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', data)

            if 'bye' in data.lower().strip() or not data:
                print('Connection with client ' + str(count) + " ended")
                break

            if len(arr) != 0:
                print("Unsorted numbers of client " + str(count) + ": " + ' '.join(arr))
                sort(arr, 0, len(arr) - 1)
                print("Sorted numbers of client " + str(count) + ': ' + ' '.join(arr))
                conn.send(("Sorted numbers: "+ ' '.join(arr) + " bye").encode())
                break
            print("Client " + str(count) + ": " + str(data))
            conn.send(('Please enter the numbers you want to sort').encode())

        print("Closing connection with client " + str(count))
        conn.close()  
            
    while True:
        conn, address = server_socket.accept()  
        print("Connection made from: " + str(address) + ' at ' + str(datetime.now().time()))
        clients_count += 1
        start_new_thread(multi_thread_client, (conn, clients_count))
        print('Number of clients that connected to the server successfully since start: ' + str(clients_count))
    
    server_socket.close()


if __name__ == '__main__':
    server_program()