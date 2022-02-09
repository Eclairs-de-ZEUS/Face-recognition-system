import sys

def print_info(string: str) -> None:
    print(f"[INFO] {string}")

def print_error(string: str) -> None:
    print(f"[ERROR] {string}", file=sys.stderr)
    sys.exit(84)
