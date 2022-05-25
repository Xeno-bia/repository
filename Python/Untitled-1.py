$ pip list                            #ライブラリの一覧
$ pip install ライブラリ              #ライブラリをインストール
$ pip-review --auto                   #ライブラリをアップデート
import ライブラリ                     #ライブラリをインポート
from ライブラリ import *              #ライブラリをインポート
class クラス(親クラス):               #オブジェクトを作成
    フィールド = 値                   #    フィールドを作成
    def メソッド(self, 引数):         #    メソッドを作成
        ...                           #        処理
オブジェクト = クラス(引数)           #オブジェクトを作成
オブジェクト.フィールド               #フィールドを呼び出し
オブジェクト.メソッド(引数)           #メソッドを呼び出し
1.0                                   #数値
f'1{x}'                               #文字列
[1]                                   #リスト
range(開始, 終了, 間隔)               #連番
リスト.append(値)                     #リストに値を追加
リスト.remove(位置)                   #リストの値を削除
リスト.sort()                         #昇順にする
リスト.sort(reverse=True)             #降順にする
.count(値)                                                         # ...の個数をカウント
.replace(旧, 新)                                                   # ...を...に置き換える
.split(区切り)                                                     # ...を...で分割する
.zfill(桁)                                                         # ゼロ埋め
len(リスト)                                                        # ...の要素数
max(リスト)                                                        # ...の最大値
min(リスト)                                                        # ...の最小値
sorted(リスト)                                                     # ...を昇順に並べ替え
sum(リスト)                                                        # ...の合計
... + ...                                                          # ...足す...
... - ...                                                          # ...引く...
... * ...                                                          # ...掛ける...
... ** ...                                                         # ...の...乗
... / ...                                                          # ...割る...
... % ...                                                          # ...割る...の余り
... == ...                                                         # ...イコール...
... < ...                                                          # ...小なり...
... <= ...                                                         # ...小なりイコール...
... > ...                                                          # ...大なり...
... >= ...                                                         # ...大なりイコール...
... in ...                                                         # ...が...を含む
... and ...                                                        # ...かつ...
... or ...                                                         # ...または...
not ...                                                            # ...ではない

with ファイル as 変数:                                             # ファイルを開く
    ...                                                            #     ...する

if 条件:                                                           # もし...なら
    ...                                                            #     ...する
elif 条件:                                                         # でなければもし...なら
    ...                                                            #     ...する
else:                                                              # でなければ
    ...                                                            #     ...する

for 変数 in リスト:                                                # ...の分
    ...                                                            #     ...を繰り返す
    continue                                                       #     処理を飛ばす
    break                                                          #     ループを終わる

while 条件:                                                        # ...の間繰り返す
    ...                                                            #     ...を繰り返す
    continue                                                       #     処理を飛ばす
    break                                                          #     ループを終わる

print(出力内容, sep=区切り)                                        # ...を...区切りで出力

input(プロンプト)                                                  # 入力を取得

$ pyinstaller Pythonファイル --onefile --noconsole --icon=アイコン # ...をEXEファイル化