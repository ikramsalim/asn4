import socket


def socket_server():
    # Get hostname
    # host = '0.0.0.0'
    # port = 54321
    host = socket.gethostname()
    # Give port
    port = 8080

    # Instance of server
    chat_server = socket.socket()
    # bind host address and port together
    chat_server.bind((host, port))

    # Configure the number of clients
    chat_server.listen(2)
    print("Server running on host: ", host, "🚀")

    # Server accepts new connection
    conn, address = chat_server.accept()

    print("Connection from: " + str(address))
    while True:
        # receive data stream
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        # Send data to the client
        conn.send(data.encode())
    # Close the connection
    conn.close()


if __name__ == '__main__':
    socket_server()
