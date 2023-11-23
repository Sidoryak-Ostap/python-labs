import socket
import threading
import json
from datetime import datetime


# Storing connected clients
clients = []

# Function to broadcast a message to all connected clients
def broadcast(message, conn):
    print("broadcasting")
    for client in clients:
        try:
            if(client != conn):
                json_data = json.dumps(message)
                client.send(json_data.encode('utf-8'))
        except:
            # Remove the client if the connection is broken
            clients.remove(client)


def client_thread(conn, addr):
    try:
        print(f"Connected by {addr}")
        while True:
            message = conn.recv(1024).decode('utf-8')
            received_dict = json.loads(message)
            print("before if")
            if not message:
                print("connection from ", addr, " closed")
                break
            print(f"Received from {addr} {received_dict['user']}: {received_dict['text']}")

            with open("server.txt", "a") as file:
                file.write(f"message: {received_dict['text']}; from: {received_dict['user']}; time: {datetime.now().time()}\n")
            broadcast(received_dict, conn)
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