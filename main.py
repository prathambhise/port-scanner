# This is a python script.
# Author: PRATHAM BHISE
# This python script is used to scan TCP ports.

"""Imports-> PortScanner from port_scanner.py"""

from port_scanner import PortScanner


if __name__ == "__main__":
    # help(PortScanner)
    ps1 = PortScanner()

    try:
        ps1.ps_run()
    except (KeyboardInterrupt, SystemExit):
        exit()
