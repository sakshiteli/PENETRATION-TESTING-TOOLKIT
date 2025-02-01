import argparse
from port_scanner import scan_ports
from brute_forcer import brute_force
import os

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("-t", "--target", help="Target IP or domain", required=True)
    parser.add_argument("-p", "--portscan", help="Run port scanner", action="store_true")
    parser.add_argument("-b", "--bruteforce", help="Run brute-force attack on login page", action="store_true")
    parser.add_argument("-u", "--username", help="Username for brute-force", default="admin")
    parser.add_argument("-w", "--wordlist", help="Path to password wordlist", default="passwords.txt")

    args = parser.parse_args()

    if args.portscan:
        ports = [22, 80, 443, 8080]  # Common ports
        scan_ports(args.target, ports)

    if args.bruteforce:
        if not os.path.isfile(args.wordlist):
            print("[!] Wordlist file not found!")
            return
        brute_force(args.target, args.username, args.wordlist)

if __name__ == "__main__":
    main()
