# from parsel import Selector
# import requests


# response = requests.get("http://books.toscrape.com/")
# selector = Selector(text=response.text)
# # Extrai todos os preços da primeira página
# prices = selector.css(".product_price .price_color::text").re(r"£\d+\.\d{2}")
# print(prices)

# # substituir o método getall pelo método re, ou o método get por re_first.
# # Ambos, além de recuperar valores, aplicarão a expressão regular sobre
# # aquele valor.

# # £\d+\.\d{2} Expressao regular para "limpar" Â£26.08 -> £26.08

from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
selector = Selector(text=response.text)

# Extrai a descrição - verifica se tem o ...more
description = selector.css("#product_description ~ p::text").get()
print(description)

# "Fatiamos" a descrição removendo o sufixo
suffix = "...more"
if description.endswith(suffix):
    description = description[:-len(suffix)]
print(description)
