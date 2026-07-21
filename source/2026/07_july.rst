7月：データ検証レシピ
======================

pandas と Notebook で、商品価格マスタを検証します。


教材
----

:download:`教材一式をダウンロード <../examples/07_pandas_data_check.zip>`

個別にダウンロードする場合は、次の2ファイルを同じフォルダーに保存します。

- :download:`data_check.ipynb <../examples/07_pandas_data_check/data_check.ipynb>`
- :download:`price.csv <../examples/07_pandas_data_check/price.csv>`


実行環境
--------

**JupyterLab を使う場合**

Windows（PowerShell）

.. code-block:: powershell

   python -m pip install pandas jupyterlab
   python -m jupyter lab

Mac / Linux（ターミナル）

.. code-block:: bash

   python3 -m pip install pandas jupyterlab
   python3 -m jupyter lab

**VS Code を使う場合**

Python 3 本体と、Microsoft の Python 拡張機能・Jupyter 拡張機能が必要です。
Notebook で使う Python 環境に、次をインストールします。

Windows（PowerShell）

.. code-block:: powershell

   python -m pip install pandas ipykernel

Mac / Linux（ターミナル）

.. code-block:: bash

   python3 -m pip install pandas ipykernel

``.ipynb`` を開き、右上の「カーネルの選択」から、準備した Python 環境を選びます。
VS Code で実行する場合、JupyterLab 本体は必要ありません。

- `VS Code 公式：Python in Visual Studio Code <https://code.visualstudio.com/docs/languages/python>`_
- `VS Code 公式：Manage Jupyter Kernels <https://code.visualstudio.com/docs/datascience/jupyter-kernel-management>`_


検証すること
------------

現在は、次の5項目を使って商品単価を取得しています。

- 商品コード
- 提供先コード
- バリエーション
- 加工区分
- 供給ルート

供給ルートを外しても、登録価格が1つに決まるか確認します。


1. データの読み込み
-------------------

.. code-block:: python

   import pandas as pd

   df = pd.read_csv(
       "price.csv",
       encoding="cp932",
   )

   print(df.shape)
   display(df.head())

.. code-block:: python

   print(list(df.columns))


2. 健康診断
-----------

.. code-block:: python

   print(df.isna().sum())
   print(df.dtypes)


3. 空欄を整理する
-----------------

.. code-block:: python

   df2 = df.fillna({
       "バリエーション": "(空)",
       "加工区分": "(空)",
       "供給ルート": "(空)",
   })

   check = df2[
       df2["商品コード"].isna()
       | df2["提供先コード"].isna()
       | df2["登録価格"].isna()
   ]

   ok = df2[
       df2["商品コード"].notna()
       & df2["提供先コード"].notna()
       & df2["登録価格"].notna()
   ]

   print("df:", len(df))
   print("ok:", len(ok))
   print("check:", len(check))
   display(check)


4. 商品コードと提供先コードの組み合わせを確認する
--------------------------------------------------

.. code-block:: python

   key = ["商品コード", "提供先コード"]

   same_key = ok[
       ok.duplicated(key, keep=False)
   ]

   print(len(same_key))
   display(same_key)


5. 現行キーで価格が一意か確認する
---------------------------------

.. code-block:: python

   current_key = [
       "商品コード",
       "提供先コード",
       "バリエーション",
       "加工区分",
       "供給ルート",
   ]

   current_price_count = (
       ok.groupby(current_key)["登録価格"]
       .nunique()
   )

   current_check = current_price_count[
       current_price_count > 1
   ]

   print(len(current_check))
   display(current_check)


6. 供給ルートを外して価格が一意か確認する
-----------------------------------------

.. code-block:: python

   candidate_key = [
       "商品コード",
       "提供先コード",
       "バリエーション",
       "加工区分",
   ]

   candidate_price_count = (
       ok.groupby(candidate_key)["登録価格"]
       .nunique()
   )

   candidate_check = candidate_price_count[
       candidate_price_count > 1
   ]

   print(len(candidate_check))
   display(candidate_check)


7. 要確認の明細を見る
---------------------

.. code-block:: python

   problem_keys = (
       candidate_check
       .reset_index()[candidate_key]
   )

   problem_detail = ok.merge(
       problem_keys,
       on=candidate_key,
       how="inner",
   )

   display(problem_detail)


8. 完全に同じ行を確認する
-------------------------

.. code-block:: python

   duplicate_rows = df[
       df.duplicated(keep=False)
   ]

   print(len(duplicate_rows))
   display(duplicate_rows)


9. 要確認データを CSV に出す
----------------------------

.. code-block:: python

   check.to_csv(
       "check_blank.csv",
       index=False,
       encoding="utf-8-sig",
   )

   problem_detail.to_csv(
       "check_price.csv",
       index=False,
       encoding="utf-8-sig",
   )


10. 結果
--------

- 現行キーで価格が一意でない組：0組
- 供給ルートを外すと価格が一意でない組：3組
- 要確認明細：6行
