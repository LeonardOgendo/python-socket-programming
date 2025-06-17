import socket



def get_server_ip(domain_or_ip):
    try:
        return socket.gethostbyname(domain_or_ip)
    
    except socket.gaierror:
        print("[!] Error: Could not resolve hostname")
        return None

def main():
    # User-defined target
    target = input("Enter server domain or IP:")
    server_ip = get_server_ip(target)
    port = 4444

    if server_ip:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                print(f"[+] Connecting to {server_ip}:{port}")
                client_socket.connect((server_ip, port))

                # send message to the server
                message = "Connected! Hello server!"
                client_socket.send(message.encode())

                ## Receive server response
                response = client_socket.recv(1024).decode()
                print(f"[+] Server says: {response}")
        
        except ConnectionRefusedError:
            print("[!] Connection failed. Is the server running?")
        
        except socket.timeout:
             print("[!] Connection timed out.")
        
        except Exception as e:
            print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    main()