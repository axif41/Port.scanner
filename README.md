🔎 Network Port Scanner

A Python-Based TCP Port Scanner (Educational Purpose Only)

📌 Overview

The Network Port Scanner is a Python-based command-line tool designed to demonstrate how TCP socket connections work in networking.

This project scans specified ports on a target IP address, determines whether they are open or closed, performs basic banner grabbing on open ports, and displays formatted results.

⚠️ This tool is intended strictly for educational and authorized security testing purposes.

🚀 Features

Scan a single IP address

Scan specific ports or a port range

Identify open and closed ports

Perform basic banner grabbing on open ports

Display results in clean, table-formatted output

Count total open ports

Save scan results to a file

Adjustable timeout option

No external dependencies (uses Python's built-in socket module)

🛠 Tech Stack

Python 3.x

Built-in socket module

Built-in argparse module

Built-in datetime module

📂 Project Structure
network-port-scanner/
│
├── port_scanner.py
├── README.md
└── output.txt (generated after scan)

⚙️ Installation
1️⃣ Install Python



2️⃣ Clone Repository
git clone https://github.com/yourusername/network-port-scanner.git
cd network-port-scanner

3️⃣ No Additional Dependencies

This project uses only built-in Python modules.
No need to install external packages.

▶️ How to Use (Step-by-Step Process)
🔹 Basic Scan
python port_scanner.py -i 192.168.1.1


This will scan default ports.

🔹 Scan Specific Ports
python port_scanner.py -i 192.168.1.1 -p 22,80,443

🔹 Scan a Port Range
python port_scanner.py -i 192.168.1.1 -p 1-1000

🔹 Set Custom Timeout
python port_scanner.py -i 192.168.1.1 -p 1-1000 -t 2

🔹 Save Output to File
python port_scanner.py -i 192.168.1.1 -o results.txt

📊 Example Output
----------------------------------------
Port     Status     Service/Banner
----------------------------------------
22       OPEN       OpenSSH 8.2
80       OPEN       Apache HTTP Server
443      CLOSED
----------------------------------------
Total Open Ports: 2
Scan Completed in 4.52 seconds

🧠 How It Works (Technical Explanation)

The program creates a TCP socket using Python’s socket module.

It attempts to establish a connection to each specified port.

If the connection succeeds → Port is marked as OPEN.

If the connection fails → Port is marked as CLOSED.

For open ports, the program attempts basic banner grabbing.

Results are formatted and displayed cleanly in the terminal.

🔐 Ethical Use & Legal Warning

⚠️ IMPORTANT — READ BEFORE USING

This tool must only be used:

On systems you personally own

On lab environments (e.g., virtual machines)

With explicit written permission from the system owner

Unauthorized port scanning may be illegal and may violate cybersecurity laws such as:

IT Act 2000 (India)

Computer Fraud and Abuse Act (USA)

Local cybercrime laws in your country

Misuse of this tool can result in:

Legal action

Criminal charges

Permanent IP blacklisting

The developer assumes NO responsibility for misuse or illegal activity.

🧪 Recommended Safe Practice Environment

To practice legally and safely, use:

Localhost (127.0.0.1)

Virtual Machines (VirtualBox / VMware)

Authorized cybersecurity labs

Personal home network (your own devices only)

Never scan:

Government websites

Corporate servers

Public infrastructure

Any system without permission

📈 Limitations

Basic TCP connect scan only

No stealth scanning

No multi-threading (if not implemented)

Not optimized for enterprise-level scanning

This tool is meant for learning networking fundamentals, not for offensive security operations.

🛣 Future Improvements

Multi-threaded scanning

Service detection improvement

OS detection

Progress indicator

Logging system

GUI version

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Your Name : ASIF PARWEZ
Backend & Cybersecurity Learner

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Commit your changes: `git commit -m "Add feature"`
5. Push to branch: `git push origin feature-name`
6. Open a Pull Request

Please make sure contributions follow **ethical use guidelines**.  
Do not include instructions for illegal scanning.


Add version number
