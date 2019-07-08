#!/bin/bash
export ENVIRONMENT='LOCAL'
echo $ENVIRONMENT
gunicorn -c 'gunicorn_config.py' src.api:app
