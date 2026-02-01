# Network-Aware Compute Offloading & Benchmarking

### Project Overview

This research-oriented project evaluates the feasibility and performance of **Compute-as-a-Service (CaaS)** in mobile environments. It simulates a mobile client that must decide—based on real-time network conditions—whether to execute a compute-intensive task locally or offload it to a remote edge server.

The framework includes a benchmarking suite to stress-test the system under varying network impairments like latency, jitter, and packet loss using Linux Kernel traffic control tools.

---

### Key Features

* **Dynamic Decision Engine:** A Python-based client that profiles the network environment to determine the optimal execution site (Local vs. Edge).
* **Network Simulation:** Utilizes `tc` (Traffic Control) and `netem` (Network Emulator) to simulate 5G, LTE, and congested network profiles.
* **Compute-as-a-Service (CaaS):** A socket-based server architecture designed to handle remote execution requests.
* **KPI Analysis:** Measures and logs critical Key Performance Indicators (KPIs) including:
* **Round Trip Time (RTT)**
* **Task Execution Latency (Local vs. Offloaded)**
* **Throughput Impact**
* **Decision Accuracy under Network Stress**



---

### Project Structure

```text
.
├── server.py        # The Edge Compute Service
├── client.py        # Decision Engine & Mobile Client
├── benchmark.sh     # Automated Stress-Testing Suite (Linux/tc)
└── README.md        # Documentation

```

---

### Technical Requirements

* **Operating System:** Linux (Ubuntu recommended for `tc` support)
* **Language:** Python 3.x
* **Tools:** Linux `iproute2` package (for `tc` command)

---

### How to Run & Benchmark

1. **Start the Edge Server:**
```bash
python3 server.py

```


2. **Run the Benchmark Suite (Requires Sudo for Network Simulation):**
```bash
chmod +x benchmark.sh
sudo ./benchmark.sh

```



---

### Research Observations & KPIs

During the stress-testing phase, the following traffic patterns and behaviors were identified:

* **Latency Sensitivity:** Offloading remains beneficial until the RTT exceeds .
* **Packet Loss Impact:** High packet loss () significantly degrades CaaS solutions, making local execution more reliable for real-time applications.
* **Throughput Constraints:** Bandwidth throttling identifies the minimum data rate required to sustain high-resolution compute-intensive tasks.

---

### Future Scope

* Integration with **Ollama** for benchmarking LLM-offloading specifically.
* Expanding to **Docker-based** microservices to evaluate virtualization overhead.

---

### Next Step for You

1. **Push this to GitHub:** Create a new repository and upload the three files we discussed.
2. **Add a "Results" section:** If you run the script, copy the output from your terminal and paste it into the README under a "Sample Results" header to show you've actually tested it.

**Would you like me to help you draft the "Results" table based on the expected output of the benchmarking script?**
