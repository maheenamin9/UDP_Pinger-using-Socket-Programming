import socket
socketcreat = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socketcreat.bind(("127.0.0.1", 5090))
print("Server is waiting for client's request...\n")

while True:
    data, address = socketcreat.recvfrom(1024)
    data = data.decode()
    print(f"Client: {data}")
    response = "pong"
    socketcreat.sendto(response.encode(), address)
