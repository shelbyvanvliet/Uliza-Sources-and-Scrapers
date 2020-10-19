import scrapy
from ..items import DictScraperItem
# xpath for dict word: '//*[@id="post-16755"]/div/div/p[2]/span/b'
# xpath for link to word: '//*/h3/a/@href'
# change page/number to get to next page
# there are 726 pages in total

class DictSpiderSpider(scrapy.Spider):
    name = 'dict_spider'
    # allowed_domains = ['https://mytwidictionary.com']
    start_urls = ['https://mytwidictionary.com/page/1/?s&ht-kb-search=1&lang']
    pages = 726
    link_path = '//*/h3/a/@href'
    english_word_path = '//*/h3/a/text()'
    twi_word_path = '//*/b/text()'
    pos_path = '/html/body/div/div/div/main/div/article/div/div/p[1]/text()'

    def parse(self, response):
        for page in range(1,self.pages):
            page_url = f"https://mytwidictionary.com/page/{page}/?s&ht-kb-search=1&lang"
            yield response.follow(page_url, callback = self.parse_word_list)

    def parse_word_list(self, response):
            links = response.xpath(self.link_path).getall() 
            # english_words = response.xpath(self.english_word_path).getall()
            for link in links:
                yield response.follow(link, callback = self.parse_word)
    
    def parse_word(self, response):
        entry = DictScraperItem()
        english_word = response.url.split('/')[-2]
        print(english_word)
        twi_word = response.xpath(self.twi_word_path).get()
        pos = response.xpath(self.pos_path).get()

        entry["english"] = english_word
        entry["twi"] = twi_word
        entry["pos"] = pos
        return entry
