# これはエスパーですが、
# 1. 最大公約数の最大化なので1とか2とかは避けないと駄目
# 2. N個の数でMを構成するので、↑から、できるだけ小さい数を避けて大きい数を揃えたいが、どれかを大きくするとどれかが小さくなってしまう
#   -> 均等にわける （M/N）
# 余ったやつを適当にどれかに足す。なので数列を構成する数値は最大で2種類だけになる（余りがない場合もある）
# （よくよく考えたら種類が多いとそのぶんgcdが小さくなりそうなのでこれでよさそう）
# ex): n, m = 5, 10 -> (2, 2, 2, 2, 2)で2
# ex): n, m = 4, 10 -> (2, 2, 2, 4)で2
# ex): n, m = 5, 13 -> (2, 2, 2, 2, 5)で1

# だと思ったのに駄目でした
# 凡例: n, m = 7, 55の場合↑だと1になってしまうが(7と13のgcd)、(5, 5, 5, 10, 10, 10, 10)の5が正解っぽい

# 種類が少ないほうがいいのはあってそうなので、2種類のうち小さい順にa,bとすると(a*x)+(b*y)=m, x+y=nみたいな感じになりそう
# -> 総当たりの気持ち?

# -> 頭がこんがらがったので解説みたらまっっっっっっったく違ってたので死んだほうがいいね
# 方向性は完全に違ってたけど利用できそうなアプローチは微妙に思考過程から一歩出たところにあった気がする
# さっき凡例に上げたやつはもっといえば(5,5,5,5,5,5,25)でいい
# くやしいので解きたいんだけどどうせ次やるときはこの理解すら忘れてるはずだわな 向いてないからだね
