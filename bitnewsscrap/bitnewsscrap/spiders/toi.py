
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from bitnewsscrap.items import BitnewsscrapItem


class MySpider(CrawlSpider):
    name = "toi-india"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider2(CrawlSpider):
    name = "toi-world"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider3(CrawlSpider):
    name = "toi-business"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider4(CrawlSpider):
    name = "toi-cricket"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/4719161.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items


class MySpider5(CrawlSpider):
    name = "toi-sports"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider6(CrawlSpider):
    name = "toi-tech"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/5880659.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider7(CrawlSpider):
    name = "toi-health"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/3908999.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider8(CrawlSpider):
    name = "toi-edu"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/913168846.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider9(CrawlSpider):
    name = "toi-entertainment"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class MySpider10(CrawlSpider):
    name = "toi-lifestyle"
    allowed_domains = ["timesofindia.indiatimes.com"]
    start_urls = [
                    "http://timesofindia.indiatimes.com/rssfeeds/2886704.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

############################Economic Times Spiders############################

class EtSpider1(CrawlSpider):
    name = "et-industry"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/industry/rssfeeds/13352306.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items


class EtSpider2(CrawlSpider):
    name = "et-tech"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class EtSpider3(CrawlSpider):
    name = "et-markets"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class EtSpider4(CrawlSpider):
    name = "et-economy"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/news/economy/rssfeeds/1373380680.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class EtSpider5(CrawlSpider):
    name = "et-smallbiz"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/small-biz/rssfeeds/5575607.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class EtSpider6(CrawlSpider):
    name = "et-magazines"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/magazines/rssfeeds/1466318837.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items
class EtSpider7(CrawlSpider):
    name = "et-wealth"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/wealth/rssfeeds/837555174.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items

class EtSpider8(CrawlSpider):
    name = "et-jobs"
    allowed_domains = ["economictimes.indiatimes.com"]
    start_urls = [
                    "http://economictimes.indiatimes.com/jobs/rssfeeds/107115.cms",
                ]

    def parse(self, response):
        items=[]
        titles = response.selector.xpath("//item")
        for title in titles:
            item = BitnewsscrapItem()
            item['title'] = title.xpath("title/text()").extract()
            item['description'] = title.xpath("description/text()").extract()
            item['link'] = title.xpath("link/text()").extract()
            item['pubdate'] = title.xpath("pubDate/text()").extract()
            items.append(item)
        return items
