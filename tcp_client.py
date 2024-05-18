import socket

target_host ="localhost"
target_port=9998

#creating a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connet the client 

client.connect((target_host,target_port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")


#receive some data

response = client.recv(4096)

print(response)