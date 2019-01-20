import scrapy


class Word(scrapy.Spider):
    name = "new_word"

    def start_requests(self):
        urls = [
            "https://www.oxfordlearnersdictionaries.com/definition/english/behave",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sound in response.css('.icon-audio')[:2]:
            yield {'sound': sound.css('::attr(data-src-mp3)').extract_first()}
