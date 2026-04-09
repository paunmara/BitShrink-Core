# Network Sentinel 🛡️

Network Sentinel is a sophisticated **Network Intrusion Detection System (NIDS)** designed for real-time traffic monitoring and threat identification. By leveraging Deep Packet Inspection (DPI) and temporal heuristic analysis, the system identifies anomalous patterns—such as DDoS attempts or unauthorized port scans—across local and wide-area networks.

## 🏗️ System Architecture
The application is built on a **multi-threaded asynchronous architecture**, ensuring that high-speed packet ingestion never bottlenecks the user interface or analytical engine.



### Core Components:
* **Ingestion Engine:** Utilizes the Scapy library to interface with raw sockets, capturing L2/L3/L4 data across specified network interfaces.
* **DPI Layer (Deep Packet Inspection):** Performs protocol analysis at the Transport Layer (TCP/UDP), mapping destination ports to a database of 1,000+ registered services (HTTPS, SSH, DNS, etc.).
* **Heuristic Analyzer:** Implements a **Sliding Window Algorithm** using `collections.deque`. It monitors packet frequency within a 10-second temporal window to detect volumetric attacks.
* **Geospatial Resolver:** Interfaces with RESTful APIs to provide real-time geographic attribution for external IP addresses.
* **SOC Dashboard:** A high-fidelity terminal UI built with `Rich`, utilizing ANSI escape codes for stationary, real-time data visualization.

## 📊 Performance & Scalability
* **Concurrency:** Decoupled Sniffer and UI threads maintain sub-200ms latency in dashboard updates.
* **Memory Efficiency:** Pruning logic ensures that the `ip_log` and `recent_packets` buffers remain at a constant memory footprint, regardless of uptime.

## 🚦 Deployment
1. **Initialize Environment:** `python -m venv .venv && source .venv/bin/activate`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Elevated Execution:** `sudo python main.py` (Linux) or Run as Administrator (Windows).

## 🧪 Quality Assurance
Validated via a comprehensive suite of unit tests covering the detection logic and data integrity:
```bash
python -m unittest discover tests
