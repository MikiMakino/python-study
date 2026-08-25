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

df.to_csv("books.csv", index=False, encoding="utf-8-sig")
print("books.csv に保存しました")
