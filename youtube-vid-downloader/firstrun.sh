#!/usr/bin/env bash


pip install pipenv 
python -m venv .venv
pipenv shell
pipenv install

python app/main.py
