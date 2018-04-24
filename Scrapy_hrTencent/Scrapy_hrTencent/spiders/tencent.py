# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyHrtencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com/position.php?keywords=python']
    start_urls = ['https://hr.tencent.com/position.php']

    custom_settings = {'DOWNLOAD_DELAY':3,}

    def parse(self, response):

        for sel in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            tencent = ScrapyHrtencentItem()
            position_url = sel.xpath('./td[1]/a/@href').extract_first()
            position_name = sel.xpath('./td[1]/a/text()').extract_first()
            position_type = sel.xpath('./td[2]/text()').extract_first()
            position_num = sel.xpath('./td[3]/text()').extract_first()
            position_site = sel.xpath('./td[4]/text()').extract_first()
            position_time = sel.xpath('./td[5]/text()').extract_first()

            url = response.urljoin(position_url)
            tencent["position_url"] = url
            tencent["position_name"] = position_name
            tencent["position_type"] = position_type
            tencent["position_num"] = position_num
            tencent["position_site"] = position_site
            tencent["position_time"] = position_time

            yield tencent

        next_url = response.css("a#next::attr(href)").extract_first()
        if next_url:
            next_page = response.urljoin(next_url)
            yield scrapy.Request(url=next_page,callback=self.parse,dont_filter=True)