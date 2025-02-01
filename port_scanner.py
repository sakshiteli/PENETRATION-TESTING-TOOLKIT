import socket
from concurrent.futures import ThreadPoolExecutor

def check_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open on {target}")
    sock.close()

def scan_ports(target, ports):
    print(f"Scanning ports on {target}...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda port: check_port(target, port), ports)

if __name__ == "__main__":
    target = input("Enter the target IP or domain: ")
    ports = [22, 80, 443, 8080]
    scan_ports(target, ports)
