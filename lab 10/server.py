import socket
import threading

# Storing connected clients
clients = []

# Function to broadcast a message to all connected clients
def broadcast(message, conn):
    print("broadcasting")
    for client in clients:
        try:
            if(client != conn):
                client.send(message.encode())
        except:
            # Remove the client if the connection is broken
            clients.remove(client)


def client_thread(conn, addr):
    try:
        print(f"Connected by {addr}")
        while True:
            message = conn.recv(1024).decode()
            if not message:
                print("connection from ", addr, " closed")
                break
            print(f"Received from {addr}: {message}")
            broadcast(message, conn)
        conn.close()
    except:
        clients.remove(conn)

def start_server():
    print("server started")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

start_server()