"""import scrapy Module"""
import scrapy

class Audiocom1Spider(scrapy.Spider):
    '''Spider class'''
    name = "audiocom"
    allowed_domains = ["www.audiocom.no"]
    start_urls = ["https://www.audiocom.no/bilguide"]
  
    def parse(self, response):
        """it would scraping to the div of  attribute value='data-link'"""
        anchors = response.xpath("//div[@class='ArticleWithBackground Layout3Element']/@data-link").getall()
        for anchor in anchors:
            link="https://www.audiocom.no/bilguide"
            small_link =anchor.replace("https://www.audiocom.no/bilmerke-tilbeh%25C3%25B8r/","/")
            yield scrapy.Request(link+small_link.lower(), callback=self.parse_product,dont_filter = True)

    def parse_product(self, response):
        """it would scraping to the products"""
        scrapr_anchor=response.xpath(".//div[@class='AddProductImage']/a")
        yield from response.follow_all(scrapr_anchor, callback=self.parse_product_scrapy,dont_filter = True)
        
       
        inner_anchor=response.xpath(".//div[@id='ctl00_CPHCnt_WebPubArea3_Pnl_A100306F4523_Dsp_PGE100306F4523']//div[@class='textContent']/h3/a/@href").getall()
        for inner in inner_anchor:
            yield scrapy.Request(inner, callback=self.parse_product,dont_filter = True)

    
    def parse_product_scrapy(self, response):
        """it would scraping to the products"""
        # import pdb; import pdb;pdb.set_trace()
        img_1=[]
        img_2=[]
        img_3=[]
        img_4=[]
        img_5=[]
        img_6=[]
        img_7=[]
        img_8=[]
        img_9=[]
        img_10=[]
        img_11=[]
        img_12=[]
        img_13=[]
        img_14=[]
        img_15=[]
        img_16=[]
        img_17=[]
        all_image=response.xpath(".//div[@id='PanelProductInfo']//div[@id='1']//img/@src").getall()
        for i in range(len(all_image)+1):
            if i==1:
                img_1.append(all_image[0])
            elif i==2:
                img_2.append(all_image[1])
            elif i==3:
                img_3.append(all_image[2])
            elif i==4:
                img_4.append(all_image[3])
            elif i==5:
                img_5.append(all_image[4])
            elif i==6:
                img_6.append(all_image[5])
            elif i==7:
                img_7.append(all_image[6])  
            elif i==8:
                img_8.append(all_image[7])
            elif i==9:
                img_9.append(all_image[8])
            elif i==10:
                img_10.append(all_image[9])
            elif i==11:
                img_11.append(all_image[10])
            elif i==12:
                img_12.append(all_image[11])
            elif i==13:
                img_13.append(all_image[12])
            elif i==14:
                img_14.append(all_image[13])
            elif i==15:
                img_15.append(all_image[14])
            elif i==16:
                img_16.append(all_image[15])
            elif i==17:
                img_17.append(all_image[16])     
        current=response.xpath(".//div[@class='current-price-container']/span[1]/text()").get()
        old=response.xpath(".//span[@class='OldPriceLabel']/text()").get()          
        if current and old:
            discount_price=current
            Actual_price=old
        else:
            Actual_price=current
            discount_price=old
       
        yield{
               "product Id":response.css(".product-number-inner .prd-num-label::text").get(),
               "Main Category":response.xpath(".//div[@class='BreadCrumb']/a[1]/text()").get(),
               "Category 1":response.xpath(".//div[@class='BreadCrumb']/a[2]/text()").get(),
               "Category 2":response.xpath(".//div[@class='BreadCrumb']/a[3]/text()").get(),
               "Category 3":response.xpath(".//div[@class='BreadCrumb']/a[4]/text()").get(),
               "Category 4":response.xpath(".//div[@class='BreadCrumb']/a[5]/text()").get(),
               "Category 5":response.xpath(".//div[@class='BreadCrumb']/a[6]/text()").get(),
               "Brand":response.xpath(".//div[@class='BreadCrumb']/a[2]/text()").get(),
               "Product Name":response.xpath(".//h1/text()").get(),
               "Product Information":response.xpath(".//h2/text()").get(),
               "Main Price":Actual_price,
               "Discount Price":discount_price,
               "Product Discription":response.xpath(".//div[@class='product-description']//text()").getall(),
               "picture 1":''.join(img_1),
               "picture 2":''.join(img_2),
               "picture 3":''.join(img_3),
               "picture 4":''.join(img_4),
               "picture 5":''.join(img_5),
               "picture 6":''.join(img_6),
               "picture 7":''.join(img_7),
               "picture 8":''.join(img_8),
               "picture 9":''.join(img_9),
               "picture 10":''.join(img_10),
               "picture 11":''.join(img_11),
               "picture 12":''.join(img_12),
               "picture 13":''.join(img_13),
               "picture 14":''.join(img_14),
               "picture 15":''.join(img_15),
               "picture 16":''.join(img_16),
               "picture 17":''.join(img_17),
               "source":"www.audiocom.no",

             }
   