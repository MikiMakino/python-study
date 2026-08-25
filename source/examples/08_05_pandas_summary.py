import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=10)
response.raise_for_status()
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_list = []

for book in books:
    title = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(price_text.replace("£", ""))
    book_list.append({"title": title, "price": price})

df = pd.DataFrame(book_list)

print(df.head())
print("冊数:", len(df))
print("平均価格: £{:.2f}".format(df["price"].mean()))
print("最高価格: £{:.2f}".format(df["price"].max()))
print("最安価格: £{:.2f}".format(df["price"].min()))
