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

:nekochan:`yoshi-nya` まずは小さく動かしてみるニャ


2. まずは計算だけ試してみる
~~~~~~~~~~~~~~~~~~~~~~~~~~~

いきなり全部を作るのではなく、最初は簡単な計算だけ試してみましょう。

:download:`05_01_basic_calculation.py をダウンロード <../examples/05_01_basic_calculation.py>`

.. literalinclude:: ../examples/05_01_basic_calculation.py
   :language: python
   :caption: source/examples/05_01_basic_calculation.py
   :linenos:

ダウンロードしたファイルは、次のように実行できます。

*Windows (PowerShell)*

.. code-block:: powershell

   python "$env:USERPROFILE\Downloads\05_01_basic_calculation.py"

*Mac / Linux*

.. code-block:: bash

   python3 ~/Downloads/05_01_basic_calculation.py

このプログラムでは、
``price`` に値段、``quantity`` に個数を入れて、
``subtotal`` で小計を計算しています。

``print(subtotal)`` を実行すると、 ``2400`` と表示されます。

このように、Python では途中の結果を変数に入れておくと、
あとから計算や表示に使いやすくなります。


3. 入力を受け取ってみる
~~~~~~~~~~~~~~~~~~~~~~~

次に、お店の人が入力できるようにしてみます。

:download:`05_02_input_subtotal.py をダウンロード <../examples/05_02_input_subtotal.py>`

.. literalinclude:: ../examples/05_02_input_subtotal.py
   :language: python
   :caption: source/examples/05_02_input_subtotal.py
   :linenos:

ダウンロードしたファイルは、次のように実行できます。

*Windows (PowerShell)*

.. code-block:: powershell

   python "$env:USERPROFILE\Downloads\05_02_input_subtotal.py"

*Mac / Linux*

.. code-block:: bash

   python3 ~/Downloads/05_02_input_subtotal.py

``input()`` は、キーボードから入力された内容を受け取る関数です。

ただし、``input()`` の結果は文字列として扱われます。
そのため、値段や個数のように計算したい値は ``int()`` で整数に変換します。

:nekochan:`memo-nya` 入力された数字は、最初は文字として受け取られるニャ

.. note::

   ``int`` は integer（整数）の略です。
   もし ``int()`` を付けずに計算しようとすると、
   数字ではなく文字として扱われ、思ったように計算できません。


4. 条件によって値引きを変える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

会員なら 10% 引き、そうでなければ値引きなしにしてみましょう。
ここでは、前の計算で小計が ``2400`` 円になったとして試します。

:download:`05_03_member_discount.py をダウンロード <../examples/05_03_member_discount.py>`

.. literalinclude:: ../examples/05_03_member_discount.py
   :language: python
   :caption: source/examples/05_03_member_discount.py
   :linenos:

ダウンロードしたファイルは、次のように実行できます。

*Windows (PowerShell)*

.. code-block:: powershell

   python "$env:USERPROFILE\Downloads\05_03_member_discount.py"

*Mac / Linux*

.. code-block:: bash

   python3 ~/Downloads/05_03_member_discount.py

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

:download:`05_04_calculate_total_function.py をダウンロード <../examples/05_04_calculate_total_function.py>`

.. literalinclude:: ../examples/05_04_calculate_total_function.py
   :language: python
   :caption: source/examples/05_04_calculate_total_function.py
   :linenos:

ダウンロードしたファイルは、次のように実行できます。

*Windows (PowerShell)*

.. code-block:: powershell

   python "$env:USERPROFILE\Downloads\05_04_calculate_total_function.py"

*Mac / Linux*

.. code-block:: bash

   python3 ~/Downloads/05_04_calculate_total_function.py

``def`` は、関数を定義するときに使います。

この ``calculate_total()`` 関数は、
値段・個数・会員かどうかを受け取って、
小計、会員割引、まとめ買い割引、合計金額をまとめて返します。

最後の ``print(calculate_total(1200, 3, True))`` では、
返ってきた4つの値がまとめて表示されます。

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


7. 完成版をダウンロードしよう
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

完成版をダウンロードして、動きを見てみましょう。

:download:`05_05_ohanashi_register.py をダウンロード <../examples/05_05_ohanashi_register.py>`

ダウンロードしたファイルは、作業用フォルダの
``2026/05_ohanashi_register/`` に入れて使います。
ファイル名は ``ohanashi_register.py`` に変更しても、そのまま使えます。

コードの中身を確認したいときは、次の見本を読んでみてください。

:nekochan:`kochira-nya` 完成版はこちらニャ

.. literalinclude:: ../examples/05_05_ohanashi_register.py
   :language: python
   :caption: source/examples/05_05_ohanashi_register.py
   :linenos:


8. 実行してみよう
~~~~~~~~~~~~~~~~~

まずは、``python-study`` の中に 5月用の作業フォルダを作ります。
そのあと、ダウンロードした ``05_05_ohanashi_register.py`` をそのフォルダへコピーします。

*Windows (PowerShell)*

.. code-block:: powershell

   Set-Location python-study
   New-Item -ItemType Directory 2026\05_ohanashi_register -Force
   Copy-Item "$env:USERPROFILE\Downloads\05_05_ohanashi_register.py" 2026\05_ohanashi_register\ohanashi_register.py

*Mac / Linux*

.. code-block:: bash

   cd python-study
   mkdir -p 2026/05_ohanashi_register
   cp ~/Downloads/05_05_ohanashi_register.py 2026/05_ohanashi_register/ohanashi_register.py

ファイルをコピーできたら、次のように実行します。

:nekochan:`yoshi-nya` ここで実行してみるニャ

*Windows (PowerShell / コマンドプロンプト)*

.. code-block:: powershell

   python 2026\05_ohanashi_register\ohanashi_register.py

*Mac / Linux*

.. code-block:: bash

   python3 2026/05_ohanashi_register/ohanashi_register.py

この教材リポジトリに入っている見本コードを試す場合は、
リポジトリのルートで次のように実行できます。

*Windows (PowerShell / コマンドプロンプト)*

.. code-block:: powershell

   python source\examples\05_05_ohanashi_register.py

*Mac / Linux*

.. code-block:: bash

   python3 source/examples/05_05_ohanashi_register.py

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

9. 発展：GUI版も試してみよう
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
CLI版が動いたら、発展として **ウィンドウで動かす GUI 版** も試せます。
今回はCLI版が本題なので、余裕がある人向けです。
 
GUI版のコードとセットアップ手順は、次の GitHub リポジトリに置いています。
 
   https://github.com/MikiMakino/100days-of-code/tree/main/day95-ohanashi-register-gui
 
``ohanashi_register_gui.py``・``README.md``・``requirements.txt`` の
3ファイルをそのままコピーして使ってかまいません。

計算ロジック（``calculate_total()``）は、CLI 版と同じ考え方で使えます。


10. エラーメッセージの見方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プログラムを書いていて、エラーが出た時、
大切なのは、**「失敗した」ではなく「どこを直せばよいかのヒントが出た」** と考えることです。

たとえば、値段を入れる場面で文字を入力すると、次のようなエラーが出ます。

:nekochan:`memo-nya` エラーは直す場所を教えてくれるヒントだニャ

.. code-block:: text

   1つの値段を入力してください: りんご
   Traceback (most recent call last):
     File "ohanashi_register.py", line 53, in <module>
       main()
     File "ohanashi_register.py", line 30, in main
       price = int(input("1つの値段（円）を入力してください: "))
   ValueError: invalid literal for int() with base 10: 'りんご'

このときは、次の順番で見ると分かりやすくなります。

- 最後の行  
  ``ValueError`` は「値の変換で困った」という意味です。
- その少し上の行  
  ``price = int(input(...))`` のところで起きたと分かります。
- ``line 30``  
  30行目を見直せばよいと分かります。

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

:nekochan:`yossha-nya` 1つだけ変えるところからで大丈夫ニャ

- 会員割引を 10% ではなく 5% に変えてみる
- 5個以上買ったら、まとめ買い割引を 200 円にしてみる
- 最後のメッセージを好きな文に変えてみる
- 消費税を計算する変数を追加してみる
- ``input()`` の質問文を、自分のお店らしい表現に変えてみる

5月は、**自分で入力した値でプログラムが動く楽しさ** を味わう回です。
まずは完成版をそのまま動かし、
そのあとで少しずつ自分のアイデアを足してみましょう。

おつかれさまでしたー :nekochan:`huhuhu-nya`


:nekochan:`calendar-nya` 次回予告
---------------------------------

次回の勉強会は **6月：特別回・講師招待ハンズオン** です。

6月6日（土）には、広島で **Python Boot Camp in 広島 3rd** も開催されます。
勉強会のメンバーでぜひ一緒に参加しましょう！

詳しくは :doc:`06_june` と :doc:`../events/index` をご覧ください。


:nekochan:`calendar-nya` PyCon JP 2026 のお知らせ
--------------------------------------------------

PyCon JP 2026 は、2026年8月21日（金）・22日（土）に広島国際会議場で開催されます。

現在、CfP（発表提案）・スポンサー・チケットの案内が公開されています。

- CfP の提出締め切りは **5月31日（日）** です。
- スポンサーを募集しています。
- チケット販売が始まっています。
- Early Bird チケットは **6月14日（日）** までです。

CfP、スポンサー、チケットの案内はすべて connpass ページにまとまっています。

`PyCon JP 2026 - connpass <https://pyconjp.connpass.com/event/391006/>`_
