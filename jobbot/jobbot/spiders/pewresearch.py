# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
import scrapy
import os
import sys

scriptpath = os.path.dirname(__file__)
sys.path.append(os.path.abspath(scriptpath))
from accessDB import compare
from sendEmail import notify

class PewresearchSpider(scrapy.Spider):
    name = 'pewresearch'
    allowed_domains = ['jobs-prc.icims.com/']
    start_urls = ['https://jobs-prc.icims.com/jobs/search?ss=1&searchLocation=&searchCategory=&in_iframe=1&hashed=124493942']

    def parse(self, response):
        name = 'pewresearch'
        lx = LinkExtractor()
        lst = lx.extract_links(response) # List contains the list of jobs
        # Call the function which compares between lst and MongoDB. Return Boolean Value
        flag = compare(name,lst)
        # @TODO if True, call the function which send an email to users
        if flag:
            notify(name)
            print("Notified")
        else:
            print("No Update")
