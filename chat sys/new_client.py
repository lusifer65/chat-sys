import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=str(socket.gethostbyname("localhost"))
port=7777
client.connect((host,port))
while True:
    message=client.recv(1024)
    print(message.decode())
    if(message.decode()=='bye'):
        client.send("bye".encode('ascii'))
        client.close()
    else:
        client.send(input("enter messaage:-\t").encode('ascii'))
        print("message sent....")

    
