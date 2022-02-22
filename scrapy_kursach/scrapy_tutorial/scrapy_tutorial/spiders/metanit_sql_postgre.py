import time
import scrapy
from scrapy.spiders import Spider
from urllib.parse import urlparse

class MetanitSqlPostgreSpider(Spider):
    name = 'metanit_sql_postgre'
    start_urls = ['https://metanit.com/sql/postgresql/1.1.php']

    def parse(self, response):
        next_page = response.xpath("//div[@class=\"nav\"]/p/a[3]/@href").get()
        parsed_uri = urlparse(response.url)

        out = {'source_link': response.url,
               'source': '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri),
               'posted': response.xpath('//*[@class="date"]/text()').get(),
               'title': response.xpath('//*[@id="articleText"]/h2/text()').get(),
               'text': ' '.join(response.xpath('//*[@id="articleText"]//text()').getall()),
               'html_body': response.xpath('//*[@id="articleText"]').get()}
        time.sleep(.2)
        yield out

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
