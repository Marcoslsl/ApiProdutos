from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def get_hash(text: str):
    """Get hash."""
    return pwd_context.hash(text)


def verify_hash(text: str, hash: str):
    """Verify hash."""
    return pwd_context.verify(text, hash)
