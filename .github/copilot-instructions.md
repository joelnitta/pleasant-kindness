# Copilot Instructions

## Styling Consistency Rule

- All user-facing pages must use consistent site styling.
- Templates for pages exposed to users must extend `base.html`.
- Avoid shipping framework default plain templates when a page is visible in the
  normal user flow.
- When adding auth/account pages (login, signup, email verify, password reset,
  confirmation pages), create or update matching template overrides in:
  `myapp/templates/account/`.
- Keep copy, spacing, and link/button presentation aligned with existing portal
  pages.
