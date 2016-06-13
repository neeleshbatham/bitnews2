import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from bitnewsscrap.items import BitnewsscrapItem, BitnewsscrapItem2

class DainikSpider(CrawlSpider):
	name = "dainik"
	allowed_domains = ["bhaskar.com"]
	start_urls = (
		'http://www.bhaskar.com/rss-feed/2322/',
		'http://www.bhaskar.com/rss-feed/2338/'
	)

	def parse(self, response):
		items=[]
		titles = response.selector.xpath("//item")
		for title in titles:
			item = BitnewsscrapItem2()
			item['title'] = title.xpath("title/text()").extract()
			item['description'] = title.xpath("description/text()").extract()
			item['pubdate'] = title.xpath("pubDate/text()").extract()
			item['link'] = title.xpath("link/text()").extract()
			for x in item['link']:
				if item['link']:
                			item['link'] = response.urljoin(x)
            		yield Request(item['link'], meta={'item': item},callback=self.parse_images)
  			items.append(item)

	def parse_images(self, response):
		item = response.request.meta['item']
		item['image'] = response.xpath("//*[@id='image']/img/@*[2]").extract()
		yield item