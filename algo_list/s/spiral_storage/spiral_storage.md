# 螺旋存储


(数据结构)



定义:
一次增加几个槽的动态哈希表。它使用哈希函数h，其范围为[0,1]。对于键k，计算中间值x=≤S-h(k)≤h(k)≤h(k)≤，以找到最终槽⌊dx⌋，其中d>1称为生长因子。要增加槽数，可将S增加到S'，并将数组中所有的键重哈希为⌊dS'⌋-1。



概括(我是一种……)
动态哈希。



另请参阅
线性散列。



注意:
选择d=2和S=log2N，槽的数量，每次扩展退出一个槽并创建两个新槽。由于正在使用的槽位从⌊dS⌋到⌊dS+1⌋-1，因此它们通常被重新映射为物理存储。


作者:钢


G. N. N. Martin，螺旋存储:增量可扩充哈希寻址存储，计算理论第27期，英国华威大学，1979年。

Per-Åke Larson，动态哈希表，ccacm 31(4):446-457, 1988年4月。








2006年7月25日修改。
HTML页面格式化星期三三月13 12:42:46 2019。



引用如下:
Paul E. Black，“螺旋存储”，in
算法和数据结构词典[在线]，Paul E. Black主编，2006年7月25日。(今天访问)
可从:https://www.nist.gov/dads/HTML/spiralStorage.html获得