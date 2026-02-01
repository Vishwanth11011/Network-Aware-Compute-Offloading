import socket
import time

def heavy_computation():
    # Simulates a compute-heavy task
    res = 0
    for i in range(10**6):
        res += i
    return res

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen(5)
print("Edge Server is running on port 5000...")

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    if data == b"START":
        result = heavy_computation()
        conn.send(str(result).encode())
    conn.close()