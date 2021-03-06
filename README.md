## Qualcomm Security Bulletin Parser

A demo project to learn Scrapy.  

Run:  
```bash
$ virtualenv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ scrapy runspider --nolog qualcomm/qualcomm/spiders/bulletins_spider.py
```

Output:
```
$ ls -1p output
april-2021-bulletin/
august-2021-bulletin/
december-2021-bulletin/
february-2022-bulletin/
january-2022-bulletin/
july-2021-bulletin/
june-2021-bulletin/
march-2021-bulletin/
may-2021-bulletin/
november-2021-bulletin/
october-2021-bulletin/
september-2021-bulletin/

$ ls -1 output/february-2022-bulletin
CVE-2021-30309
CVE-2021-30318
CVE-2021-30322
CVE-2021-30323
CVE-2021-30324
CVE-2021-30325
CVE-2021-30326
CVE-2021-35068
CVE-2021-35069
CVE-2021-35074
CVE-2021-35075
CVE-2021-35077

$ cat output/february-2022-bulletin/CVE-2021-30309
CVE ID: CVE-2021-30309
Title: Buffer Copy Without Checking Size of Input in Modem
Description: Improper size validation of QXDM commands can lead to memory corruption
Technology Area: UTILS
Vulnerability Type: CWE-120 Buffer Copy Without Checking Size of Input ('Classic Buffer Overflow')
Access Vector: Local
Security Rating: High
CVSS Rating: High
CVSS Score: 7.8
CVSS String: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
Date Reported: 03/01/2021
Customer Notified Date: 08/02/2021
Affected Chipsets*: MDM9650, QCA6174A, QCA6390, QCA6391, QCA9377, QCM6125, QCS410, QCS603, QCS605, QCS610, QCS6125, SD660, SD665, SD690 5G, SD730, SD765, SD765G, SD768G, SD865 5G, SD870, SDX12, SDX55M, SDXR1, SM7250P, WCD9326, WCD9335, WCD9341, WCD9370, WCD9375, WCD9380, WCD9385, WCN3950, WCN3980, WCN3988, WCN3990, WCN3991, WCN3998, WCN6850, WCN6851, WSA8810, WSA8815, WSA8830, WSA8835
```
