# aters-threat-simulator
# ATERS: Automated Threat Enrichment and Response Simulator

**ATERS** is a Python-based threat enrichment and response logic simulator designed for cybersecurity analysts and engineers. This project queries multiple threat intelligence APIs to enrich a given IP address, then simulates SOAR-style decision logic and actions based on the enrichment results.

---

## Features

- Multi-source threat enrichment from:
  - [AbuseIPDB](https://www.abuseipdb.com/)
  - [VirusTotal](https://www.virustotal.com/)
  - [GreyNoise](https://www.greynoise.io/)
- Conditional response logic based on enrichment results
- Simulated SOAR actions:
  - Block IP (mocked firewall rule)
  - Isolate Host (mocked EDR response)
  - Create Ticket (mocked ticketing system)
- Slack alert integration using Incoming Webhooks
- Clean, modular Python codebase using utility functions

---

## Example: Response Logic Decision Tree

```
Input IP: 211.253.9.49

Enrichment Completed

→ Response Logic:

AbuseIPDB score 100 > 70 → Block IP  
Simulated: Blocked IP 211.253.9.49 on firewall (mock call)

VirusTotal reputation -6 < 0 → Isolate host  
Simulated: Isolated host with IP 211.253.9.49 (mock EDR action)

GreyNoise: malicious, noise=True → Create ticket  
Simulated: Created ticket for IP 211.253.9.49 → Reason: GreyNoise indicates scanning or attack activity
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/aters-threat-simulator.git
cd aters-threat-simulator
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Activate:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your Environment

Create a `.env` file in the root directory with the following contents:

```
ABUSEIPDB_KEY=your_abuseipdb_api_key
VT_KEY=your_virustotal_api_key
GN_KEY=your_greynoise_api_key
SLACK_WEBHOOK=https://hooks.slack.com/services/your/webhook/url
```

> **DO NOT commit your `.env` file to GitHub.** It's already included in `.gitignore`.

---

## How to Run

```bash
python main.py
```

Enter an IP address when prompted, and the script will:

1. Query all three intelligence sources.
2. Display and simulate response actions.
3. Send alerts to your Slack channel if applicable.

---

## Project Structure

```
aters-threat-simulator/
│
├── utils/
│   ├── enrich_abuseipdb.py
│   ├── enrich_virustotal.py
│   ├── enrich_greynoise.py
│   └── responders.py
│
├── main.py
├── requirements.txt
├── .env (not committed)
└── README.md
```

---

## Use Case

This project is ideal for demonstrating:

- Python scripting in cybersecurity workflows
- Threat enrichment using public APIs
- SOAR logic simulation
- Alerting and automation

---

## Disclaimer

This project simulates response actions — no real IPs are blocked or hosts isolated. Always test responsibly in safe environments.