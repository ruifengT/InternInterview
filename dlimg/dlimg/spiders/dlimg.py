import scrapy
from dlimg.items import DlimgItem

# create project: scrapy startproject Dlimg
# run spider: scrapy crawl dlimg
# use pip to install scrapy
# also beforehand have MS Visual C++ 14.0+ and pywin32 installed
# for image ImportError (DLL load failed) reinstall pillow version 4.0.0 for python 3.6.0

class DlimgSpider(scrapy.Spider):
    # spider name
    name = 'dlimg'

    def start_requests(self):
        # target urls
        urls = [
            'http://www.decormatters.com/index.php'
        ]
        # for each url yield request
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # extract all source urls
        src_urls = response.xpath('//img/@src').extract()

        # for each source urls
        for src_url in src_urls:
            # join source url with website url
            joined_url = response.urljoin(src_url)
            # yeild a download image item with its image_urls which set to joined_url
            yield DlimgItem(image_urls=[joined_url])
