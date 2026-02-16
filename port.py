import socket
import argparse
import time
from datetime import datetime

# Function to scan a single port on a given IP
def scan_port(ip, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((ip, port))  # 0 if port is open
        if result == 0:
            try:
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    return f"Open (Banner: {banner[:50]}...)"
                else:
                    return "Open (No banner)"
            except:
                return "Open (Banner grab failed)"
        else:
            return "Closed"
    except socket.error as e:
        return f"Error: {str(e)}"
    finally:
        sock.close()

# Function to scan multiple ports and print/save results
def scan_ports(ip, ports, timeout=1, save_file=None):
    print(f"\n🔍 Scanning {ip} for {len(ports)} ports...")
    print(f"Started at: {datetime.now()}")
    print("=" * 70)
    print(f"{'Port':<8} {'Status':<20} {'Details'}")
    print("=" * 70)

    open_ports = []
    results = []

    for port in ports:
        status = scan_port(ip, port, timeout)
        details = "" if "Closed" in status or "Error" in status else status.split('(', 1)[1].rstrip(')')
        print(f"{port:<8} {status.split('(')[0].strip():<20} {details}")
        results.append(f"Port {port}: {status}")
        if "Open" in status:
            open_ports.append(port)
        time.sleep(0.05)  # small delay

    print("=" * 70)
    print(f"Scan completed at: {datetime.now()}")
    print(f"Total open ports: {len(open_ports)}")
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("Open ports: None")

    if save_file:
        try:
            with open(save_file, 'w') as f:
                f.write(f"Port Scan Results for {ip}\n")
                f.write(f"Scanned at: {datetime.now()}\n")
                f.write(f"Total open ports: {len(open_ports)}\n\n")
                f.writelines([line + '\n' for line in results])
            print(f"Results saved to {save_file}")
        except Exception as e:
            print(f"Error saving to file: {e}")

# Main function to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="Simple Network Port Scanner")
    parser.add_argument("-i", "--ip", required=True, help="Target IP or domain (e.g., 192.168.1.1 or google.com)")
    parser.add_argument("-p", "--ports", help="Comma-separated list of ports (e.g., 80,443,22)")
    parser.add_argument("-r", "--range", help="Port range (e.g., 1-100)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout in seconds (default: 1.0)")
    parser.add_argument("-s", "--save", help="Save results to a file (e.g., results.txt)")
    args = parser.parse_args()

    # Resolve domain to IP
    try:
        target_ip = socket.gethostbyname(args.ip)
    except socket.gaierror:
        print("❌ Error: Invalid IP address or domain.")
        return

    # Parse ports
    ports = []
    if args.ports:
        try:
            ports = [int(p.strip()) for p in args.ports.split(',')]
        except ValueError:
            print("❌ Error: Invalid port list. Use comma-separated integers.")
            return
    elif args.range:
        try:
            start, end = map(int, args.range.split('-'))
            if start > end or start < 1 or end > 65535:
                raise ValueError
            ports = list(range(start, end + 1))
        except ValueError:
            print("❌ Error: Invalid port range. Use format like 1-100.")
            return
    else:
        print("❌ Error: Specify ports with -p or -r.")
        return

    # Perform scan
    scan_ports(target_ip, ports, args.timeout, args.save)

if __name__ == "__main__":
    main()
