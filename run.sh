#!/usr/bin/env sh

exec uvicorn --host 0.0.0.0 --port 7777 --reload --log-level info app.main:app
