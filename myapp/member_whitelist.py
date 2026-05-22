import csv
from functools import lru_cache
from pathlib import Path

from django.conf import settings


@lru_cache(maxsize=1)
def load_allowed_member_emails():
    csv_path = Path(settings.BASE_DIR) / 'ppg_members.csv'
    if not csv_path.exists():
        return set()

    allowed_emails = set()
    with csv_path.open('r', encoding='utf-8-sig', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            email = (row.get('email') or '').strip().lower()
            if email:
                allowed_emails.add(email)
    return allowed_emails
