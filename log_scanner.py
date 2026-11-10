"""
Failed Login Log Scanner
Scans an SSH auth log for failed logins, counts attempts per IP address,
and flags IPs that look like brute-force attacks.
"""
import re
import sys
from collections import Counter

# Matches lines like:
# "Failed password for root from 203.0.113.45"
# "Failed password for invalid user admin from 203.0.113.45"
PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})"
)

THRESHOLD = 3  # this many failures or more from one IP gets flagged


def scan(path):
    ips = Counter()
    users = Counter()
    with open(path) as f:
        for line in f:
            match = PATTERN.search(line)
            if match:
                user, ip = match.groups()
                ips[ip] += 1
                users[user] += 1
    return ips, users


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "sample_auth.log"

    try:
        ips, users = scan(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

    print(f"Scanned {path}: {sum(ips.values())} failed login attempts found\n")

    print("Attempts by IP:")
    for ip, count in ips.most_common():
        flag = "  <-- possible brute force" if count >= THRESHOLD else ""
        print(f"  {ip:<16} {count}{flag}")

    print("\nTargeted usernames:")
    for user, count in users.most_common():
        print(f"  {user:<16} {count}")


if __name__ == "__main__":
    main()