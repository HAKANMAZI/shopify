import  requests
import  json

url = "https://helmboots.com/products.json"
r = requests.get(url)
data = r.json()



for item in data['products']:
    item = item['title']
    handle = item["handle"]
    print(handle)
    created_at = item['created_at']
    product_type = item['product_type']
    for variant in item['variants']:
        price = variant['price']
        sku = variant['sku']
        available = variant['available']
        print(price)