import pandas as pd
import requests

#url = "https://worldpopulationreview.com/countries/countries-by-gdp/#worldCountries"
url = "https://www.shopistores.com/search/vegan%20food/"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df = df_list[1]
df.to_csv("hakan.csv")
df.head()