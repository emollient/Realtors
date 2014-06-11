from scrapy.contrib.spiders.init import InitSpider
from scrapy.selector import Selector

from selenium import selenium, webdriver

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

        items = []

        sites = sel.find_elements_by_xpath('//*[@id="2"]')
        """
        for site in sites:
            item = RealtorsItem()
            item['name'] = site.find_element_by_xpath('//div[@class="wrap"]/a/em').text
            item['company'] = site.find_element_by_xpath('//ul[@class="summary"]/label').text
            item['number'] = site.find_element_by_xpath('//ul[@class="summary"]/li[@class="phone"]').text
            items.append(item)
        """
        print(sites[0].get_attribute('class'))
        self.selenium.quit()
