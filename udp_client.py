import socket

target_host = "127.0.0.1"
target_port = 80

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send some data
    client.sendto(b"this is test data", (target_host, target_port))

    # Receive some data
    data, addr = client.recvfrom(4096)
    print(data)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket
    client.close()
