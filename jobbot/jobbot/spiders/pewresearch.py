# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
import scrapy


class PewresearchSpider(scrapy.Spider):
    name = 'pewresearch'
    allowed_domains = ['https://jobs-prc.icims.com/']
    start_urls = ['https://jobs-prc.icims.com/jobs/search?ss=1&searchLocation=&searchCategory=&in_iframe=1&hashed=124493942']

    def parse(self, response):
        lx = LinkExtractor()
        lst = lx.extract_links(response) # List contains the list of jobs
        # Call the function which compares between lst and MongoDB. Return Boolean Value

        # if True, call the function which send an email to users