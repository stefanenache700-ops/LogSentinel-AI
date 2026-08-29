# LogSentinel-AI
Autonomous security and log-monitoring platform that detects anomalies and triggers deterministic remediation in real time using agentic AI workflows. Developed during the Google Romania Agentic AI Summer School 2026.


## Features

* **Agentic Log Analysis:** Leverages Google ADK workflows in `agent.py` to evaluate telemetry, classify anomalies, and reason over security threats.
* **Deterministic Threat Mitigation:** Triggers automatic responses based on severity levels (e.g., suspicious IP isolation, credential invalidation).
* **Reproducible Dependency Tree:** Utilizes pinned dependencies via `requirements.lock.txt` for consistent production deployment.

---

## Architecture Overview

```text
[ System Logs / Telemetry ]
           │
           ▼
[ Google ADK Agent Engine (log_sentinel/agent.py) ]
           │
           ├──► [ Threat Classification & Scoring ]
           └──► [ Automated Remediation Playbooks ]
```

## Project Structure

```text
LogSentinel/
├── .adk/                   # Google Agent Development Kit local configuration
├── log_sentinel/           # Core application package
│   ├── .adk/               # Package-level agent definitions
│   ├── __init__.py         # Package initialization
│   └── agent.py            # Main Agentic AI reasoning and action loop
├── .env                    # Environment variables & API credentials (local only)
├── requirements.lock.txt   # Fully locked, reproducible dependency tree
├── requirements.txt        # Primary project dependencies
└── README.md               # Project documentation
```
## Getting Started

## 1. Clone the repository
```bash
git clone https://github.com/stefanenache700-ops/LogSentinel-AI.git
cd LogSentinel-AI
```
## 2. Set up the Python Virtual Environment (.venv)

### Create the virtual environment
```bash
python3 -m venv .venv
```

### Activate on Linux / macOS:
```bash
source .venv/bin/activate
```

### Activate on Windows (PowerShell / Command Prompt):
```bash
.venv\Scripts\activate
```
## 3. Install Google ADK & Dependencies
### Upgrade pip and install the Google Agent Development Kit (ADK)
```bash
pip install --upgrade pip
pip install google-adk
```

### Install locked dependencies if requirements.lock.txt is present
```bash
pip install -r requirements.txt
```

## 4. Initialize & Configure Google ADK (.adk)
### Initialize local ADK workspace configuration (creates local .adk directory)
```bash
adk init
```
### Configure your environment variables
```bash
cp .env.example .env
```

## 5. Run the Sentinel Agent
### CLI Execution:
```bash
python -m log_sentinel.agent
```
### Web UI Execution:
```bash
adk web
```

