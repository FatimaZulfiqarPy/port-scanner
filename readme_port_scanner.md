# Port Scanner (Python)

A simple and beginner-friendly port scanner built with Python. This project helps you learn how to check which ports on a target machine are open. Use it only on machines or networks you own or have permission to test.


## What it does
- Scans a range of TCP ports on a target (default: 1–1024)
- Prints open ports
- Works with either a hostname (e.g. `example.com`) or an IP address (e.g. `127.0.0.1`)

## Features
- Easy to read and run
- Short timeout for faster scanning
- Friendly ASCII banner using `pyfiglet`
- Simple error handling (invalid host, network errors, user interrupt)

## Requirements
- Python 3.x
- `pyfiglet` (install with `pip install pyfiglet`)

## How to run
1. Open terminal (or VS Code terminal) in the project folder.
2. Install dependency (if not already):
   ```bash
   pip install pyfiglet
   ```
3. Run the scanner (option A: run and type target; option B: pass target as argument):
   ```bash
   # Option A - interactive
   python portscanner.py
   # then type: 127.0.0.1

   # Option B - pass target directly
   python portscanner.py 127.0.0.1
   ```

## Sample output
```
PORT SCANNER
--------------------------------------------------
Scanning Target: 127.0.0.1
Scanning started at: 2025-09-17 22:57:02
--------------------------------------------------
Port 22 is open
Port 80 is open
```

## Ethical note
Only scan machines you own or have explicit permission to test. Unauthorized scanning may be illegal and unethical.

## Author
Fatima Zulfiqar


