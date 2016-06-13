import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from bitnewsscrap.items import BitnewsscrapItem, BitnewsscrapItem2


class DainikSpider(CrawlSpider):
	name = "loksatta"
	allowed_domains = ["loksatta.com"]
	start_urls = (
		'http://www.loksatta.com/desh-videsh/',
	)

	def parse(self, response):
		items=[]
		titles = response.selector.xpath("//html/body/section/article/div[3]/div")
		for title in titles:
			item = BitnewsscrapItem2()
			item['title'] = title.xpath("h2/a/text()").extract()
			item['description'] = title.xpath("p/text()").extract()
			a=title.xpath("h2/a/@*[1]").extract()
			if not a:
				continue
			item['link'] = a
			for x in item['link']:
				if item['link']:
                			item['link'] = response.urljoin(x)
            		yield Request(item['link'], meta={'item': item},callback=self.parse_images)
  			items.append(item)

	def parse_images(self, response):
		item = response.request.meta['item']
		item['image'] = response.xpath("//*[@id='imgholder']/img/@*[1]").extract()
		item['pubdate'] = response.xpath("//*[@class='dateholder']/div[1]/p/span/@*[2]").extract()
		yield item

