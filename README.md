# 🛡️ Basic Firewall Simulation in Python

Welcome to this Python-based firewall simulation! This project is designed to help budding cybersecurity enthusiasts understand the fundamentals of network traffic filtering based on IP addresses and ports. 🚦

## 🌟 Features

- **IP and Port Filtering**: Filters incoming network traffic based on predefined rules involving IP addresses and ports. 🚫
- **Logging**: Every decision made by the firewall is logged for security analysis and auditing purposes. 📝
- **Random Traffic Simulation**: Generates random IP addresses and ports to simulate different network traffic scenarios and test the firewall's effectiveness. 🎲

## 🛠 Installation

This project uses only standard Python libraries, ensuring that no extra installations are necessary. Just make sure you have Python 3.x installed. Download Python [here](https://www.python.org/downloads/).

## 🚀 Usage

To get the firewall simulation up and running, follow these steps:

```bash
git clone https://your-repository-url-here
cd le-meilleur-firewall 
python firewall_simulation.py
```

## 🔧 Configuration

You can customize the firewall rules in the `main()` function. Here's how you can define your rules:

```python
firewall_rules = [
    {"ip": "192.168.1.1", "port": 80, "action": "block"},
    {"ip": "192.168.1.4", "action": "allow"},
    {"ip": "192.168.1.9", "port": 443, "action": "block"},
    ...
]
```
- **ip** : The IP address to filter.
- **port** : (Optional) Specify the port for targeted control. If omitted, the rule applies to all ports for that IP.
- **action** : Choose whether to block or allow the traffic.

## 🤝 Contributing

Feel free to fork this repo and contribute back by submitting a pull request. We love your submissions towards:
- Better simulation logic
- More configuration options
- A cooler user interface

## 😄 A Little Dev Joke

> Why do programmers prefer dark mode? 🌚
> 
> Because light attracts bugs! 🐛

## 📜 License

This project is freely available under the MIT license. Feel free to use it however you'd like!
