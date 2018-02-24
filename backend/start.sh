#!/bin/bash

gunicorn -c 'gunicorn_config.py' src:app