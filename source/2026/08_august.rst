8月：はじめてのスクレイピング
==============================

テーマ
------

PythonでWebの情報を取ってみよう！―はじめてのスクレイピング

この回のねらい
--------------

7月は、pandas を使ってCSVデータを検証しました。

8月は、Webページから直接データを取ってくる **スクレイピング** に挑戦します。
次のことを練習します。

- ``requests`` でWebページを取得する
- ``BeautifulSoup`` でHTMLを解析する
- タイトルや価格など、必要な情報だけを取り出す
- 取り出した結果をリストに保存する
- ``pandas`` でデータをまとめて集計する
- 結果をCSVファイルに保存する

「Webページを見る → Pythonで情報を取る → データにする」
という流れを体験してみよう。


内容
----

1. 今日使うサイトを知る
~~~~~~~~~~~~~~~~~~~~~~~

今回は `Books to Scrape <https://books.toscrape.com/>`_ という書籍紹介サイトを使います。

このサイトは、スクレイピングの練習のために公開されているサンプルサイトです。
実在のオンライン書店ではなく、練習用のダミーデータが表示されています。

.. note::

   自分の練習以外の目的で、他の人のWebサイトの情報を無断で大量に取得すると、
   サイト運営者に迷惑をかけたり、利用規約に違反したりすることがあります。

   スクレイピングをするときは、次の点を確認しましょう。

   - そのサイトの利用規約でスクレイピングが許可されているか
   - ``robots.txt``（例： ``https://example.com/robots.txt``）で禁止されていないか

:nekochan:`memo-nya` マナーがあるニャ


2. 仮想環境を作る
~~~~~~~~~~~~~~~~~~

今回使うライブラリは、4月に作った ``python-study`` フォルダの中に、
仮想環境を作って入れていきます。作り方は4月と同じです。

``python-study`` フォルダに移動し、まだ ``.venv`` を作っていなければ作成します。

.. code-block:: bash

   python -m venv .venv

*Windows (PowerShell)*

.. code-block:: powershell

   .\.venv\Scripts\Activate.ps1

*Windows (コマンドプロンプト)*

.. code-block:: bat

   .venv\Scripts\activate.bat

*Mac/Linux*

.. code-block:: bash

   source .venv/bin/activate

有効化すると、ターミナルの先頭に ``(.venv)`` と表示されます。
以降のコマンドは、この仮想環境を有効化した状態で実行してください。

:nekochan:`yoshi-nya` 4月にやったのと同じだニャ


3. 必要なライブラリをインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

仮想環境を有効化した状態で、今回使うライブラリをインストールします。

- ``requests``：Webページを取得する
- ``beautifulsoup4``：取得したHTMLを解析する
- ``pandas``：データをまとめて集計・保存する

*Windows (PowerShell)*

.. code-block:: powershell

   python -m pip install requests beautifulsoup4 pandas

*Mac / Linux*

.. code-block:: bash

   python3 -m pip install requests beautifulsoup4 pandas

:nekochan:`yoshi-nya` まずはインストールから始めるニャ


4. 作業フォルダを作る
~~~~~~~~~~~~~~~~~~~~~~

5月と同じように、月ごとにフォルダを分けて整理します。
``python-study`` フォルダの中に、8月用のフォルダを作りましょう。

*Windows (PowerShell)*

.. code-block:: powershell

   Set-Location python-study
   New-Item -ItemType Directory 2026\08_book_scraper -Force
   Set-Location 2026\08_book_scraper

*Mac / Linux*

.. code-block:: bash

   cd python-study
   mkdir -p 2026/08_book_scraper
   cd 2026/08_book_scraper

こんな構成になります。

.. code-block:: text

   python-study/
   ├─ 2026/
   │  ├─ 05_ohanashi_register/
   │  │  └─ ohanashi_register.py
   │  └─ 08_book_scraper/
   └─ README.md

最後の ``Set-Location`` （``cd``）で、``08_book_scraper`` フォルダの中に移動しました。
このあとダウンロードするファイルは、このフォルダに入れてから実行していきます。
（次回以降にターミナルを開き直したときは、このフォルダまで移動してから作業を再開してください。）

:nekochan:`yoshi-nya` フォルダの中で作業していくニャ


5. まずはページを取得してみる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

いきなり情報を取り出すのではなく、まずはページが取得できるかを確認します。

:download:`08_01_fetch_page.py をダウンロード <../examples/08_01_fetch_page.py>`

.. literalinclude:: ../examples/08_01_fetch_page.py
   :language: python
   :caption: source/examples/08_01_fetch_page.py
   :linenos:

ダウンロードしたファイルを、今いる ``08_book_scraper`` フォルダに入れて実行します。

*Windows (PowerShell)*

.. code-block:: powershell

   Move-Item "$env:USERPROFILE\Downloads\08_01_fetch_page.py" .
   python 08_01_fetch_page.py

*Mac / Linux*

.. code-block:: bash

   mv ~/Downloads/08_01_fetch_page.py .
   python3 08_01_fetch_page.py

``requests.get(url)`` は、指定したURLにアクセスして、返ってきた内容を受け取る関数です。

``timeout=10`` を付けておくと、10秒たっても応答がない場合に処理を打ち切ってくれます。
これを付けないと、通信がうまくいかないときにプログラムが延々と固まってしまうことがあります。

``response.status_code`` が ``200`` なら、正常にページを取得できたことを表します。
``response.text`` には、ページのHTMLがそのまま文字列として入っています。

.. note::

   ``404`` はページが見つからない、``500`` はサーバー側のエラーを表します。
   ``200`` 以外が返ってきたときは、URLが正しいか、サイトが動いているかを確認しましょう。


6. タイトルを取り出す
~~~~~~~~~~~~~~~~~~~~~~

取得したHTMLの中から、本のタイトルだけを取り出してみます。

:download:`08_02_get_titles.py をダウンロード <../examples/08_02_get_titles.py>`

.. literalinclude:: ../examples/08_02_get_titles.py
   :language: python
   :caption: source/examples/08_02_get_titles.py
   :linenos:

ダウンロードしたファイルを、今いる ``08_book_scraper`` フォルダに入れて実行します。

*Windows (PowerShell)*

.. code-block:: powershell

   Move-Item "$env:USERPROFILE\Downloads\08_02_get_titles.py" .
   python 08_02_get_titles.py

*Mac / Linux*

.. code-block:: bash

   mv ~/Downloads/08_02_get_titles.py .
   python3 08_02_get_titles.py

``response.raise_for_status()`` は、``404`` や ``500`` のようにページの取得に失敗していた場合、
その場でエラーを発生させて処理を止めてくれます。
これを入れておかないと、失敗したページのまま解析を続けてしまい、
「タイトルが1件も取れない」など、原因が分かりにくい結果になってしまいます。

``BeautifulSoup(response.text, "html.parser")`` で、HTMLを解析しやすい形に変換します。

Books to Scrape では、1冊分の情報が ``<article class="product_pod">`` というタグに
まとまっています。``find_all()`` を使うと、条件に合うタグをすべてリストで取得できます。

タイトルは ``<h3><a title="...">`` の ``title`` 属性に入っているため、
``book.h3.a["title"]`` で取り出しています。

:nekochan:`yoshi-nya` ブラウザの「検証」機能でHTMLを見てみると分かりやすいニャ

.. note::

   ブラウザで対象ページを開き、右クリック →「検証」（Inspect）を選ぶと、
   実際のHTML構造を確認できます。どのタグに何が入っているか分からないときは、
   まずここを見てみましょう。


7. 価格も取り出す
~~~~~~~~~~~~~~~~~~

タイトルと合わせて、価格も取り出してみます。

:download:`08_03_get_titles_and_prices.py をダウンロード <../examples/08_03_get_titles_and_prices.py>`

.. literalinclude:: ../examples/08_03_get_titles_and_prices.py
   :language: python
   :caption: source/examples/08_03_get_titles_and_prices.py
   :linenos:

ダウンロードしたファイルを、今いる ``08_book_scraper`` フォルダに入れて実行します。

*Windows (PowerShell)*

.. code-block:: powershell

   Move-Item "$env:USERPROFILE\Downloads\08_03_get_titles_and_prices.py" .
   python 08_03_get_titles_and_prices.py

*Mac / Linux*

.. code-block:: bash

   mv ~/Downloads/08_03_get_titles_and_prices.py .
   python3 08_03_get_titles_and_prices.py

価格は ``<p class="price_color">`` というタグの中にテキストとして入っています。

``book.find("p", class_="price_color")`` で、その本の中にある価格タグを1つだけ探し、
``.text`` で中の文字列（例： ``£51.77``）を取り出しています。

``response.encoding = response.apparent_encoding`` を追加しているのは、
``£`` のような記号がそのままだと文字化けすることがあるためです。
これを入れておくと、ページの文字コードを判定し直してくれます。

.. note::

   ``class`` はPythonの予約語（クラスを定義するときに使う言葉）なので、
   そのまま引数名には使えません。BeautifulSoupでは代わりに ``class_`` を使います。


8. 結果をリストに保存する
~~~~~~~~~~~~~~~~~~~~~~~~~~

取り出したタイトルと価格を、1冊ずつ辞書にして、リストにまとめます。

:download:`08_04_save_list.py をダウンロード <../examples/08_04_save_list.py>`

.. literalinclude:: ../examples/08_04_save_list.py
   :language: python
   :caption: source/examples/08_04_save_list.py
   :linenos:

ダウンロードしたファイルを、今いる ``08_book_scraper`` フォルダに入れて実行します。

*Windows (PowerShell)*

.. code-block:: powershell

   Move-Item "$env:USERPROFILE\Downloads\08_04_save_list.py" .
   python 08_04_save_list.py

*Mac / Linux*

.. code-block:: bash

   mv ~/Downloads/08_04_save_list.py .
   python3 08_04_save_list.py

``price_text.replace("£", "")`` で通貨記号を取り除き、
``float()`` で小数として扱えるように変換しています。

``book_list.append({...})`` を1冊ごとに繰り返すことで、
最終的に「本のリスト」ができあがります。

:nekochan:`memo-nya` 1冊分は辞書、それが集まってリストになるニャ


9. pandasで集計する
~~~~~~~~~~~~~~~~~~~~

リストにまとめたデータを、pandasのDataFrameに変換して集計します。

:download:`08_05_pandas_summary.py をダウンロード <../examples/08_05_pandas_summary.py>`

.. literalinclude:: ../examples/08_05_pandas_summary.py
   :language: python
   :caption: source/examples/08_05_pandas_summary.py
   :linenos:

ダウンロードしたファイルを、今いる ``08_book_scraper`` フォルダに入れて実行します。

*Windows (PowerShell)*

.. code-block:: powershell

   Move-Item "$env:USERPROFILE\Downloads\08_05_pandas_summary.py" .
   python 08_05_pandas_summary.py

*Mac / Linux*

.. code-block:: bash

   mv ~/Downloads/08_05_pandas_summary.py .
   python3 08_05_pandas_summary.py

``pd.DataFrame(book_list)`` で、辞書のリストを表形式のデータに変換します。

``df["price"].mean()``・``.max()``・``.min()`` を使うと、
価格の平均・最高・最安を、それぞれ1行で計算できます。

7月に学んだ ``groupby`` などと同じように、
pandasを使うと、まとめて計算する処理が短く書けます。


10. CSVに保存する
~~~~~~~~~~~~~~~~~

集計したデータを、あとで見返せるようにCSVファイルへ保存します。

:download:`08_06_save_csv.py をダウンロード <../examples/08_06_save_csv.py>`

.. literalinclude:: ../examples/08_06_save_csv.py
   :language: python
   :caption: source/examples/08_06_save_csv.py
   :linenos:

ダウンロードしたファイルを、今いる ``08_book_scraper`` フォルダに入れて実行します。

*Windows (PowerShell)*

.. code-block:: powershell

   Move-Item "$env:USERPROFILE\Downloads\08_06_save_csv.py" .
   python 08_06_save_csv.py

*Mac / Linux*

.. code-block:: bash

   mv ~/Downloads/08_06_save_csv.py .
   python3 08_06_save_csv.py

``df.to_csv("books.csv", index=False, encoding="utf-8-sig")`` で、
DataFrameの内容をCSVファイルに書き出します。

``encoding="utf-8-sig"`` を指定しておくと、Excelで開いたときに文字化けしにくくなります。

実行すると、スクリプトと同じフォルダに ``books.csv`` が作成されます。


11. 完成版をダウンロードしよう
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここまでの内容を1つの完成版としてまとめました。

:download:`08_07_book_scraper.py をダウンロード <../examples/08_07_book_scraper.py>`

ダウンロードしたファイルは、今いる ``08_book_scraper`` フォルダに入れて使います。
ファイル名は ``book_scraper.py`` に変更しても、そのまま使えます。

:nekochan:`kochira-nya` 完成版はこちらニャ

.. literalinclude:: ../examples/08_07_book_scraper.py
   :language: python
   :caption: source/examples/08_07_book_scraper.py
   :linenos:


12. 実行してみよう
~~~~~~~~~~~~~~~~~~~

*Windows (PowerShell)*

.. code-block:: powershell

   Copy-Item "$env:USERPROFILE\Downloads\08_07_book_scraper.py" book_scraper.py
   python book_scraper.py

*Mac / Linux*

.. code-block:: bash

   cp ~/Downloads/08_07_book_scraper.py book_scraper.py
   python3 book_scraper.py

たとえば、次のように動きます。

.. code-block:: text

                                       title  price
   0                       A Light in the ...  51.77
   1                       Tipping the Velvet  53.74
   2                               Soumission  50.10
   3                            Sharp Objects  47.82
   4  Sapiens: A Brief History of Humankind  54.23
   冊数: 20
   平均価格: £38.05
   最高価格: £57.25
   最安価格: £13.99
   C:\...\08_book_scraper\books.csv に保存しました

.. note::

   価格はサイトの表示にあわせてポンド（£）のまま扱っています。
   ``float`` は計算を繰り返すとごくわずかな誤差が出ることがあるため、
   実際の家計簿アプリなどで金額を扱う場合は、通貨や端数の扱いにあわせて
   整数（円）で扱う、または ``decimal.Decimal`` を使うなど、
   用途に応じたルールを決めましょう。


13. エラーメッセージの見方
~~~~~~~~~~~~~~~~~~~~~~~~~~

スクレイピングでよく出会うエラーには、次のようなものがあります。

:nekochan:`memo-nya` エラーは直す場所を教えてくれるヒントだニャ

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - 最後の1行
     - よくある原因
   * - ``ModuleNotFoundError``
     - ``requests`` や ``bs4``、``pandas`` が未インストール。pipを実行したか確認
   * - ``ConnectionError``
     - ネットワークが繋がっていない、URLの入力ミス
   * - ``AttributeError: 'NoneType' object has no attribute ...``
     - ``find()`` で目的のタグが見つからず、``None`` が返ってきている
   * - ``ValueError: could not convert string to float``
     - 通貨記号など、数字以外の文字が混ざったまま ``float()`` しようとしている

特に ``AttributeError`` は、サイトのHTML構造が想定と違うときによく出ます。
そのときは、ブラウザの「検証」機能で、実際のタグ名やクラス名を見直してみましょう。


14. どこを見ればよいか
~~~~~~~~~~~~~~~~~~~~~~~

完成版のコードでは、次の点に注目して読んでみましょう。

- ``fetch_books()``
  ページの取得からデータの抽出まで、スクレイピングの本体部分を担当しています。
- ``summarize()``
  集計してターミナルに表示する部分を担当しています。
- ``main()``
  取得 → 集計 → 保存という、全体の流れをまとめています。
- ``if __name__ == "__main__":``
  このファイルを直接実行したときだけ ``main()`` を動かす書き方です。5月と同じですね。

.. note::

   ここまでの例では ``url`` と小文字で書いていましたが、完成版では ``URL`` と大文字にしています。
   Pythonでは、途中で書き換えないファイル全体の設定値（定数）を大文字で書く慣習があります。
   一方、``fetch_books(url)`` の引数 ``url`` は関数の中だけで使う値なので、これまでどおり小文字のままです。


15. Gitで記録しよう
~~~~~~~~~~~~~~~~~~~~

今回のプログラムも、Gitに記録してみましょう。
``08_book_scraper`` フォルダの中にいる状態のまま、次のコマンドを実行します。

*Windows (PowerShell / コマンドプロンプト)*

.. code-block:: powershell

   git status
   git add book_scraper.py
   git commit -m "Add book_scraper.py"

*Mac / Linux*

.. code-block:: bash

   git status
   git add book_scraper.py
   git commit -m "Add book_scraper.py"

.. note::

   ``books.csv`` はスクレイピングのたびに再生成できるファイルです。
   記録するかどうかは好みですが、記録したくない場合は ``.gitignore`` に
   ``books.csv`` を追加しておくと、毎回 ``git status`` に表示されなくなります。


課題
----

余裕があれば、次のどれかを追加してみましょう。

:nekochan:`yossha-nya` 1つだけ変えるところからで大丈夫ニャ

- 価格が一定額（たとえば £30）以上の本だけを表示してみる
- タイトルの文字数が長い順に並べ替えてみる
- 星の評価（``star-rating`` クラス）も一緒に取得してみる
- 2ページ目（``catalogue/page-2.html``）のデータも取得してみる
- 取得件数やエラー時のメッセージを、もう少し親切な表示にしてみる

実務で使うのはこんな場面
----------------------

- 自社サイトや自社が管理するページの棚卸
- 定期的にコピペしていた作業の自動化（毎日／毎週、同じ形式のページから同じ項目を目視で拾ってExcelに転記しているみたいな作業）
- 社内システムやイントラのページ（自社権限で見られる情報を決まった形式で定期的に集計したい）


おつかれさまでしたー :nekochan:`huhuhu-nya`


本日の参考資料
---------------

- `Books to Scrape <https://books.toscrape.com/>`_
- `requests 公式ドキュメント <https://requests.readthedocs.io/>`_
- `Beautiful Soup 公式ドキュメント <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
- `pandas 公式ドキュメント <https://pandas.pydata.org/docs/>`_
