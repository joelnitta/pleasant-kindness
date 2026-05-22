import csv
import os
from functools import lru_cache
from pathlib import Path

from django.conf import settings


def _normalize_email(value):
    return (value or '').strip().lower()


def _load_emails_from_env():
    raw_value = os.environ.get('MEMBER_EMAIL_WHITELIST', '')
    if not raw_value.strip():
        return set()

    normalized = raw_value.replace(';', ',').replace('\n', ',').replace('\r', ',')
    return {
        _normalize_email(item)
        for item in normalized.split(',')
        if _normalize_email(item)
    }


def _load_emails_from_csv():
    csv_path = Path(settings.BASE_DIR) / 'ppg_members.csv'
    if not csv_path.exists():
        return set()

    allowed_emails = set()
    with csv_path.open('r', encoding='utf-8-sig', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            email = _normalize_email(row.get('email'))
            if email:
                allowed_emails.add(email)
    return allowed_emails


@lru_cache(maxsize=1)
def load_allowed_member_emails():
    env_emails = _load_emails_from_env()
    if env_emails:
        return env_emails
    return _load_emails_from_csv()
