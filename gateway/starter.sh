#!/bin/bash
gunicorn -w 2 -k uvicorn.workers.UvicornWorker api:app --reload -b 0.0.0.0:8080
