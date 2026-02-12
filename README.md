# ARTEMIS 

An html tool extractor. Using **beautifulsoup4**, you can easily use this to extract text from any html. Just follow the json estructure with your desired html pattern, and url. Simple, straight, and no roundabouts.

Simply run 

```bash

git clone https://github.com/fogg928s4/artemis.git
cd artemis
python3 -m venv .venv
source .venv/bin/activate

pip3 install json beautifulsoup4 requests

cp example-config.json config.json

python3 artemis.py

deactivate
```

Make sure to fill the config.json file with the information you need.
