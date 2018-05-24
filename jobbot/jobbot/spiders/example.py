# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
import scrapy

import os
import sys

from accessDB import compare
from sendEmail import notify


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com/']
    start_urls = ['https://example.com/career']

    def parse(self, response):
        name = 'example'
        lx = LinkExtractor()
        lst = lx.extract_links(response)  # List contains the list of jobs
        # Call the function which compares between lst and MongoDB. Return Boolean Value
        flag = compare(name, lst)
        # if True, call the function which send an email to users
        if flag:
            notify(name)
        else:
            print("No Update")
