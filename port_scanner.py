# This is a python script.
# Author: PRATHAM BHISE
# This python script is used to scan TCP ports.

"""Imports-> datetime module as dt; tqdm module; threading module; socket module; time module; pyfiglet module; sys module"""

from datetime import datetime as dt
from ports_dict import ports_dict
from tqdm import tqdm
import threading
import pyfiglet
import socket
import sys


class PortScanner:
    def __init__(self) -> None:
        """
            Initialise instance for PortScanner class.

            :return: None
        """
        self.ps_target = "localhost"
        self.host_name = socket.gethostname()
        self.host = socket.gethostbyname(socket.gethostname())
        self.ports_scanned = 0
        self.ports_open = 0
        self.available = []

    def ps_run(self) -> None:
        """
            Commencement method for instance of PortScanner.

            :return: None
        """
        self.ps_welcome()
        self.ps_get_details()
        self.ps_connect()

    def ps_welcome(self) -> None:
        """
            Print welcome message.

            :return: None
        """
        ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
        print(ascii_banner)
        print(f"POSSIBLE HOST NAME       : {self.host_name}")
        print(f"POSSIBLE HOST IP ADDRESS : {self.host}")

    def ps_get_details(self) -> None:
        """
            Accept target details from user.

            :return: None
        """
        try:
            self.ps_target = input(str("TARGET IP: "))
        except KeyboardInterrupt:
            self.quit()
        print("_" * 50)
        print("Scanning Target:", self.ps_target)
        print("Scanning Started At" + self.timestamp())
        print("_" * 50)

    def ps_connect(self) -> None:
        """
            Create multiple threads for scanning individual ports.

            :return: None
        """
        print("\nScanning In Progress...")
        try:
            for port in tqdm(range(1, 65535)):
                current_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                curt_thread = threading.Thread(target=self.ps_new_thread, args=(current_socket, port), daemon=True)
                curt_thread.start()
                self.ports_scanned += 1
        except KeyboardInterrupt:
            self.quit()
        except socket.error:
            print("Host not responding")
            self.quit()
        finally:
            print()
            print("_" * 50)
            print("Scanning Target:", self.ps_target)
            print("Scanning Ended At" + self.timestamp())
            print(f"SCANNED PORTS : {self.ports_scanned}")
            print(f"OPEN PORTS    : {self.ports_open}")
            print(f"CLOSED PORTS  : {self.ports_scanned - self.ports_open}")
            print("_" * 50)
            print("State\tPort\tService")
            print("_" * 50)
            for port in self.available:
                if port in ports_dict.keys():
                    print(f"[open]\t{port}\t\t{ports_dict[port]}")
                else:
                    print(f"[open]\t{port}\t\tUnreserved Port")

    def ps_new_thread(self, curt_socket, curt_port) -> None:
        """
            Bind host address and port number to the socket.

            :param curt_socket: socket
            :param curt_port: int
            :return: None
        """
        try:
            sock_return_code = curt_socket.connect_ex((self.ps_target, curt_port))
            if sock_return_code == 0:
                self.available.append(curt_port)
                # print(f"\n[*] Port {curt_port} is open.\n")
                self.ports_open += 1
            # else:
            #     print(f"[*] Port {curt_port} is closed, return code: {sock_return_code}")
            curt_socket.close()
        except socket.error:
            print("Host not responding")
            self.quit()
        except KeyboardInterrupt:
            self.quit()

    @staticmethod
    def timestamp() -> str:
        """
            Return current date and time.

            :type: staticmethod
            :return: str
        """
        date = dt.now().date()
        hour = dt.now().time().hour
        minute = dt.now().time().minute
        return f":{date} | {hour}:{minute}"

    @staticmethod
    def quit() -> None:
        """
            End the script.

            :type: staticmethod
            :return: None
        """
        print("\nExiting")
        sys.exit()

