#!/usr/bin/env python3
"""
This script connects to a MySQL database, retrieves user data,
and logs the data while redacting sensitive information.
"""
import os
import re
import logging
import mysql.connector
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Custom logging formatter that redacts specified PII fields from log
    messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified record as text, redacting sensitive fields.
        """
        filtered = filter_datum(self.fields, self.REDACTION,
                                record.getMessage(), self.SEPARATOR)
        record.msg = filtered
        return super().format(record)


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str
) -> str:
    """
    Redact specified fields from the log message.
    """
    extract, replace = (
        lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
        lambda x: r'\g<field>={}'.format(x))
    return re.sub(extract(fields, separator), replace(redaction), message)


def get_logger() -> logging.Logger:
    """
    Create and configure a logger with a redacting formatter.
    """
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database using environment variables for
    configuration.
    """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        port=3306,
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME", ""),
    )


def main():
    """
    Retrieve user data from the database and log it with sensitive fields
    redacted.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT name, email, phone, ssn, password, last_login,\
        user_agent FROM users;")
    logger = get_logger()
    for row in cursor:
        logger.info("name={};email={};phone={};ssn={};password={};\
                    last_login={};user_agent={};".
                    format(row[0], row[1], row[2], row[3], row[4],
                           row[5], row[6]))
    cursor.close()
    db.close()
