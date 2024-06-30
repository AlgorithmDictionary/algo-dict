# 基数排序


(算法)



定义:
一种多遍分布排序算法，根据项的键的一部分，从键的最低有效部分开始，将每个项分配到一个桶中。每次通过后，从桶中收集物品，保持物品的顺序，然后根据密钥的下一个最重要部分重新分配。



概括(我是一种……)
分布。



聚合子(…)是我的一部分或在我身上使用。)
计数排序可能是适合每次传递的算法。



另请参阅
邮差排序，桶排序，美国国旗排序，自顶向下基数排序。



注意:
这里有一个简单的例子。假设输入键为34、12、42、32、44、41、34、11、32和23。四个存储桶是合适的，因为有四个不同的数字(1、2、3和4)。第一次传递按最低有效数字将密钥分配到存储桶中。在第一次传递的中途，桶包含以下内容，其中每一行都是一个桶。B1: B2: 12 42 32 B3: B4: 34 44当第一次通过后，我们有以下内容。B1: 41 11 B2: 12 42 32 32 B3: 23 B4: 34 44 34我们收集这些，保持它们的相对顺序:41 11 12 42 32 32 23 34 44 34。现在我们用下一个最高位，也就是最高位来分配，得到下面的结果。B1: 11 12 B2: 23 B3: 32 32 34 34 B4: 41 42 44当我们收集它们时，它们是按顺序排列的:11 12 23 32 32 34 34 41 42 44。

基数排序在链表中特别有效。将项目放在链表中，而不是放在桶中。在一个回合结束时，通过将列表“缝合”在一起来收集项目:使每个列表的尾部指向下一个列表的头部。(摘自Steven Pigeon的《list上的快速排序和基数排序》，Dr. Dobb's Journal, 2002年5月，第89-94页。)


作者:钢







条目于2022年4月21日修改。
HTML页面格式化Thu Apr 21 14:52:02 2022。



引用如下:
Paul E. Black，“基数排序”，in
算法与数据结构词典[在线]，Paul E. Black主编，2022年4月21日。(今天访问)
可从:https://www.nist.gov/dads/HTML/radixsort.html获得