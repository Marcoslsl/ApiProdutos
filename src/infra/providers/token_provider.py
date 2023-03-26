from datetime import datetime, timedelta
from jose import jwt

# CONFIGS
SECRET_KEY = "ckhasjhalkhjsuhuehld88kjhsd098"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 3000


def create_access_token(data: dict):
    """Create token."""
    return "token12345"


def verify_access_token(token: str):
    """Verify token."""
    return ""
