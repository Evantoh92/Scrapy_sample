import scrapy
from chubby.items import ChubbyItem

class ChubbySpider(scrapy.Spider):
    name = "chubby"
    start_urls = [
        "http://www.chubbygrub.com/"
    ]

    def parse(self, response): # Define parse() function. 
        for url in response.xpath('/html/body/div[4]/div/div/div/a/@href'):
            yield response.follow(url, self.parse_author)

    def parse_author(self, response):
        items = []
        for i in response.xpath('//*[@id="items"]/tbody/tr'):
            item = ChubbyItem()
            item['calories'] = i.xpath('./td[3]/text()').get()
            item['name'] = i.xpath('./td[1]/text()').get()
            item['carbs'] = i.xpath('./td[5]/text()').get()
            item['category'] = i.xpath('./td[2]/a/text()').get()
            item['restaurant'] = response.xpath('/html/body/div[2]/div[1]/div/div/h1/span/text()').get()
            items.append(item)
        return items

        '''from chubby.items import ChubbyItem
            for sel in response.xpath('/html/body/div[4]/div/div/div/a'): #try out using the helper first
                item = ChubbyItem()
                item['restaurant'] = sel.xpath("./text()").extract() #the . is impt
                item['slug'] = sel.xpath("./@href").get()
            return items.append(item)
            item['calories']
            item['carbs']
            item['category']
            item['fat']
            item['name']
            item['restaurant']
            items.append(item)
            for sel in response.xpath("//div/a"):
            item = ChubbyItem()
            item['restaurant'] = sel.xpath('//a/text()').extract()
        return item''' 