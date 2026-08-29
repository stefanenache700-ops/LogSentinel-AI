import os
import json
import ipaddress

from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ and "GEMINI_API_KEY" in os.environ:
    os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError(
        "Setează GOOGLE_API_KEY sau GEMINI_API_KEY în fișierul .env!"
    )

def get_server_logs(service: str) -> str:
    """
    Extrage ultimele linii de log pentru un serviciu.
    Servicii disponibile: auth, nginx.
    """

    mock_logs = {
        "auth": [
            "2026-08-18 08:30:12 Failed password for invalid user admin from 198.51.100.42 port 44211 ssh2",
            "2026-08-18 08:30:15 Failed password for invalid user root from 198.51.100.42 port 44215 ssh2",
            "2026-08-18 08:30:18 Failed password for invalid user ubuntu from 198.51.100.42 port 44219 ssh2",
            "2026-08-18 08:31:00 Accepted publickey for stefan from 192.168.1.50 port 51234 ssh2",
        ],
        "nginx": [
            "198.51.100.42 - - [18/Aug/2026:08:32:01] 'GET /admin/login.php HTTP/1.1' 401",
            "198.51.100.42 - - [18/Aug/2026:08:32:05] 'GET /wp-login.php HTTP/1.1' 404",
            "192.168.1.50 - - [18/Aug/2026:08:32:10] 'GET /api/v1/dashboard HTTP/1.1' 200",
        ],
    }

    service = service.strip().lower()

    logs = mock_logs.get(
        service,
        ["Nu există log-uri recente pentru acest serviciu."]
    )

    return json.dumps(
        {
            "service": service,
            "entries": logs,
        },
        ensure_ascii=False,
    )


def block_ip_firewall(ip_address: str, reason: str) -> str:
    """
    Blochează o adresă IP malițioasă în firewall după
    validarea formatului IP.
    """

    ip_address = ip_address.strip()

    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        return (
            f"ERROR: '{ip_address}' nu este o adresă IP validă. "
            "Operațiune anulată."
        )

    print(
        f"\n[FIREWALL ACTION] "
        f"IP {ip_address} BLOCAT. "
        f"Motiv: {reason}"
    )

    return (
        f"SUCCESS: IP-ul {ip_address} a fost blocat "
        f"pe toate porturile de intrare. "
        f"Motiv: {reason}"
    )


def send_security_alert(
    severity: str,
    incident_summary: str
) -> str:
    """
    Trimite o alertă securizată către echipa de securitate.
    """

    severity = severity.strip().upper()

    print(
        f"\n[DISPATCH ALERT] "
        f"[{severity}] {incident_summary}"
    )

    return (
        f"SUCCESS: Alerta [{severity}] "
        "a fost expediată către echipa SOC."
    )


SYSTEM_INSTRUCTION = """
Ești LogSentinel, un agent autonom de analiză a securității
și răspuns la incidente (SOC).

OBIECTIVE:

1. Inspectează log-urile serverului atunci când utilizatorul
   solicită acest lucru, folosind get_server_logs.

2. Analizează log-urile pentru a identifica amenințări precum:
   - atacuri brute-force SSH;
   - scanări de endpoint-uri web;
   - accesări suspecte.

3. Dacă identifici un IP malițios pe baza log-urilor,
   folosește block_ip_firewall pentru a-l bloca.

4. După remediere, folosește send_security_alert pentru
   a notifica echipa SOC.

5. Răspunde utilizatorului cu un raport tehnic structurat
   în Markdown.

REGULI:

- Nu inventa log-uri.
- Nu inventa rezultate ale tool-urilor.
- Folosește get_server_logs înainte de a afirma că ai analizat
  log-urile.
- Nu bloca un IP fără o justificare bazată pe log-uri.
- Dacă identifici un atacator, explică de ce IP-ul este suspect.
- După blocarea unui IP, trimite o alertă SOC.
- Prezintă rezultatul final clar și tehnic.
"""

root_agent = Agent(
    name="log_sentinel",
    model="gemini-3.5-flash-lite",
    description=(
        "Autonomous SOC and log analysis agent "
        "with remediation capabilities."
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        get_server_logs,
        block_ip_firewall,
        send_security_alert,
    ],
)