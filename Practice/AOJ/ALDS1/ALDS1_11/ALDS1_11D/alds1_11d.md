## 問題名
Graph I - Connected Components

## キーワード
グラフ, DFS, BFS

## 概要
N人とM個の関係性が入力されたあとQ個のクエリに答える

## 方針と読解
## level1 2WA
Union-Findやんけ〜と思いきや、DFSやBFSで解く回らしく、ろくに制限もみずに愚直に組んだ。
適当に隣接リストにおいて加えていき、クエリの段でstack式DFSをやるとふつうに間に合わない。そりゃそうだよ
## level2 3WA
なんでやDFSやっただろうがと思いながら書籍をみると、どうやら各クエリでDFSなんぞするわけはなく、前段階のグループ分け操作でDFSを行うことで各クエリはO(1)で解ける、というらしい。
## level3 2WA
脳みそが腐ってるから関係性が与えられるたびDFSしててWA。これはすべての関係性が与えられ終わってからやれば十分。
## level4 1WA
↑を組んだらなぜかミスってて、よくよくみたらグループの初期化はすなわちすべて独立した要素としてみているので、そのへん考慮するの忘れてた

最初の提出からn十分くらいかけたのでマジでキーボード破壊しそうになった
## 参考
書籍

## 所感
死にたくならない？