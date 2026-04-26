5月：Python基礎① おはなしレジアプリを作ろう
==============================================

テーマ
------

入力・計算・条件分岐・関数を使って、売上計算アプリを作る

この回のねらい
--------------

4月は、Python を実行するところと Git の最初の使い方を体験しました。

5月は、実際に「動くアプリ」を1本作りながら、次のことを練習します。

- ``input()`` を使って入力を受け取る
- 数字を ``int()`` で整数に変換する
- 変数に値を入れて、計算に使う
- ``if`` を使って条件によって処理を変える
- 関数にまとめて、読みやすいプログラムにする
- ファイルを実行し、Git で記録する


内容
----

1. 今日作るもの
~~~~~~~~~~~~~~~

今日のテーマは、**おはなしレジアプリ** です。

本屋さんや雑貨屋さんのレジをイメージして、
商品名・値段・個数・会員かどうかを入力すると、
合計金額を表示するプログラムを作ります。

今回のアプリでは、次のルールにします。

- 小計 = 値段 × 個数
- 会員なら 10% 引き
- 3個以上買ったら、まとめ買い割引でさらに 100 円引き
- 最後に、お客さん向けのメッセージを表示する

1本のプログラムの中で、
**入力 → 計算 → 条件分岐 → 表示**
という流れをまとめて体験できます。


2. まずは計算だけ試してみる
~~~~~~~~~~~~~~~~~~~~~~~~~~~

いきなり全部を作るのではなく、最初は簡単な計算だけ試してみましょう。

.. code-block:: python

   price = 1200
   quantity = 2
   subtotal = price * quantity

   print(subtotal)

このプログラムでは、
``price`` に値段、``quantity`` に個数を入れて、
``subtotal`` で小計を計算しています。

``print(subtotal)`` を実行すると、 ``2400`` と表示されます。

このように、Python では途中の結果を変数に入れておくと、
あとから計算や表示に使いやすくなります。


3. 入力を受け取ってみる
~~~~~~~~~~~~~~~~~~~~~~~

次に、お店の人が入力できるようにしてみます。

.. code-block:: python

   item_name = input("商品名を入力してください: ")
   price = int(input("1つの値段を入力してください: "))
   quantity = int(input("個数を入力してください: "))

   subtotal = price * quantity

   print(f"{item_name} の小計は {subtotal} 円です")

``input()`` は、キーボードから入力された内容を受け取る関数です。

ただし、``input()`` の結果は文字列として扱われます。
そのため、値段や個数のように計算したい値は ``int()`` で整数に変換します。

.. note::

   ``int`` は integer（整数）の略です。
   もし ``int()`` を付けずに計算しようとすると、
   数字ではなく文字として扱われ、思ったように計算できません。


4. 条件によって値引きを変える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

会員なら 10% 引き、そうでなければ値引きなしにしてみましょう。

.. code-block:: python

   member_answer = input("会員ですか？ (y/n): ").strip().lower()

   if member_answer == "y":
       discount = int(subtotal * 0.1)
   else:
       discount = 0

   total = subtotal - discount

   print(f"値引き額は {discount} 円です")
   print(f"お会計は {total} 円です")

``if`` は、条件によって処理を分けるための書き方です。

- ``member_answer == "y"`` が本当なら、10% 引き
- そうでなければ、``else`` のほうを実行

ここでは、入力された文字の前後の空白を消すために ``strip()`` を使い、
大文字・小文字の違いを減らすために ``lower()`` を使っています。

.. note::

   Python では、``:`` のあとに改行し、
   次の行を字下げして書くことで、どこまでが ``if`` の中かを表します。
   この字下げを **インデント** と呼びます。


5. 関数にまとめてみる
~~~~~~~~~~~~~~~~~~~~~

処理が長くなってきたら、関数に分けると読みやすくなります。

.. code-block:: python

   def calculate_total(price, quantity, is_member):
       subtotal = price * quantity

       if is_member:
           member_discount = int(subtotal * 0.1)
       else:
           member_discount = 0

       if quantity >= 3:
           bulk_discount = 100
       else:
           bulk_discount = 0

       total = subtotal - member_discount - bulk_discount
       return subtotal, member_discount, bulk_discount, total

``def`` は、関数を定義するときに使います。

この ``calculate_total()`` 関数は、
値段・個数・会員かどうかを受け取って、
小計、会員割引、まとめ買い割引、合計金額をまとめて返します。

関数にしておくと、あとで同じ計算をもう一度使いたいときにも便利です。


6. 作業フォルダはどう整理する？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

今後 8 月に GitHub へ push する予定があるなら、
**``python-study`` を1つの学習用リポジトリにして、月やテーマごとに階層化する** のがおすすめです。

たとえば、次のように整理すると見返しやすくなります。

.. code-block:: text

   python-study/
   ├─ 2026/
   │  ├─ 04_setup/
   │  │  └─ day.py
   │  └─ 05_ohanashi_register/
   │     └─ ohanashi_register.py
   └─ README.md

この形にしておくと、次のメリットがあります。

- 何月に何を作ったか分かりやすい
- 1つの Git リポジトリで学習履歴をまとめられる
- 8月に GitHub へ push するときに、そのまま成果物として見せやすい

5月のファイルは、``python-study`` の中に
``2026/05_ohanashi_register/ohanashi_register.py``
として保存してみましょう。


7. 完成版を見てみよう
~~~~~~~~~~~~~~~~~~~~~

この教材リポジトリでは、見本コードを
``source/examples/ohanashi_register.py`` に置いています。

自分で作るときは、作業用フォルダの
``2026/05_ohanashi_register/`` に
``ohanashi_register.py`` という名前で保存してみましょう。

.. literalinclude:: ../examples/ohanashi_register.py
   :language: python
   :caption: source/examples/ohanashi_register.py
   :linenos:


8. 実行してみよう
~~~~~~~~~~~~~~~~~

まずは、5月用の作業フォルダへ移動します。

*Windows (PowerShell)*

.. code-block:: powershell

   Set-Location python-study
   New-Item -ItemType Directory 2026\05_ohanashi_register -Force
   Set-Location 2026\05_ohanashi_register

*Mac / Linux*

.. code-block:: bash

   cd python-study
   mkdir -p 2026/05_ohanashi_register
   cd 2026/05_ohanashi_register

その場所に ``ohanashi_register.py`` を保存したら、次のように実行します。

*Windows (PowerShell / コマンドプロンプト)*

.. code-block:: powershell

   python ohanashi_register.py

*Mac / Linux*

.. code-block:: bash

   python3 ohanashi_register.py

この教材リポジトリに入っている見本コードを試す場合は、
リポジトリのルートで次のように実行できます。

*Windows (PowerShell / コマンドプロンプト)*

.. code-block:: powershell

   python source\examples\ohanashi_register.py

*Mac / Linux*

.. code-block:: bash

   python3 source/examples/ohanashi_register.py

たとえば、次のように動きます。

.. code-block:: text

   おはなしレジアプリへようこそ！
   お客さんの名前を入力してください: さくら
   商品名を入力してください: えほん
   1つの値段（円）を入力してください: 1200
   個数を入力してください: 3
   会員ですか？ (y/n): y

   --- お会計 ---
   さくらさん、ありがとうございます。
   商品: えほん
   区分: 会員
   小計: 3600円
   会員割引: -360円
   まとめ買い割引: -100円
   合計: 3140円
   またおはなしの世界へどうぞ！

9. GUI版も試してみよう
~~~~~~~~~~~~~~~~~~~~~~
 
CLI版が動いたら、同じアプリを **ウィンドウで動かす GUI 版** も試してみましょう。
 
ターミナルの代わりに、画面上の入力欄に文字を入力して Enter を押すと、
同じ会話の流れでお会計が表示されます。
 
.. image:: https://github.com/MikiMakino/100days-of-code/raw/main/day95-ohanashi-register-gui/README.md
   :alt: おはなしレジアプリ GUI版のスクリーンショット
 
GUI版のコードとセットアップ手順は、次の GitHub リポジトリに置いています。
 
   https://github.com/MikiMakino/100days-of-code/tree/main/day95-ohanashi-register-gui
 
``ohanashi_register_gui.py``・``README.md``・``requirements.txt`` の
3ファイルをそのままコピーして使ってかまいません。
 
コードをコピーして使った場合は、ぜひリポジトリの ☆ Star を押してもらえると嬉しいです。
 
CLI版との主な違いは次のとおりです。
 
- ``print()`` の代わりに、ScrolledText（スクロールできるテキストエリア）に追記する
- ``input()`` の代わりに、Entry ウィジェット（入力欄）と Enter キーで回答する
- 「今どの質問か」を ``step`` という変数で管理することで、会話の流れを再現している
 
計算ロジック（``calculate_total()``）は CLI 版と同じコードを使っています。


10. エラーメッセージの見方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プログラムを書いていて、エラーが出た時、
大切なのは、**「失敗した」ではなく「どこを直せばよいかのヒントが出た」** と考えることです。

たとえば、値段を入れる場面で文字を入力すると、次のようなエラーが出ます。

.. code-block:: text

   1つの値段を入力してください: りんご
   Traceback (most recent call last):
     File "ohanashi_register.py", line 6, in <module>
       price = int(input("1つの値段を入力してください: "))
   ValueError: invalid literal for int() with base 10: 'りんご'

このときは、次の順番で見ると分かりやすくなります。

- 最後の行  
  ``ValueError`` は「値の変換で困った」という意味です。
- その少し上の行  
  ``price = int(input(...))`` のところで起きたと分かります。
- ``line 6``  
  6行目を見直せばよいと分かります。

今回のレジアプリでよくあるのは、次のようなケースです。

- ``ValueError``  
  値段や個数に、数字ではない文字を入れてしまった
- ``IndentationError``  
  ``if`` や ``else`` の字下げがそろっていない
- ``SyntaxError``  
  ``:`` や ``"`` の付け忘れなどで、文の形が正しくない

全部を読む必要はありません。
**まずは最後の行のエラー名を見る → 何行目かを見る → その行の前後を直す**
という順番で十分です。


11. どこを見ればよいか
~~~~~~~~~~~~~~~~~~~~~~

完成版のコードでは、次の点に注目して読んでみましょう。

- ``main()``  
  入力から表示まで、全体の流れを書いています。
- ``calculate_total()``  
  合計金額を計算する部分を担当しています。
- ``member_label()``  
  ``True`` / ``False`` を、そのまま表示するのではなく、
  「会員」「一般」という分かりやすい表示に変えています。
- ``if __name__ == "__main__":``  
  このファイルを直接実行したときだけ、``main()`` を動かす書き方です。

最初はすべてを一度に理解しようとしなくて大丈夫です。
「入力して、計算して、条件で分けて、表示している」
という大きな流れをつかめれば十分です。


12. Gitで記録しよう
~~~~~~~~~~~~~~~~~~~

4月に続いて、今回のプログラムも Git に記録してみましょう。

``python-study`` のルートで実行するなら、次のように書けます。

*Windows (PowerShell / コマンドプロンプト)*

.. code-block:: powershell

   git status
   git add 2026\05_ohanashi_register\ohanashi_register.py
   git commit -m "Add おはなしレジアプリ"

*Mac / Linux*

.. code-block:: bash

   git status
   git add 2026/05_ohanashi_register/ohanashi_register.py
   git commit -m "Add おはなしレジアプリ"

``git status`` で状態を確認してから、
``git add`` で記録したいファイルを追加し、
``git commit`` で1つの変更として残します。


課題
----

余裕があれば、次のどれかを追加してみましょう。

- 会員割引を 10% ではなく 5% に変えてみる
- 5個以上買ったら、まとめ買い割引を 200 円にしてみる
- 最後のメッセージを好きな文に変えてみる
- 消費税を計算する変数を追加してみる
- ``input()`` の質問文を、自分のお店らしい表現に変えてみる

5月は、**自分で入力した値でプログラムが動く楽しさ** を味わう回です。
まずは完成版をそのまま動かし、
そのあとで少しずつ自分のアイデアを足してみましょう。
