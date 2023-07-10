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
    
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(ADDR)
    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)
    print(IP)
    
    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")
    global conn
 

    
    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        while True:
            if receiving() is False:
                break



        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")


def receiving():
    """ Receiving the filename, filedata from the client. """
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
