#!/bin/bash

. .web/bin/activate
pip install -r requirements.txt
npm install
python -m app