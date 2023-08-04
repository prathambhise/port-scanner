# This is a python script.
# Author: PRATHAM BHISE
# This python script is used to scan TCP ports.

"""Imports-> PortScanner from port_scanner.py"""

from port_scanner import PortScanner
import getopt
import sys

if __name__ == "__main__":
    # help(PortScanner)

    arguments = sys.argv[1:]
    opts, args = [], []

    try:
        opts, args = getopt.getopt(arguments, "t:", ["target="])
    except getopt.GetoptError as err:
        print(err)
    target_ip = "localhost"
    for opt, arg in opts:
        if opt in ("-t", "--target"):
            target_ip = arg
        else:
            print("insufficient arguments, try:\n"
                  "python3 main.py -t [target ip]\n"
                  "python3 main.py --target [target ip]")

    ps1 = PortScanner(target_ip)

    try:
        ps1.ps_run()
    except (KeyboardInterrupt, SystemExit):
        exit()
