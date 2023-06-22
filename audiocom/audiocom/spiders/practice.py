import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "practice"
    allowed_domains = ["www.audiocom.no"]
    start_urls = ["https://www.audiocom.no/bilguide/audi"]
    
    
    
    def parse(self, response):
        """it would scraping to the products"""
        link_all=response.xpath("//div[@id='ctl00_CPHCnt_WebPubArea3_Pnl_A100306F4523_Dsp_PGE100306F4523']//div[@class='textContent']/h3/a/@href").getall()
        for link in link_all:
            yield scrapy.Request(link, callback=self.parse_product)
    
    def parse_product(self, response):
        heading=response.xpath(".//div[@class='AddHeaderContainer']/a/@href").getall()
        for i in heading:
            url="https://www.audiocom.no"
            yield scrapy.Request (url+i, callback=self.parse_product_scrapy,dont_filter = True)
    def parse_product_scrapy(self, response):
        print(response)
        # yield {
        #     "name":response.xpath(".//h1/text()").get(),
        # }

