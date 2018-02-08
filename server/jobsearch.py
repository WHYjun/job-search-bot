# -*- coding: utf-8 -*-
import csv
import hashlib

from bs4 import BeautifulSoup
import urllib.request

class JobSearch:
    def __init__(self, reader):
        self.companyLst = []
        self.urls = []
        self.reader = reader

    def export(self):
        for line in reader:
            self.companyLst.append(line[0])
            self.urls.append(line[1])
    
    def check(self):
        self.export()
        for i in range(len(self.urls)):
            req = self.request(self.urls[i])
            soup = BeautifulSoup(req, 'html.parser')
            htmlcode = str(soup.prettify())
            self.writeTemp(htmlcode)
            tmp = self.readTemp()
            h1 = hashlib.md5(tmp.encode()).hexdigest()
            original = self.read(self.companyLst[i])
            h2 = hashlib.md5(original.encode()).hexdigest()
            if h1 != h2:
                print('Updated')
                self.write(self.companyLst[i], htmlcode)
            else:
                print('No Update')

    def read(self, companyName):
        try:
            filename = 'local/' + companyName +'Html.txt'
            with open(filename, 'r') as f:
                result = f.read()
                return result
        except FileNotFoundError:
            self.write(companyName,'New Company')
            result = self.read(companyName)
            return result

    def readTemp(self):
        filename = 'local/temp.txt'
        with open(filename, 'r') as f:
            result = f.read()
            return result

    def write(self, companyName, htmlcode):
        filename = 'local/' + companyName +'Html.txt'
        with open(filename, 'w') as f:
            f.write(htmlcode)

    def writeTemp(self, htmlcode):
        filename = 'local/temp.txt'
        with open(filename, 'w') as f:
            f.write(htmlcode)

    def request(self, url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        req = urllib.request.urlopen(req).read()
        return req

if __name__ == '__main__':
    filename = 'local/companyURL.csv'
    with open(filename, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        search = JobSearch(reader)
        search.check()