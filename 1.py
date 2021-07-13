import  requests
import  json
import pandas as pd 
from bs4 import BeautifulSoup

class Cshopify():
    def __init__(self) -> None:
        self.product_list =  []
        self.count = 0

    def extract(self, url):
        r = requests.get(url)
        data = r.json()

        for item in data['products']:
            title = item['title']
            handle = item["handle"]
            created_at = item['created_at']
            product_type = item['product_type']

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
                    'title' : title,
                    'handle' : handle,
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
        url = "https://www.shopistores.com/search/jewellery/"

        for i in range(1, 960):
            self.geturls(url+str(i))

        

if __name__=="__main__":
    cls = Cshopify()

    #cls.extract("https://helmboots.com/products.json?limit=10000#page=1")
    #cls.test("https://www.ukecigstore.com/products.json?limit=10000#page=1")
    #cls.test("https://helmboots.com/products.json?limit=10000#page=1")
    #cls.save_csv()

    cls.dongu()
