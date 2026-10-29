def parse_user_id(header_val: str) -> int:
    """Parse integer user ID from Bearer token header."""
    parts = header_val.split(" ")
    # Bug: Crashes with IndexError when empty header or no token passed
    return int(parts[1])
