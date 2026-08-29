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

##Project Structure

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
