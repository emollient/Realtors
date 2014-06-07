# Scrapy settings for realtors project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'realtors'

SPIDER_MODULES = ['realtors.spiders']
NEWSPIDER_MODULE = 'realtors.spiders'

ITEM_PIPELINES = {'realtors.pipelines.RealtorsPipeline'}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'realtors (+http://www.yourdomain.com)'
