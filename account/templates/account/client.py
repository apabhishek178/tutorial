import socket

def Main():
    host = '128.199.126.171'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    message = input("->")
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Recieved from service: " +data)
        message = input("->")
    s.close()

if __name__ == '__main__':
    Main()
