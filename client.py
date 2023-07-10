#!/bin/python

import socket
import sys
import json
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    connecting()

def connecting():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(ADDR)
    
    data()
    client.close()

def data():
    with open("./client_config.json", 'r') as json_file:   
        json_data = json.load(json_file)
        i=1
        while True:
            try :
                file_name = json_data['filename'][f"{i}"]
            except:
                break
            fd = open(file_name, 'rt', encoding='utf-8')
            file_data = None
            while file_data != '' :  
                file_data = fd.readline()
                if sys.getsizeof(file_data) == 49:
                    break
                msg = file_name+';'+file_data
                sending(msg)
            i=i+1

def sending(msg):
    data = msg.encode(FORMAT)
    length = len(data)
    if length == 0:
        return False

    client.send(length.to_bytes(4, byteorder="little"))
    client.send(data)

if __name__ == '__main__':
    main()
