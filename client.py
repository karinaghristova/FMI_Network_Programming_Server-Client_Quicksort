import socket

def client_program():
    host = socket.gethostname()
    port = 5000  # socket server port number

    client_socket = socket.socket()
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(2048).decode()

        if 'bye' in data.lower().strip():
            print('Server: ' + data.replace('bye', ''))
            break
        print('Server: ' + data)

        message = input(" -> ")

    client_socket.close()


if __name__ == '__main__':
    client_program()