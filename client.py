import socket

def client_program():
    host = socket.gethostname() #Getting the host name
    port = 5000  #Server port number

    #Instantiating
    client_socket = socket.socket()
    print("Waiting to connect to the server...")
    #Connecting to the server
    client_socket.connect((host, port))  

    message = ''

    while message.lower().strip() != 'bye':
        #Receiving response from the server
        data = client_socket.recv(2048).decode()

        #If the server sends a message that contains 'bye' the connection will end :/ 
        if 'bye' in data.lower().strip():
            print('Server: ' + data.replace('bye', ''))
            break
        
        print('Server: ' + data)
        message = input(" -> ")
        #Sending message to the server
        client_socket.send(message.encode())
    #Closing the connection
    client_socket.close()


if __name__ == '__main__':
    client_program()