# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyHrtencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位的url
    position_url = scrapy.Field()
    #职位的名称
    position_name = scrapy.Field()
    #职位的类型
    position_type = scrapy.Field()
    #招聘的人数
    position_num = scrapy.Field()
    #工作的地点
    position_site = scrapy.Field()
    #发步的时间
    position_time = scrapy.Field()

    def get_insert_sql(self):

        insert_sql = """
            insert into position (url,name,type,num,site,time) VALUES (%s,%s,%s,%s,%s,%s)
        """

        params = (self["position_url"],self["position_name"],self["position_type"],self["position_num"],self["position_site"],self["position_time"])

        return insert_sql,params