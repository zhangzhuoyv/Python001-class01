# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class MoviesItem(Item):
    movie_name = Field()
    movie_type = Field()
    movie_time = Field()