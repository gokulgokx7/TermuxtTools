import socket
import threading

target = input("Enter target IP or domain: ")
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    s.close()

print(f"🔎 Scanning {target}...\n")

for port in ports:
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
