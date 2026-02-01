import socket
import time
import subprocess

SERVER_IP = '127.0.0.1' # Change to server IP if on different machines

def local_compute():
    start = time.time()
    res = 0
    for i in range(10**6): res += i # Same task as server
    return time.time() - start

def offload_compute():
    try:
        start = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2) # If network is too slow, it fails
        s.connect((SERVER_IP, 5000))
        s.send(b"START")
        s.recv(1024)
        s.close()
        return time.time() - start
    except:
        return float('inf') # Network error or timeout

if __name__ == "__main__":
    t_local = local_compute()
    t_offload = offload_compute()
    
    print(f"Local Execution: {t_local:.4f}s")
    print(f"Offload Execution: {t_offload:.4f}s")
    
    if t_offload < t_local:
        print("Decision: Offloading to Edge Server")
    else:
        print("Decision: Executing Locally (Network Latency too high)")