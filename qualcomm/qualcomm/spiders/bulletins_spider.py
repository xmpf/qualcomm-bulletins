import os
import scrapy

OUTDIR = os.path.abspath('./output')

class BulletinsSpider(scrapy.Spider):

    name = 'bulletins'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
    allowed_domains = ['qualcomm.com']
    start_urls = ['https://www.qualcomm.com/company/product-security/bulletins']

    def set_user_agent(self, request):
        ''' change user-agent '''

        request.headers['User-Agent'] = self.user_agent
        return request

    def parse(self, response):
        ''' driver function '''

        entries = response.xpath("//a[@class='InternalLinkComponent__StyledLink-sc-122dfxv-0 jLUaEa Flex-sc-1aicpuu-0 cyKQQz Flex-sc-1aicpuu-0 cFkTcm']/@href").getall()
        for entry in entries:
            url = 'https://www.qualcomm.com' + entry
            yield response.follow(url=url, callback=self.parse_bulletin, cb_kwargs={"bulletin": entry.split("/")[-1]})
        
    def parse_bulletin(self, response, **kwargs):
        ''' callback function '''

        bulletin = kwargs.get("bulletin")
        print(f"Parsing: {bulletin}")

        outdir = os.path.join(OUTDIR, bulletin)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        
        tables = response.xpath("//table")
        for table in tables[3:]:
            
            lines = []
            table_body = table.xpath(".//tbody")
            rows = table_body.xpath(".//tr")

            for ix, row in enumerate(rows):
                left = None
                right = None
                columns = list(map(lambda x: x.strip(), row.xpath(".//td/text()").getall()))
                
                if len(columns) < 2:
                    break
                elif len(columns) >= 2:
                    left = columns[0]
                    right = ' '.join(columns[1:])
                else:
                    left, right = columns

                lines.append(f"{left}: {right}\n")

                if ix == 0:
                    cve = right

            if cve.startswith("CVE-"):

                print(f"[+] {cve}")

                fname = os.path.join(outdir + "/" + cve)
                fname = os.path.abspath(fname)
                if os.path.commonpath([fname, OUTDIR]) != OUTDIR:
                    raise ValueError("Directory traversal attempt")
                
                with open(fname, "w") as f:
                    f.writelines(lines)
