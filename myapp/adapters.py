from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError

from .member_whitelist import load_allowed_member_emails


class MemberWhitelistAccountAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        email = super().clean_email(email)
        normalized_email = email.strip().lower()

        if normalized_email not in load_allowed_member_emails():
            raise ValidationError(
                'This email is not listed in the approved member directory.'
            )

        return normalized_email
