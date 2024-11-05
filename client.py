import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1255
s.connect((host,port))

msg=input("Enter a message :")
s.send(msg.encode())
print("message sent !!")

with open('sample.txt','rb') as file:
    data=file.read(1024)
    while data:
        s.send(data)
        data=file.read(1024)
print("file sent successfully")
s.close()
