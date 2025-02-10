from __future__ import annotations

import hashlib
import secrets

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str

    @classmethod
    def create_user(cls, name: str, email: str, password: str) -> User:
        if not password.strip():
            raise ValueError("Password cannot be empty")
        hashed_password = cls.hash_password(password)
        return cls(name=name, email=email, password=hashed_password)

    @staticmethod
    def hash_password(password: str) -> str:
        salt = secrets.token_hex(16)  # Secure 16-byte salt
        hashed = hashlib.sha256((salt + password).encode()).hexdigest()
        return f"{salt}${hashed}"  # Store salt and hash together

    def verify_password(self, password: str) -> bool:
        try:
            salt, stored_hash = self.password.split("$")
            test_hash = hashlib.sha256((salt + password).encode()).hexdigest()
            return test_hash == stored_hash
        except ValueError:
            return False  # Handle improperly formatted hashes
