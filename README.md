## Qualcomm Security Bulletin Parser

A demo project to learn Scrapy.  
The script doesn't work well in some cases because something breaks on parsing.  

Run:  
```bash
$ virtualenv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ scrapy runspider --nolog qualcomm/qualcomm/spiders/bulletins_spider.py
```

