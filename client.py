import socket

def client_program():
    host = socket.gethostname()
    port = 5000  

    client_socket = socket.socket()
    print("Waiting to connect to the server...")
    client_socket.connect((host, port))  

    message = ''

    while message.lower().strip() != 'bye':
        data = client_socket.recv(2048).decode()

        if 'bye' in data.lower().strip():
            print('Server: ' + data.replace('bye', ''))
            break
        
        print('Server: ' + data)
        message = input(" -> ")
        client_socket.send(message.encode())

    client_socket.close()


if __name__ == '__main__':
    client_program()