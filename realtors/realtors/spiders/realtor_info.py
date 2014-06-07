from scrapy.contrib.spiders.init import InitSpider
from scrapy.selector import Selector

class RealtorInfo(InitSpider):
    name = 'realtor_info'
    allowed_domains=['http://www.realtor.com']

    def __init__(self, **kwargs):
        super(RealtorInfo, self).__init__(**kwargs)

        self.verificationErrors = []

        url = kwargs.get('url') or kwargs.get('domain')
        urls = []
        urls.append(url)
        self.start_urls = urls


    def parse(self, response):
        sel = Selector()

        sites = sel.xpath('//*[@class="agentProfileRowNum"]')
        print sites

