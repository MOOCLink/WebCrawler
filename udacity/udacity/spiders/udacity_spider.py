import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.item import Item, Field

class UdacityItem(Item):
    name = Field()
    project = Field()
    about = Field()
    instructor = Field()
    school = Field()
    startDate = Field()
    url = Field()
    length = Field()
    effort = Field()
    prereqs = Field()
    video = Field()
    syllabus = Field()
    courseCode = Field()
    category = Field()

class UdacitySpider(CrawlSpider):
    name = "udacity"
    allowed_domains = ["class-central.com"]
    start_urls = [
        "https://www.class-central.com/provider/udacity"
    ]
    # # no pagination at the moment therefore no xpath restrictions
    # rules = (Rule (SgmlLinkExtractor(allow=("", ),restrict_xpaths=('',))
    # , callback="parse_sites", follow= True),
    # )

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        sel = Selector(response)
        sites = sel.xpath('//a[@class="course-name"]/@href').extract()

        requests = []
        for site in sites:
            site = "https://www.class-central.com" + site
            item = UdacityItem()
            request = scrapy.Request(site, callback=self.parse_details)
            request.meta['item'] = item            
            requests.append(request)

        return requests


    def parse_details(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        sel = Selector(response)
        item = response.meta['item']
        item['name'] = sel.xpath('//h1[@class="course-title"]/text()').extract()
        item['about'] = sel.xpath('//div[@class="course-desc"]/div[position()=1]/*').extract() #retains tags
        item['url'] = sel.xpath('//a[@class="register-button"]/@href').extract()
        item['instructor'] = sel.xpath('//span[@class="course-instructors"]/text()').extract()
        item['school'] = sel.xpath('//ul[@class="institution-list"]/li/a/text()').extract()
        item['startDate'] = sel.xpath('//div[@class="course-data-row course-pace"]/a/text()').extract()
        item['length'] = sel.xpath('//span[@class="course-length"]/text()').extract()
        item['prereqs'] = sel.xpath('//div[preceding-sibling::strong[text()="Prerequisites and Requirements"]]/p').extract() #retains tags
        item['video'] = sel.xpath('//a[text()="Youtube"]/@href').extract()
        item['syllabus'] = sel.xpath('//*[preceding-sibling::h2[text()="Syllabus"]]').extract() #retains tags
        item['effort'] = "Assumes 6hr/wk"
        item['categoryId'] = "12"
        cc = item['url'][0].split("/")[5]
        if(cc == "Course"):
            cc = item['url'][0].split("/")[6]
        print(item['url'][0] + "\n")
        print(cc + "\n") 
        item['courseCode'] = cc
        if item['startDate'] == 'Upcoming':
            item['startDate'] = sel.xpath('//select[@id="sessionOptions"]/option/@content').extract()
        return item
