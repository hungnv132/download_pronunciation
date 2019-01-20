# -*- coding: utf-8 -*-
import scrapy
from download_pronunciation.utils import (
    get_downloaded_folder_path, get_file_name_from_url
)


class PronunciationSpider(scrapy.Spider):
    name = "pronunciation_spider"
    user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36" \
                 " (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

    def start_requests(self):
        urls = [
            "https://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page=1",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for word in response.css('ul.wordlist-oxford3000>li'):
            detail_word_url = word.css('a::attr(href)').extract_first()
            yield scrapy.Request(detail_word_url, callback=self.get_audio_url)

        for next_page in response.css('#paging ul li > a'):
            yield response.follow(next_page, self.parse)

    def get_audio_url(self, response):
        for audio in response.css('.icon-audio')[:2]:
            audio_url = audio.css('::attr(data-src-mp3)').extract_first()
            yield scrapy.Request(audio_url, callback=self.save_pronunciation)

    def save_pronunciation(self, response):
        audio_file_name = get_file_name_from_url(response.url)
        audio_file_path = "{}/{}".format(get_downloaded_folder_path(),
                                         audio_file_name)
        with open(audio_file_path, "wb") as f:
            f.write(response.body)
