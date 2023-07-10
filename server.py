import socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    connecting()


def connecting():
    print("[STARTING] Server is starting.")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(ADDR)
    server.bind(ADDR)
    print(IP)
    
    server.listen()
    print("[LISTENING] Server is listening.")
    global conn
 

    
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        while True:
            if receiving() is False:
                break

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")


def receiving():
    data = conn.recv(4)
    len = int.from_bytes(data, "little")
    if len == 0:
        return False

    data = conn.recv(len)
    recv_data = data.decode(FORMAT)
    separating(recv_data) 
      
    

def separating(recv_data):
    data = recv_data.split(sep=';')

    print(data)

    if data[1] == "END_OF_FILE":
        return True
    logging(data[0], data[1])


def logging(file_name, file_data):
    fd = open(file_name + ".txt", 'a+')
    file_name = fd.writelines(file_data)
    fd.close() 

if __name__ == '__main__':
    main()
