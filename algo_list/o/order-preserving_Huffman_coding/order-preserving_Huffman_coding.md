# 保序霍夫曼编码


(算法)



定义:
基于每个字符出现频率的可变长度字符编码。该算法类似于霍夫曼编码，但树与字符保持相同的顺序。将组合频率最小的两棵相邻树连接为新根的子树。与霍夫曼编码一样，新树被分配为子树频率的总和。重复，直到所有字符都在一个树中。



聚合子(…)是我的一部分或在我身上使用。)
全二叉树，优先队列，贪心算法。



另请参阅
霍夫曼编码。



注意:
这可能不会产生真正的霍夫曼码。虽然编码后的消息长度可能是真正的霍夫曼码的两倍，但保持顺序的霍夫曼码“对大多数数据都相当有效”。[Graef06，第5页]

有一些算法可以产生最优的保序前缀码，但它们都比较复杂。


作者:钢







2006年12月5日修改。
HTML页面格式化星期三三月13 12:42:46 2019。



引用如下:
Paul E. Black，“保序霍夫曼编码”，in
算法和数据结构词典[在线]，Paul E. Black主编，2006年12月5日。(今天访问)
可从:https://www.nist.gov/dads/HTML/orderPreservingHuffmanCoding.html获得