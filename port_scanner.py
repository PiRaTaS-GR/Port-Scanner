import socket
import sys
import threading
import pyfiglet
from colorama import Fore, init


init()


logo = pyfiglet.figlet_format("PiRaTaS-GR")
print(Fore.LIGHTBLUE_EX + logo)

print(Fore.LIGHTBLUE_EX + "For contact, email: piratas.gr@proton.me\n", end=Fore.RESET)


logo2 = pyfiglet.figlet_format("Port-Scanner")
print(Fore.RED + logo2)

print(Fore.YELLOW + "\n")


def check_port(host, port):
    try:
       
        sock = socket.create_connection((host, port), timeout=0.5)  
        sock.close()
        print(f"Port {port} is open")
        return True
    except (socket.timeout, socket.error):
        return False


def check_all_ports(host):
    open_ports = []
    threads = []  
    for port in range(1, 65536):  
        thread = threading.Thread(target=lambda p=port: check_port(host, p))  
        threads.append(thread)
        thread.start()

   
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    while True:
        
        host = input("Please enter the domain or IP to check (e.g. example.com or 192.168.1.1): ")

        if not host:
            print("You must enter a valid domain or IP address!")
            continue

        print(f"Checking ports for server {host}...")
        check_all_ports(host)

        
        again = input("Do you want to check another domain/IP? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting program.")
            break
