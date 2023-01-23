import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9999))
        
clientLoop = True
while clientLoop:
    msg = s.recv(9999)
    print(msg.decode("utf-8"))
    print("Python DB Menu")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit")
    
    userInput = input("Choice")
    s.send(bytes(userInput, "utf-8"))

    match userInput:
        case "1":
            name = input("Name:")
            s.send(bytes(name, "utf-8"))
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "2":
            print("Enter info")
            name = input("Name:")
            s.send(bytes(name, "utf-8"))
            age = input("Age:")
            s.send(bytes(age, "utf-8"))
            address = input("Address:")
            s.send(bytes(address, "utf-8"))
            number = input("Number:")
            s.send(bytes(number, "utf-8"))
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "3":
            name = input("Customer Name:")
            s.send(bytes(name, "utf-8"))
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "4":
            name = input("Customer Name:")
            s.send(bytes(name, "utf-8"))
            age = input("New Customer Age:")
            s.send(bytes(age, "utf-8"))
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "5":
            name = input("Customer Name:")
            s.send(bytes(name, "utf-8"))
            address = input("New Address:")
            s.send(bytes(address, "utf-8"))
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "6":
            name = input("Name:")
            s.send(bytes(name, "utf-8"))
            number = input("New number:")
            s.send(bytes(number, "utf-8"))
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "7":
            data = s.recv(9999)
            print(data.decode("utf-8"))

        case "8":
            clientLoop = False
            print("Program exited")

        case _:
            print("Input something again")










    
    
