# Pleasant Kindness - Django App

A simple Django app with "Hello World" homepage.

This project now includes a Django built-in login system with:

- Login and logout
- Signup via django-allauth
- Password reset flow
- Members-only page
- Staff-only page

## Setup

1. Clone this repo
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `source .venv/bin/activate` (or `.venv\Scripts\activate` on
	Windows)
4. Install dependencies: pip install -r requirements.txt
5. Run locally: `./serve.sh`

## First-time Database Setup

Run these commands once after installing dependencies:

```bash
python manage.py migrate
python manage.py createsuperuser
```

This creates the auth tables and an admin account.

## Local Preview

Use `serve.sh` to preview the site before pushing:

```bash
./serve.sh
```

Then open http://127.0.0.1:8000 in your browser. The server watches
for file changes, so edits to `myapp/content/*.md` are reflected
immediately on refresh — no restart needed.

`serve.sh` clears the Postgres environment variables. In that mode, the app
uses local SQLite (`db.sqlite3`), which is easiest for beginners.

It has no effect on Railway, which uses the `Procfile` and its own Postgres
credentials.

## Login URLs

- Login: `http://127.0.0.1:8000/accounts/login/`
- Signup: `http://127.0.0.1:8000/accounts/signup/`
- Logout: submit the "Log out" button in the top navigation
- Password reset: `http://127.0.0.1:8000/accounts/password_reset/`
- Members page (login required): `http://127.0.0.1:8000/members/`
- Staff page (staff users only): `http://127.0.0.1:8000/staff/`
- Admin: `http://127.0.0.1:8000/admin/`

## Member-Only Signup Rule

Signup is restricted to emails listed in `ppg_members.csv` at the repository
root. Users can only create an account if their submitted email matches an
email in that file (case-insensitive).

## Beginner Local Login Test

Use this checklist to test everything locally.

1. Start the server:

	```bash
	./serve.sh
	```

2. In your browser, open `/accounts/login/` and confirm the login form loads.

3. Log in with your superuser account and check:
	- You can open `/members/`
	- You can open `/staff/`
	- You can open `/admin/`

4. Log out with the top nav button and confirm `/members/` redirects to login.

5. Test password reset:
	- Open `/accounts/password_reset/`
	- Enter the email of an existing user
	- Submit and check terminal output for the reset URL
	- Open that URL and set a new password
	- Log in with the new password

6. Test signup restriction:
	- Open `/accounts/signup/`
	- Try signing up with an email that is not in `ppg_members.csv` (should fail)
	- Try signing up with an email that is in `ppg_members.csv` (should succeed)

For a full beginner guide with troubleshooting, see
`docs/local-testing.md`.

## Deploy to Railway

1. Push this repo to GitHub
2. Connect it to Railway
3. Railway will automatically deploy!

The app will be available at your Railway domain.

### Railway Login Fix

If login POSTs fail with a CSRF origin error on Railway, set one of these
environment variables in the Railway service settings:

```bash
CSRF_TRUSTED_ORIGINS=https://your-app.up.railway.app
```

Or, if you prefer, set:

```bash
RAILWAY_PUBLIC_DOMAIN=your-app.up.railway.app
```

The app reads either value and adds the deployed HTTPS origin to Django's CSRF
trusted origins list.
