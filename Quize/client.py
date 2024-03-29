
import socket

# Define the host and port to connect to (server's IP address)
HOST = '192.168.137.1'  # Replace 'server_ip_address' with the actual IP address of the server device
PORT = 5002
print("hello bro")

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    print("Connected to server at", HOST, "port", PORT)
    # Send data to the server
    s.sendall(b'Hello, server')
    # Receive data from the server
    data = s.recv(1024)

print('Received:', data.decode())
