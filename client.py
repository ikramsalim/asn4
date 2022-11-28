import socket


def socket_client():
    # Get hostname
    #

    # host = socket.gethostname()
    host = input("hostname: ")
    # Port
    port = 8080
    # instantiate
    chat_client = socket.socket()
    # connect to the server  
    chat_client.connect((host, port))
    # take input
    message = input(" -> ")
    while message.lower().strip() != 'bye':
        # send message
        chat_client.send(message.encode())
        # receive response
        data = chat_client.recv(1024).decode()
        # show in terminal
        print('Received from server: ' + data)
        # again take input 
        message = input(" -> ")
        # close the connection
    chat_client.close()


if __name__ == '__main__':
    socket_client()
