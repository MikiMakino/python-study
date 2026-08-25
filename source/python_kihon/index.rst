Pythonの基本
==========================================

変数と型
--------

変数は「値に付ける名前」。 ``=`` は「等しい」ではなく「右の値を左の名前に入れる」

.. code-block:: python

   uriage = 12800          # 整数(int)
   ritsu = 0.1             # 小数(float)
   shiten = "東京"          # 文字列(str)。引用符で囲む
   print(uriage * 3)       # 38400

型がわからなくなったら ``type()`` で確認できます。

.. code-block:: python

   print(type(uriage))     # <class 'int'>

型の変換:

.. code-block:: python

   int("12800")            # 文字列 → 整数
   str(12800)              # 整数 → 文字列
   float("0.1")            # 文字列 → 小数

.. note::

   ``"12800"`` (文字列)と ``12800`` (数値)は別物です。
   ``"12800" + 100`` はエラーになります。CSVから読んだ数字が計算できないときは、
   たいてい「文字列のまま」なのが原因です。

文字列
------

.. code-block:: python

   name = "請求書_A社_202606.pdf"

   "請求書" in name                    # 含むか? → True(8月で使う)
   name.replace(".pdf", "")           # 置き換え → "請求書_A社_202606"
   name.split("_")                    # 分解 → ["請求書", "A社", "202606.pdf"]
   name.startswith("請求書")           # 〜で始まるか? → True

   f"合計は{uriage}円です"             # f-string:文字列に変数を埋め込む

リスト
------

複数の値を順番に並べて入れる箱

.. code-block:: python

   sizes = [3200, 45, 900, 12]

   len(sizes)              # 個数 → 4
   sizes.append(60)        # 末尾に追加
   sizes.sort()            # 小さい順に並べ替え
   sizes.sort(reverse=True)  # 大きい順
   sizes[0]                # 最初の要素(番号は0から!)
   sizes[:3]               # 最初の3個(トップ3の取り出しに使う)

辞書
----

「名前(キー)→ 値」の対応

.. code-block:: python

   counts = {".pdf": 12, ".xlsx": 7}

   counts[".pdf"]                     # pdfの値を取り出す → 12
   counts[".png"] = 3                 # .pngというキーと値を追加
   counts.get(".txt", 0)              # ".txt" がなければ、代わりに 0 を返す

   # 間違い例
   counts[".txt"]                     # キーがない場合はエラーになります。
   counts.get() を使うと、キーがない場合に返す値を指定できます。

  辞書を使って数える:

  辞書を使うと、同じ項目が何回出てきたかを数えられます。

.. code-block:: python

   counts = {}
   for item in [".pdf", ".xlsx", ".pdf"]:
       counts[item] = counts.get(item, 0) + 1
   # → {'.pdf': 2, '.xlsx': 1}

if文 —— 条件で分ける
--------------------

.. code-block:: python

   if uriage >= 100000:
       print("大口です")
   elif uriage >= 50000:
       print("中口です")
   else:
       print("小口です")

- 条件の行末に ``:`` を忘れない
- 中身は **半角スペース4つ** 下げる(この字下げがPythonの文法そのもの)

比較と組み合わせ:

.. code-block:: python

   a == b        # 等しい(=が2つ!)
   a != b        # 等しくない
   a >= b        # 以上
   "請求書" in name          # 含む
   4 <= month and month <= 6  # かつ

for文 —— 繰り返す
-----------------

.. code-block:: python

   for f in files:             # リストの中身を1つずつ取り出す
       print(f)

   for i in range(5):          # 0,1,2,3,4 と5回まわす
       print(i)

   for title, price in rows:   # 「1行=複数の値」をまとめて受け取る
       print(title, price)

if文と同じく、行末の ``:`` と字下げがセットです。
**「forで1つずつ取り出し、ifで選り分ける」** 

import —— お道具箱を開ける
------------------------

.. code-block:: python

   from pathlib import Path    # 標準ライブラリ:インストール不要
   import csv                  # 同上
   import pandas as pd         # 外部ライブラリ:pipでインストールが必要

- **標準ライブラリ** :Pythonに最初から付いてくる( ``pathlib``, ``csv``, ``datetime``, ``shutil`` )
- **外部ライブラリ** :あとから入れる( ``requests``, ``bs4``, ``pandas``, ``matplotlib`` )。
  ``python -m pip install ライブラリ名``
- ``as pd`` は「以後 ``pd`` と呼びます」という略称の宣言。 ``pd.read_csv`` のように使う

エラーの読み方
--------------

**最後の1行だけ** みてみる

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - 最後の1行
     - よくある原因
   * - ``IndentationError``
     - 字下げがずれている(スペースの数を確認)
   * - ``SyntaxError``
     - 書き間違い。 **全角スペース・全角記号の混入** が最多。 ``:`` 忘れも
   * - ``FileNotFoundError``
     - ファイルの保存場所違い。 ``.py`` とデータが同じフォルダにあるか確認
   * - ``NameError``
     - 変数名・関数名の打ち間違い(大文字小文字も区別されます)
   * - ``TypeError``
     - 型の不一致。文字列と数値を足そうとした、など
   * - ``ModuleNotFoundError``
     - ライブラリが未インストール。pipを実行したか確認

