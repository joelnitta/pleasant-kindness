# Pleasant Kindness - Django App

A simple Django app with "Hello World" homepage.

## Setup

1. Clone this repo
2. Create a virtual environment: python -m venv venv
3. Activate it: source venv/bin/activate (or venv\Scripts\activate on Windows)
4. Install dependencies: pip install -r requirements.txt
5. Run locally: `./serve.sh`

## Local Preview

Use `serve.sh` to preview the site before pushing:

```bash
./serve.sh
```

Then open http://127.0.0.1:8000 in your browser. The server watches
for file changes, so edits to `myapp/content/*.md` are reflected
immediately on refresh — no restart needed.

`serve.sh` clears the Postgres environment variables so no local
database is required. It has no effect on Railway, which uses the
`Procfile` and its own database credentials.

## Deploy to Railway

1. Push this repo to GitHub
2. Connect it to Railway
3. Railway will automatically deploy!

The app will be available at your Railway domain.
