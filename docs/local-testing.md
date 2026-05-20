# Local Login Testing Guide (Beginner Friendly)

This guide shows exactly how to test login features on your own machine.

## 1. Prerequisites

- Python 3 installed
- Project cloned locally
- Terminal open in project root

## 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

If installation fails for `psycopg2-binary` on macOS, run:

```bash
brew install libpq
export PATH="/opt/homebrew/opt/libpq/bin:$PATH"
pip install -r requirements.txt
```

## 4. Initialize database tables

Use this once on a new local setup:

```bash
python manage.py migrate
python manage.py createsuperuser
```

What to expect:

- `migrate` prints many `Applying ... OK` lines.
- `createsuperuser` asks for username, email, and password.

## 5. Start the app

```bash
./serve.sh
```

What this does:

- Clears Postgres env vars for local development
- Uses SQLite file `db.sqlite3`
- Starts server at `http://127.0.0.1:8000`

## 6. Test login and access control

1. Open `http://127.0.0.1:8000/accounts/login/`
2. Log in with your superuser credentials
3. Open `http://127.0.0.1:8000/members/` (should work)
4. Open `http://127.0.0.1:8000/staff/` (should work for superuser/staff)
5. Click `Log out` in nav
6. Re-open `http://127.0.0.1:8000/members/`

Expected result: redirected to login page.

## 7. Test first-password setup flow (password reset)

1. Log in to admin at `http://127.0.0.1:8000/admin/`
2. Create a regular user with a valid email address
3. Open `http://127.0.0.1:8000/accounts/password_reset/`
4. Enter the user email and submit
5. In terminal, find the printed reset URL
6. Open reset URL, set a new password
7. Log in as that user with the new password

## 8. Optional: Test with local Postgres instead of SQLite

If you want local behavior closer to production, set env vars before running
server:

```bash
export PGDATABASE="your_db"
export PGUSER="your_user"
export PGPASSWORD="your_password"
export PGHOST="localhost"
export PGPORT="5432"
python manage.py migrate
python manage.py runserver
```

Note: do not use `./serve.sh` for this mode because it clears Postgres vars.

## 9. Troubleshooting

- Error: `ModuleNotFoundError: No module named 'django'`
  - Fix: activate venv and run `pip install -r requirements.txt`
- Error: `could not connect to server` (Postgres mode)
  - Fix: verify DB is running and PG env vars are correct
- Error: `relation ... does not exist`
  - Fix: run `python manage.py migrate`
- Password reset email not visible
  - Fix: use local console email backend and check terminal output
