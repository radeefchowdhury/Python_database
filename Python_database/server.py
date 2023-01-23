import socket
from functions import *

while True:
    try:
        clientsocket.send(bytes("Working", "utf-8"))
        input = clientsocket.recv(9999).decode("utf-8")
        match input:
            case "1":
                name = clientsocket.recv(9999).decode("utf-8")
                data = str(find(name))
                clientsocket.send(bytes(data, "utf-8"))
            case "2":
                name = clientsocket.recv(9999).decode("utf-8")
                age = clientsocket.recv(9999).decode("utf-8")
                address = clientsocket.recv(9999).decode("utf-8")
                number = clientsocket.recv(9999).decode("utf-8")
                data = str(add(name, age, address, number))
                clientsocket.send(bytes(data, "utf-8"))
            case "3":
                name = clientsocket.recv(9999).decode("utf-8")
                data = str(delete(name))
                clientsocket.send(bytes(data, "utf-8"))
            case "4":
                name = clientsocket.recv(9999).decode("utf-8")
                change = clientsocket.recv(9999).decode("utf-8")
                data = str(update(name, "age", change))
                clientsocket.send(bytes(data, "utf-8"))
            case "5":
                name = clientsocket.recv(9999).decode("utf-8")
                change = clientsocket.recv(9999).decode("utf-8")
                data = str(update(name, "addr", change))
                clientsocket.send(bytes(data, "utf-8"))

            case "6":
                name = clientsocket.recv(9999).decode("utf-8")
                change = clientsocket.recv(9999).decode("utf-8")
                data = str(update(name, "number", change))
                clientsocket.send(bytes(data, "utf-8"))
            case "7":
                f = open("data.txt", 'r')
                content = f.read()
                clientsocket.send(bytes(content, "utf-8"))

    except:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 9999))
        s.listen(5)
        clientsocket, address = s.accept()
        print("Connected")