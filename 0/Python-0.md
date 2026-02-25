# Training Piscine Python for Data Science - 0

## Starting

**概要:** 今日はPythonプログラミング言語の基礎を学びます。

**バージョン:** 1.3

---

## 目次

| 章 | タイトル | ページ |
|---|---------|-------|
| I | 一般ルール | 2 |
| II | Exercise 00 | 4 |
| III | Exercise 01 | 5 |
| IV | Exercise 02 | 6 |
| V | Exercise 03 | 8 |
| VI | Exercise 04 | 10 |
| VII | 以降に従うべき追加ルール | 11 |
| VIII | Exercise 05 | 12 |
| IX | Exercise 06 | 14 |
| X | Exercise 07 | 16 |
| XI | Exercise 08 | 17 |
| XII | Exercise 09 | 19 |
| XIII | 提出とピア評価 | 20 |

---

## 第I章 — 一般ルール

- クラスターのコンピュータまたは仮想マシンを使用してモジュールを提出すること：
  - 仮想マシンのOSは自由に選択できる。
  - 仮想マシンにはプロジェクトを完了するために必要なすべてのソフトウェアがインストール・設定されていること。
- あるいは、必要なツールが利用可能であれば、クラスターのコンピュータを直接使用できる。
  - モジュールに必要なすべての依存関係をインストールするための十分な容量がセッションにあることを確認すること（キャンパスが提供している場合は `goinfre` を使用する）。
  - 評価前にすべてインストールが完了していること。
- 関数が予期せず終了してはならない（セグメンテーションフォールト、バスエラー、ダブルフリーなど）。未定義動作の場合を除く。このような問題が発生した場合、プロジェクトは機能していないとみなされ、評価で **0点** となる。
- プロジェクト用のテストプログラムを作成することを推奨する。ただし、これらのテストは**提出不要であり、採点対象外**である。自分の作業や仲間の作業を簡単にテストするために役立つ。これらのテストはディフェンス（防衛口頭試問）で特に有用である。ディフェンスでは、自分のテストや評価相手のテストを自由に使用できる。
- 課題は割り当てられたGitリポジトリに提出すること。Gitリポジトリ内の作業のみが採点される。Deepthoughtが採点を担当する場合、ピア評価後に実施される。Deepthoughtの採点中にいずれかのセクションでエラーが発生した場合、評価は終了する。
- **Python バージョン 3.10** を使用すること。
- 演習で明示的に禁止されていない限り、任意のビルトイン関数を使用してよい。
- ライブラリのインポートは明示的であること。例えば `import numpy as np` のように使用すること。`from pandas import *` のようなインポートは許可されず、その演習は **0点** となる。
- グローバル変数は禁止。
- オーディンにかけて、トールにかけて！自分の頭を使え！！！

---

## 第II章 — Exercise 00

| | Exercise 00 |
|---|---|
| **題名** | Exercice 00: 初めてのPythonスクリプト |
| **提出ディレクトリ** | `ex00/` |
| **提出ファイル** | `Hello.py` |
| **使用可能な関数** | なし |

各データオブジェクトの文字列を変更して、以下の挨拶を表示せよ：
"Hello World"、"Hello «キャンパスの国»"、"Hello «キャンパスの都市»"、"Hello «キャンパスの名前»"

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

期待される出力：

```
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

---

## 第III章 — Exercise 01

| | Exercise 01 |
|---|---|
| **題名** | Exercice 01: 初めてのパッケージ使用 |
| **提出ディレクトリ** | `ex01/` |
| **提出ファイル** | `format_ft_time.py` |
| **使用可能な関数** | `time`、`datetime`、または日付を取得可能な任意のライブラリ |

以下の形式で日付をフォーマットするスクリプトを書け。もちろん、日付は例と同じにはならないが、同じ形式でフォーマットされていなければならない。

期待される出力：

```
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

---

## 第IV章 — Exercise 02

| | Exercise 02 |
|---|---|
| **題名** | Exercice 02: 初めてのPython関数 |
| **提出ディレクトリ** | `ex02/` |
| **提出ファイル** | `find_ft_type.py` |
| **使用可能な関数** | なし |

オブジェクトの型を表示し、42を返す関数を書け。

プロトタイプは以下の通り：

```python
def all_thing_is_obj(object: any) -> int:
    #your code here
```

テスト用の tester.py：

```python
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

期待される出力：

```
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

> **注意:** 関数を単独で実行しても何も起こらない。

```
$>python find_ft_type.py | cat -e
$>
```

---

## 第V章 — Exercise 03

| | Exercise 03 |
|---|---|
| **題名** | Exercice 03: NULL not found |
| **提出ディレクトリ** | `ex03/` |
| **提出ファイル** | `NULL_not_found.py` |
| **使用可能な関数** | なし |

すべての種類の「Null」のオブジェクト型を表示する関数を書け。
正常に動作すれば0を返し、エラーの場合は1を返すこと。
関数はすべての種類の「Null」を表示する必要がある。

プロトタイプは以下の通り：

```python
def NULL_not_found(object: any) -> int:
    #your code here
```

テスト用の tester.py：

```python
from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
```

期待される出力：

```
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

> **注意:** 関数を単独で実行しても何も起こらない。

```
$>python NULL_not_found.py | cat -e
$>
```

---

## 第VI章 — Exercise 04

| | Exercise 04 |
|---|---|
| **題名** | Exercice 04: 偶数と奇数 |
| **提出ディレクトリ** | `ex04/` |
| **提出ファイル** | `whatis.py` |
| **使用可能な関数** | `sys`、または引数を受け取れる任意のライブラリ |

引数として数値を受け取り、それが奇数か偶数かを判定して結果を表示するスクリプトを作成せよ。

引数が複数指定された場合、または引数が整数でない場合は、**AssertionError** を表示すること。

期待される出力：

```
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

---

## 第VII章 — 以降に従うべき追加ルール

- グローバルスコープにコードを置かないこと。関数を使え！
- 各プログラムは main を持ち、単純なスクリプトであってはならない：

```python
def main():
    # テストとエラーハンドリング

if __name__ == "__main__":
    main()
```

- キャッチされていない例外は演習を無効にする。テストを求められたエラーの場合であっても同様。
- すべての関数にドキュメンテーション（`__doc__`）が必要。
- コードは規約（norm）に従うこと：
  - `pip install flake8`
  - `alias norminette=flake8`

---

## 第VIII章 — Exercise 05

| | Exercise 05 |
|---|---|
| **題名** | Exercice 05: 初めてのスタンドアロンPythonプログラム |
| **提出ディレクトリ** | `ex05/` |
| **提出ファイル** | `building.py` |
| **使用可能な関数** | `sys`、または引数を受け取れる任意のライブラリ |

今回は main を持つ本格的な独立プログラムを作成する。単一の文字列引数を受け取り、大文字、小文字、句読点、数字、スペースのそれぞれの合計数を表示すること。

- 引数が与えられない、または何も提供されない場合、ユーザーに文字列の入力を求めること。
- 複数の引数が提供された場合、**AssertionError** を表示すること。

期待される出力：

```
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward
compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$>
```

期待される出力（改行はスペースとしてカウントされる。改行を入れたくない場合は ctrl + D を使用）：

```
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

> **オーディンにかけて、トールにかけて！自分の頭を使え！！！車輪の再発明をせず、言語の機能を活用しろ。**

---

## 第IX章 — Exercise 06

| | Exercise 06 |
|---|---|
| **題名** | Exercice 06 |
| **提出ディレクトリ** | `ex06/` |
| **提出ファイル** | `ft_filter.py`, `filterstring.py` |
| **使用可能な関数** | `sys`、または引数を受け取れる任意のライブラリ |

### Part 1: filter関数の再実装

自分自身の `ft_filter` を再実装せよ。オリジナルのビルトイン関数と同じ動作をすること（`print(filter.__doc__)` と同じものを返すこと）。`ft_filter` の再実装には**リスト内包表記**を使用すること。

> **警告:** もちろん、オリジナルの `filter` ビルトイン関数の使用は禁止。

> **注意:** ここからモジュールを検証できるが、以降のプロジェクトで必要になる知識があるため、続けることを推奨する。

### Part 2: プログラム

2つの引数を受け取るプログラムを作成せよ：文字列 (S) と整数 (N)。プログラムは S 内の単語のうち、長さが N より大きいものをリストとして出力すること。

- 単語はスペース文字で区切られる。
- 文字列には特殊文字（句読点や不可視文字）を含まない。
- プログラムには少なくとも1つの**リスト内包表記**と1つの **lambda** を含むこと。
- 引数の数が2でない場合、または引数の型が不正な場合、プログラムは **AssertionError** を表示すること。

期待される出力：

```
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
$> python filterstring.py 'Hello the World' 99
[]
$>
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

---

## 第X章 — Exercise 07

| | Exercise 07 |
|---|---|
| **題名** | Exercice 07: 辞書 SoS |
| **提出ディレクトリ** | `ex07/` |
| **提出ファイル** | `sos.py` |
| **使用可能な関数** | `sys`、または引数を受け取れる任意のライブラリ |

文字列を引数として受け取り、モールス信号にエンコードするプログラムを作成せよ。

- プログラムはスペースと英数字をサポートする。
- 英数字はドット `.` とダッシュ `-` で表現される。
- 完全なモールス文字は単一のスペースで区切る。
- スペース文字はスラッシュ `/` で表現される。

モールス信号の保存には**辞書**を使用すること。

```python
NESTED_MORSE = { " ": "/ ",
                 "A": ".- ",
                 ...
```

引数の数が1でない場合、または引数の型が不正な場合、プログラムは **AssertionError** を表示すること。

```
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

---

## 第XI章 — Exercise 08

| | Exercise 08 |
|---|---|
| **題名** | Exercice 08: Loading ... |
| **提出ディレクトリ** | `ex08/` |
| **提出ファイル** | `Loading.py` |
| **使用可能な関数** | `os` |

`ft_tqdm` という関数を作成せよ。
この関数は `yield` 演算子を使って `tqdm` 関数を模倣すること。

プロトタイプは以下の通り：

```python
def ft_tqdm(lst: range) -> None:
    #your code here
```

テスト用の tester.py（自分のバージョンとオリジナルを比較する）：

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
```

期待される出力（オリジナルバージョンにできるだけ近い関数を作ること）：

```
$> python tester.py
100%|[===============================================================>]| 333/333
100%|                                                  | 333/333 [00:01<00:00, 191.61it/s]
```

> **注意:** ターミナルのサイズに適応するために `get_terminal_size` を使用できる。

---

## 第XII章 — Exercise 09

| | Exercise 09 |
|---|---|
| **題名** | Exercice 09: 初めてのパッケージ作成 |
| **提出ディレクトリ** | `ex09/` |
| **提出ファイル** | `*.py`, `*.txt`, `*.toml`, `README.md`, `LICENSE` |
| **使用可能な関数** | PyPI、またはパッケージ作成用の任意のライブラリ |

Pythonで初めてのパッケージを好きな方法で作成せよ。`pip list` コマンドを入力するとインストール済みパッケージの一覧に表示され、`pip show -v ft_package` を入力するとその特性が表示されること。

```
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

パッケージは以下のいずれかのコマンドで pip を使ってインストールできること（両方とも動作すること）：

- `pip install ./dist/ft_package-0.0.1.tar.gz`
- `pip install ./dist/ft_package-0.0.1-py3-none-any.whl`

パッケージは以下のようなスクリプトから呼び出せなければならない：

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

---

## 第XIII章 — 提出とピア評価

通常通り、課題をGitリポジトリに提出すること。ディフェンスではリポジトリ内の作業のみが評価される。フォルダ名とファイル名が正しいかどうか、必ず再確認すること。

> **評価は、評価対象グループのコンピュータ上で行われる。**
