import socket
import re
from quicksort import quicksort as sort

def server_program():
    host = socket.gethostname()
    port = 5000 

    server_socket = socket.socket()
    server_socket.bind((host, port))  # binding host address and port together

    server_socket.listen()
    conn, address = server_socket.accept()  # accepting new connection
    print("Connection made from: " + str(address))
    arr = []
    while True:
        data = conn.recv(2048).decode()
        arr = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', data)
       
        if len(arr) != 0:  #won't stop until the client gives numbers to be sorted
            print("Client: " + ' '.join(arr))
            sort(arr, 0, len(arr) - 1)
            print("Sorted numbers: " + ' '.join(arr))
            conn.send(("Sorted numbers: " + ' '.join(arr) + " bye").encode())
            
            break
        print("Client: " + str(data))
        conn.send(('Please enter the numbers you want to sort').encode())
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()