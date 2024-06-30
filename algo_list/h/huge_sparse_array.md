# huge sparse array


(数据结构)



定义:
设N为要存储的项数，R为键值范围的大小;分配两个数组，但不初始化:项数组I，其中|I|≥N;位置数组L，其中|L|=R。初始化一个变量，接下来是项数，为零(使用基于0的索引)。要插入项，请将其放在项数组中的下一个位置，并在位置数组中保存查找它的位置。




概括(我是一种……)
数组中。



另请参阅
稀疏矩阵，哈希表。



注意:
密钥必须是唯一的。重复的密钥可以用冲突解决方案来处理。这种数据结构通常是不切实际的，因为范围非常大。

这有效地分配了一个巨大的数组，而没有显式初始化它，代价是Θ(N)空间和每次访问的一点时间。

这就是哈希表想要的:插入和查找的时间是常数。


作者:钢


历史上的注意
在Alfred V. Aho, John E. Hopcroft, and Jeffrey D. Ullman, The Design and Analysis of Computer Algorithms，第71页，Addison-Wesley, 1974年，作为习题2.12首次提出的激励问题。








2008年8月14日修改。
HTML页面格式化星期三三月13 12:42:46 2019。



引用如下:
Paul E. Black，“巨大的稀疏阵列”，in
算法与数据结构词典[在线]，Paul E. Black主编，2008年8月14日。(今天访问)
可从:https://www.nist.gov/dads/HTML/hugeSparseArray.html获得