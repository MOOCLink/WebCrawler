import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.item import Item, Field

class EdxItem(Item):
    name = Field()
    about = Field()
    instructor = Field()
    school = Field()
    courseCode = Field()
    startDate = Field()
    url = Field()
    length = Field()
    effort = Field()
    prereqs = Field()
    video = Field()
    category = Field()

class EdXSpider(CrawlSpider):
    name = "edx"
    allowed_domains = ["edx.org"]
    start_urls = []
    file = open('data/category_map', 'r')
    for line in file:
        url = "https://www.edx.org/course-list/allschools/" + line.strip() + "/allcourses"
        start_urls.append(url)


    rules = (Rule (SgmlLinkExtractor(allow=("", ),restrict_xpaths=('//a[@title="Go to next page"]',))
    , callback="parse_sites", follow= True),
    )

    def parse_sites(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        sel = Selector(response)
        # sites = sel.xpath('//div/div/a/@href').extract() # course-list-all
        sites = sel.xpath('//strong/a/@href').extract()
        sites.pop(0) # remove home directory link

        requests = []
        for site in sites:
            # site = "https://edx.org/" + site
            item = EdxItem()
            item['url'] = site
            item['category'] = response.request.url.split("/")[5]
            request = scrapy.Request(site, callback=self.parse_details)
            request.meta['item'] = item
            requests.append(request)
        return requests


    def parse_details(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        sel = Selector(response)
        item = response.meta['item']
        item['name'] = sel.xpath('//h2/span/text()').extract()
        item['about'] = sel.xpath('//*[@itemprop="description"]').extract()
        item['instructor'] = sel.xpath('//*[@class="staff-title"]/text()').extract()
        item['school'] = sel.xpath('//*[@class="course-detail-school item"]/a/text()').extract()
        item['courseCode'] = sel.xpath('//*[@class="course-detail-number item"]/text()').extract()
        item['startDate'] = sel.xpath('//*[@class="course-detail-start item"]/text()').extract()
        item['length'] = sel.xpath('//*[@class="course-detail-length item"]/text()').extract()
        item['effort'] = sel.xpath('//*[@class="course-detail-effort item"]/text()').extract()
        item['prereqs'] = sel.xpath('//*[@class="course-section course-detail-prerequisites-full"]/p/text()').extract()
        item['video'] = sel.xpath('/html/head/meta[@property="og:video"]/@content').extract()
        return item