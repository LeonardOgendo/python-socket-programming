import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4444))

server_socket.listen(1)
print("[+] Listening for incoming TCP connections on port 444..")

try:
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"[+] Connection received from {client_address[0]}:{client_address[1]}")

        data = client_socket.recv(1024).decode()
        print(f"[+] Received from client: {data}")

        client_socket.send("Connected! Hello Client".encode())

        # Close the connection to this client only
        client_socket.close()

except KeyboardInterrupt:
    print("\n[!] Server shutting down")
    server_socket.close()