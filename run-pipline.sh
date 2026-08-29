#!/bin/bash

cd "$(dirname "$0")"

source .venv/bin/activate

echo "Running Scrapy..."
scrapy crawl market

echo "Running cleaning..."
~/.venv/bin/python cleaning.py

echo "DONE"