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
        self.classname = []
        self.original = []
        self.contact = []
        self.update = []

    def export(self):
        self.update.append(next(self.reader))
        for line in self.reader:
            self.update.append(line)
            self.company.append(line[0])
            self.urls.append(line[1])
            self.classname.append(line[2])
            self.original.append(line[3])
            self.contact.append(line[4])

    def write(self):
         with open('local/userinfo.csv', 'w') as f:
             writer = csv.writer(f)
             for i in range(len(self.update)):
                writer.writerow(self.update[i])
             
    def check(self):
        self.export()
        for i in range(len(self.company)):
            req = urllib.request.urlopen(self.urls[i])
            soup = BeautifulSoup(req, 'html.parser')
            result = soup.find(class_= self.classname[i])
            word = str(result.get_text("", strip = True))
            if word != self.original[i]:
                print("A new opening " + word + " at " + self.company[i])
            else:
                print("No Update at " + self.company[i])
        self.write()

if __name__ == '__main__':
    with open('local/userinfo.csv', 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        search = JobSearch(reader)
        search.check()
