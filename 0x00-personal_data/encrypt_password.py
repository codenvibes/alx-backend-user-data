#!/usr/bin/env python3

"""
This script provides two functions for password hashing and validation
using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a given hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
