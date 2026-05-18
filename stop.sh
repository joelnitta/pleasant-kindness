#!/usr/bin/env bash
pkill -f "manage.py runserver" && echo "Server stopped." || echo "No server was running."
