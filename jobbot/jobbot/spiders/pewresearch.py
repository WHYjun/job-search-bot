# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
import scrapy
from accessDB import compare

class PewresearchSpider(scrapy.Spider):
    name = 'pewresearch'
    allowed_domains = ['https://jobs-prc.icims.com/']
    start_urls = ['https://jobs-prc.icims.com/jobs/search?ss=1&searchLocation=&searchCategory=&in_iframe=1&hashed=124493942']

    def parse(self, response):
        lx = LinkExtractor()
        lst = lx.extract_links(response) # List contains the list of jobs
        # @TODO Call the function which compares between lst and MongoDB. Return Boolean Value
        flag = compare(name,lst)
        # @TODO if True, call the function which send an email to users
        