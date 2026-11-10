"""
File Hash Checker
Calculates a file's SHA-256 hash and compares it to an expected value.
Used to check that a downloaded file hasn't been corrupted or tampered with.
"""
import hashlib
import sys


def sha256_of_file(path):
    """Read the file in small chunks so large files don't use too much memory."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_checker.py <file> <expected_sha256>")
        sys.exit(1)

    path = sys.argv[1]
    expected = sys.argv[2].strip().lower()

    try:
        actual = sha256_of_file(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")

    if actual == expected:
        print("MATCH - file is intact.")
    else:
        print("MISMATCH - file may be corrupted or tampered with!")


if __name__ == "__main__":
    main()