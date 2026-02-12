#!/bin/bash

git clone https://github.com/fogg928s4/artemis.git
cd artemis
python3 -m venv .venv
source .venv/bin/activate

pip3 install json beautifulsoup4 requests

cp example-config.json config.json

python3 artemis.py

deactivate


