def find(name):
    f = open("data.txt")
    lines = f.readlines()
    data = ""
    for line in lines:
        if name in line:
            data = line
    f.close()
    if data == "":
        return "Customer does not exist"
    else:
        return data

def delete(name):
    f = open("data.txt", "r")
    lines = f.readlines()
    data = ""
    for line in lines:
        if name in line:
            data = line
    f.close()
    if data == "":
        return "Customer does not exist"
    else:
        f = open("data.txt", "w")
        for line in lines:
            if line != data:
                f.write(line)
        f.close()
        return "Customer deleted"

def update(name, type, change):
    f = open("data.txt")
    lines = f.readlines()
    for line in lines:
        if name in line:
            data = line
    if data == "":
        return "Customer does not exist"
    else:
        dataList = data.split("|")
        match type:
            case "age":
                delete(name)
                add(name, change, dataList[2], dataList[3])
            case "addr":
                delete(name)
                add(name, dataList[1], change, dataList[3])
            case "number":
                delete(name)
                add(name, dataList[1], dataList[2], change)
        return "Customer updated"

def add(name, age, address, number):
    f = open("data.txt")
    lines = f.readlines()
    data = ""
    for line in lines:
        if name in line:
            data = line
    f.close()
    if data == "":
        data = name + "|" + age + "|" + address + "|" + number
        f = open("data.txt", "w")
        for line in lines:
            if line != '\n':
                f.write(line)
        f.write(data + "\n")
        f.close()
        return "Customer added"
    else:
        return "Customer exists"