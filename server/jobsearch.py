# -*- coding: utf-8 -*-
import sys
import csv

from bs4 import BeautifulSoup
import urllib.request

class JobSearch:
    def __init__(self, reader):
        self.reader = reader
        self.company = []
        self.urls = []
        self.name = []
        self.previous = []
        self.contact = []
        self.update = []

    def export(self):
        self.update.append(next(self.reader))
        for line in self.reader:
            self.update.append(line)
            self.company.append(line[0])
            self.urls.append(line[1])
            self.name.append(line[2])
            self.previous.append(line[3])
            self.contact.append(line[4])

    def write(self, filename):
         with open(filename, 'w') as f:
             writer = csv.writer(f)
             for i in range(len(self.update)):
                writer.writerow(self.update[i])
             
    def check(self):
        self.export()
        for i in range(len(self.company)):
            req = urllib.request.Request(self.urls[i], headers={'User-Agent': 'Mozilla/5.0'})
            req = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(req, 'html.parser')
            result = self.find(soup, self.name[i], i)
            word = str(result.get_text("", strip = True))
            if word != self.previous[i]:
                print("A new opening at " + self.company[i])
                self.update[i+1][3] = word
            else:
                print("No Update at " + self.company[i])
    
    def find(self, soup, name, i):
        if name.startswith('iframe'):
            iframe = soup.find('iframe')
            response = urllib.request.Request(iframe.attrs['src'], headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(response).read()
            iframe_soup = BeautifulSoup(response)
            return iframe_soup.find(class_ = self.name[i][6:])
        else:
            return soup.find(class_= self.name[i])


if __name__ == '__main__':
    filename = 'local/userinfo.csv'
    with open(filename, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        search = JobSearch(reader)
        search.check()
    search.write(filename)