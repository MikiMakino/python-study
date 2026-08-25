from pathlib import Path

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"


def fetch_books(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")

    books = []
    for article in articles:
        title = article.h3.a["title"]
        price_text = article.find("p", class_="price_color").text
        price = float(price_text.replace("£", ""))
        books.append({"title": title, "price": price})

    return books


def summarize(df):
    print("冊数:", len(df))
    print("平均価格: £{:.2f}".format(df["price"].mean()))
    print("最高価格: £{:.2f}".format(df["price"].max()))
    print("最安価格: £{:.2f}".format(df["price"].min()))


def main():
    books = fetch_books(URL)
    df = pd.DataFrame(books)

    print(df.head())
    summarize(df)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"{Path(OUTPUT_FILE).resolve()} に保存しました")


if __name__ == "__main__":
    main()
