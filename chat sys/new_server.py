import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname("localhost")
port=7777
server.bind((host,port))
print("server is bind")
server.listen(10)
print("server is listen...")
while( True):
    client,addr=server.accept()
    print("now You are connected with address {}".format(addr))
    client.send("now you are connected with server let's talk".encode('ascii'))
    while(True):
        message=client.recv(1024)
        if(message.decode('ascii')=='bye'):
            client.send('bye'.encode('ascii'))
            print('bye\n chat ended....')
            break
        else:
            print(message.decode('ascii'))
            client.send(input(("enter the message\t")).encode('ascii'))
    client.close()
