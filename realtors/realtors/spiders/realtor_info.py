from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from selenium import selenium, webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urlparse

from realtors.items import RealtorsItem

class RealtorInfo(InitSpider):
    name = 'realtor_info'
    allowed_domains=['http://www.realtor.com']
    profiles_list_xpath = '//*[@id="AgentHeaderInfo"]/div'
    item_fields = {
        'name': '//*[@id="AgentHeaderInfo"]/div/div/ul[1]/li[1]/h1/em/text()',
        'number': '//*[@id="AgentHeaderInfo"]/div/div/ul[1]/li[3]/text()',
        'company': '//*[@id="AgentHeaderInfo"]/div/div/ul[1]/li[4]/label/text()',
        'address': '',
        'website': '', #if displayed
        'email': '', # if displayed
        'broker': '' #true or false

    }

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

        wait = WebDriverWait(sel, 10)


        try:
            elements =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'agentProfileRowNum')))
            for element in elements:
                profiles.append(element.find_element_by_tag_name('a').get_attribute('href'))

            for profile in profiles:
                self.log('Found item link: %s' %profile)
                yield Request(profile, callback=self.parse_profile, dont_filter=True)
        finally:
            print "done"



    def parse_profile(self, response):

        wait = WebDriverWait(self.selenium, 10)

        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div/div[@id="mainColumn"]/div[1]')))
        print element.get_attribute("innerHTML")


        item = RealtorsItem()
        item['name'] = ""
        item['company'] = ""
        item['number'] = ""
        item['address'] = ""
        item['website'] = ""
        item['email'] = ""
        item['broker'] = ""

        return item

