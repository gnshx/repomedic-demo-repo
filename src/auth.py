def parse_user_id(header_val: str) -> int:
    """Parse integer user ID from Bearer token header."""
    if not header_val or not header_val.strip():
        raise ValueError("Invalid header format: header cannot be empty")
    parts = header_val.strip().split(" ")
    if len(parts) < 2:
        raise ValueError("Invalid authorization header: missing token")
    return int(parts[1])
