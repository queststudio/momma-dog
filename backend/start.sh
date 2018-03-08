#!/bin/bash

gunicorn -c 'gunicorn_config.py' src/api:app