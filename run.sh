#!/bin/bash

venv=$(find . -type f -name "activate" 2>/dev/null)
if [ -f "$venv" ]; then
    source "$venv"
else
    /usr/bin/virtualenv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
fi

scrapy runspider --nolog qualcomm/qualcomm/spiders/bulletins_spider.py
