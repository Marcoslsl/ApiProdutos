from datetime import datetime, timedelta
from jose import jwt

# CONFIGS
SECRET_KEY = "ckhasjhalkhjsuhuehld88kjhsd098"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 3000


def create_access_token(data: dict):
    """Create token."""
    data_copy = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({"exp": expire})
    token_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    """Verify token."""
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")
