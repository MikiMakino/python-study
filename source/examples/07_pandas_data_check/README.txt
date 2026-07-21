レモンパイのデータ検証レシピ
==================================

このフォルダーには、7月のpandas学習会で使う3ファイルが入っています。

- data_check.ipynb : 学習用ノートブック
- price.csv        : 架空の商品価格マスタ
- README.txt       : この説明

使い方
------

1. 3ファイルを同じフォルダーに置きます。
2. 下の説明に従って、JupyterLabまたはVS Codeの実行環境を準備します。
3. JupyterLabまたはVS Codeで data_check.ipynb を開きます。
4. 上から順に Shift + Enter で実行します。

Python 3 本体は、VS Codeの拡張機能とは別にインストールが必要です。

JupyterLabを使う場合
----------------------

JupyterLabとpandasが未導入の場合は、次のコマンドで導入できます。

Windows (PowerShell):

    python -m pip install pandas jupyterlab
    python -m jupyter lab

Mac / Linux (ターミナル):

    python3 -m pip install pandas jupyterlab
    python3 -m jupyter lab

Mac / Linux では Python 3 のコマンド名が python3 のことが多いです。
仮想環境を有効にした後は、python で実行できる場合もあります。

VS Codeを使う場合
-------------------

VS Codeの拡張機能だけでは、Notebookのセルを実行できません。
次の準備が必要です。

1. Python 3本体をインストールする
2. VS CodeにMicrosoftのPython拡張機能とJupyter拡張機能を入れる
3. Notebookで使うPython環境にpandasとipykernelを入れる
4. Notebook右上のカーネル選択で、3のPython環境を選ぶ

Windows (PowerShell):

    python -m pip install pandas ipykernel

Mac / Linux (ターミナル):

    python3 -m pip install pandas ipykernel

VS Code内で実行する場合、JupyterLab本体は必須ではありません。
Notebookを実行するPython環境にはipykernelが必要です。

注意
----

名称・コード・価格・件数は、すべて学習会用の完全な架空データです。
自業務のCSVで使う場合は、ファイル名と列名を自分のデータに合わせて変更してください。
