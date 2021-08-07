import  requests
import  json
import pandas as pd 
from bs4 import BeautifulSoup

import html2text
h = html2text.HTML2Text()
h.ignore_links = True

class TekShopifyScrape():
    def __init__(self) -> None:
        self.product_list =  []
        self.count = 0

    def extractWebPages(self, url):
        r = requests.get(url)
        data = r.json()

        for item in data['products']:
            title = item['title']
            handle = item["handle"]
            body_html = h.handle(item['body_html'])
            saf_body = item['body_html']
            product_type = item['product_type']
            published_at = item['published_at']
            created_at = item['created_at']
            updated_at = item['updated_at']
            product_url = "https://completedworks.com" + '/products/' + item['handle']

            for image in item['images']:
                try:
                    imagesrc = image['src']
                except:
                    imagesrc = 'None'

            for variant in item['variants']:
                price = variant['price']
                sku = variant['sku']
                available = variant['available']
                print(price, available)

                product  = {
                    'web site' : url[:-32],
                    'title' : title,
                    'handle' : handle,
                    'body_html': body_html,
                    'saf_body': saf_body,
                    'published_at' : published_at,
                    'updated_at' : updated_at,
                    'created_at' : created_at,
                    'product_type' : product_type,
                    'price' : price,
                    'sku' : sku,
                    'available' : available,
                    'image' : imagesrc,
                    'product_url' : product_url
                    
                }

                self.product_list.append(product)

    def save_csv(self):
        df = pd.DataFrame(self.product_list)
        df.to_csv("product_list_test.csv")


class Cshopify():
    def __init__(self) -> None:
        self.product_list =  []
        self.count = 0

    def extractWebPages(self, url):
        r = requests.get(url)
        data = r.json()

        for item in data['products']:
            title = item['title']
            handle = item["handle"]
            body_html = h.handle(item['body_html'])
            product_type = item['product_type']
            published_at = item['published_at']
            created_at = item['created_at']
            updated_at = item['updated_at']

            for image in item['images']:
                try:
                    imagesrc = image['src']
                except:
                    imagesrc = 'None'

            for variant in item['variants']:
                price = variant['price']
                sku = variant['sku']
                available = variant['available']
                print(price, available)

                product  = {
                    'web site' : url[:-32],
                    'title' : title,
                    'handle' : handle,
                    'body_html': body_html,
                    'published_at' : published_at,
                    'updated_at' : updated_at,
                    'created_at' : created_at,
                    'product_type' : product_type,
                    'price' : price,
                    'sku' : sku,
                    'available' : available,
                    'image' : imagesrc
                }

                self.product_list.append(product)

    def save_csv(self):
        df = pd.DataFrame(self.product_list)
        df.to_csv("product_list.csv")

    def test(self, url):
        r = requests.get(url)
        data = r.json()

        count=0
        for item in data['products']:
            title = item['title']
            handle = item["handle"]
            body_html = item['body_html']
            product_type = item['product_type']
            published_at = item['published_at']
            created_at = item['created_at']
            updated_at = item['updated_at']
            vendor = item['vendor']
            tags = item['tags']
            options = item['options']

            print(item['images'])
            for var in item['variants']:
                print(var['price'])
            #count +=1
            #print(count)

    def geturls(self, url):
        page = requests.get(url)
        print(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tablos = soup.find(id="content-container-tbl")

        for row in tablos.select('tbody tr'):
            row_text = [x.text  for x in row.find_all('td')]
            data = ', '.join(row_text).split(",")

            all_a = row.select('.text-center a')
            for a in all_a:
                if a['title'] == "United Kingdom":
                    #print(a['title'])
                    for i in  data[2].split("\n"):
                        if ".com" in i:
                            shopifyurljson = "https://"+i.strip()+"/products.json?limit=10000#page=1"
                            shopifyurl = shopifyurljson[:-32]
                            self.count +=1
                            print(shopifyurl)
                            print(self.count)

    def dongu(self):
        #url="https://www.shopistores.com/search/vegan%20food/" #vegan food
        #url="https://www.shopistores.com/search/beauty/"
        #url = "https://www.shopistores.com/search/jewellery/"
        #url = "https://www.shopistores.com/search/cbd/"
        url = "https://www.shopistores.com/search/cosmetics/"

        for i in range(1, 960):
            self.geturls(url+str(i))

            

        #print(soup.find('table', { 'class' : 'table' }).text)

if __name__=="__main__":
    #cls = Cshopify()
    #cls.dongu()

    tekcls = TekShopifyScrape()
    tekcls.extractWebPages("https://completedworks.com/products.json?limit=10000#page=1")
    #tekcls.extractWebPages("https://tortware.com/products.json?limit=10000#page=1")
    tekcls.save_csv()

    
