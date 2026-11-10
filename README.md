# Security Scripts

Small Python security tools I built while developing my professional skills
for a career in cybersecurity.

| Script | What it does |
|---|---|
| `password_checker.py` | Rates password strength and suggests improvements |
| `hash_checker.py` | Verifies a file's SHA-256 hash to detect tampering |
| `log_scanner.py` | Scans SSH logs for failed logins and flags possible brute-force IPs |

## Usage
python password_checker.py
python hash_checker.py <file> <expected_sha256>
python log_scanner.py [logfile]