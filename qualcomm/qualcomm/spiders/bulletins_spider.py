from calendar import c
import os
import scrapy

class BulletinsSpider(scrapy.Spider):
    name = 'bulletins'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
    allowed_domains = ['qualcomm.com']
    start_urls = ['https://www.qualcomm.com/company/product-security/bulletins']

    def parse(self, response):
        entries = response.xpath("//a[@class='InternalLinkComponent__StyledLink-sc-122dfxv-0 jLUaEa Flex-sc-1aicpuu-0 cyKQQz Flex-sc-1aicpuu-0 cFkTcm']/@href").getall()
        for entry in entries:
            url = 'https://www.qualcomm.com' + entry
            print(url)
            yield response.follow(url=url, callback=self.parse_bulletin)
        
    def parse_bulletin(self, response):
        cves = iter(response.xpath("//*[contains(@id, '_cve')]/text()").getall())
        tables = response.xpath("//table")
        for table in tables[4:]:
            
            lines = []
            table_body = table.xpath(".//tbody")
            rows = table_body.xpath(".//tr")
            for row in rows:
                left = None
                right = None
                columns = list(map(lambda x: x.strip(), row.xpath(".//td/text()").getall()))
                if len(columns) < 2:
                    break
                elif len(columns) >= 2 and columns[0].startswith('Patch'):
                    left = columns[0]
                    right = ' '.join(columns[1:])
                    pass
                elif len(columns) > 2:
                    break
                else:
                    left, right = columns
                lines.append(f"{left}: {right}\n")
            else:
                if not os.path.exists("./output"):
                    os.makedirs("./output")
                cve = next(cves)
                fname = "./output/" + cve
                with open(fname, "w") as f:
                    f.writelines(lines)


        

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request
