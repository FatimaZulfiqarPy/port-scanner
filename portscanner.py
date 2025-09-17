# Port Scanner 
# Purpose: Scan common ports on a target machine to see which ports are open.
# Use this only on machines/networks you own or have permission to test.

import pyfiglet
import sys
import socket
from datetime import datetime

# Print a small ASCII banner to make the output friendlier
print(pyfiglet.figlet_format("PORT SCANNER"))

# --- Get the target ---
# If user passed an argument (when running from terminal) use it,
# otherwise ask the user interactively (good for Jupyter or direct runs).
if len(sys.argv) == 2:
    target_input = sys.argv[1]
else:
    target_input = input("Enter target hostname or IP (e.g. 127.0.0.1): ").strip()

# Convert hostname to IPv4 address (or verify the IP). If it fails, stop.
try:
    target = socket.gethostbyname(target_input)
except Exception as e:
    print(f"Could not resolve '{target_input}': {e}")
    sys.exit(1)

# Print basic info for the user
print("-" * 50)
print("Scanning Target:", target)
print("Scanning started at:", datetime.now())
print("-" * 50)

# --- Port scanning loop ---
# We scan ports 1..1024 here. Change the range if you need other ports.
try:
    for port in range(1, 1025):
        # Create a TCP socket for each port check
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a short timeout so the scan doesn't wait too long for each port
        s.settimeout(0.5)

        # connect_ex returns 0 when the connection succeeds (port is open)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")

        # Close the socket after the check to free resources
        s.close()

# Helpful messages for common error cases
except KeyboardInterrupt:
    print("\nExiting Program (user interrupt).")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nServer not responding.")
    sys.exit()

# End of script Good bye
