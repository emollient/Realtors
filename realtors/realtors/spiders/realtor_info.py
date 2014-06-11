from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest

from selenium import selenium, webdriver

import urlparse

from realtors.items import RealtorsItem

class RealtorInfo(InitSpider):
    name = 'realtor_info'
    allowed_domains=['http://www.realtor.com']

    def __init__(self, **kwargs):
        super(RealtorInfo, self).__init__(**kwargs)

        self.verificationErrors = []
        self.selenium = webdriver.PhantomJS()

        url = kwargs.get('url') or kwargs.get('domain')
        urls = []
        urls.append(url)
        self.start_urls = urls




    def parse(self, response):
        sel = self.selenium
        sel.get(response.url)
        sel.implicitly_wait(10)

        profiles = []

        sites = sel.find_elements_by_xpath('//*[@class="agentProfileRowNum"')

        for site in sites:
            profiles.append('http://www.realtor.com/realestateagents' + site.find_element_by_xpath('//div[class="wrap"]/a').get_attribute('href'))

        for profile in profiles:
            profile = urlparse.urljoin(response.url, url)
            self.log('Found item link: %s' %url)
            yield Request(url, callback='self.parse_profile', dont_filter=True)


    def parse_profile(self, response):
        #stuff
        return
