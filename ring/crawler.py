"""Crawler for ring.

Responsible for
"""
import config, models

class Crawler(object):

    def __init__(self):
        self.feeds = models.all_feeds()

    def crawl(self):
        for source in self.feeds:
            print "Crawling", source
            source.crawl()

def main():
    crawler = Crawler()
    crawler.crawl()

if __name__ == '__main__':
    main()
