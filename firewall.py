import random
import logging

# Configure the logging
logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def generate_random_ip():
    """Generate a random IP address within a specified subnet."""
    return f"192.168.1.{random.randint(1, 20)}"

def generate_random_port():
    """Generate a random port number for simulation."""
    return random.randint(1, 65535)

def check_firewall_rules(ip, port, rules):
    """Check if the IP address and port match any firewall rule and return the action."""
    for rule in rules:
        if ip == rule.get("ip") and port == rule.get("port", port):
            return rule['action']
    return "allow"  # Default action if no rule matches

def log_decision(ip, port, action):
    """Log the firewall decision to a log file."""
    logging.info(f"IP: {ip}, Port: {port}, Action: {action}")

def main():
    # Define the firewall rules
    firewall_rules = [
        {"ip": "192.168.1.1", "port": 80, "action": "block"},
        {"ip": "192.168.1.4", "action": "allow"},
        {"ip": "192.168.1.9", "port": 443, "action": "block"},
        {"ip": "192.168.1.13", "action": "block"},
        {"ip": "192.168.1.16", "port": 21, "action": "block"},
        {"ip": "192.168.1.19", "action": "block"}
    ]

    # Simulate network traffic
    for _ in range(10):
        ip_address = generate_random_ip()
        port = generate_random_port()
        action = check_firewall_rules(ip_address, port, firewall_rules)
        log_decision(ip_address, port, action)
        print(f"IP: {ip_address}, Port: {port}, Action: {action}")

if __name__ == "__main__":
    main()
