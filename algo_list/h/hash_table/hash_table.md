# hash table


(数据结构)



定义:
一个字典，其中的键通过哈希函数映射到数组位置。将多个项目的键映射到同一位置称为碰撞。有许多冲突解决方案，但它们可以分为开放寻址、链接和保留一个特殊的溢出区域。完美散列避免了冲突，但创建起来可能很耗时。



也称为分散存储。



专业化(…是一种我。)
完美哈希，动态哈希，二左哈希，杜鹃哈希，二选择哈希，哈希带。



聚合父级(我是…的一部分或在…中使用)
字典。



聚合子(…)是我的一部分或在我身上使用。)
负载因子，哈希表删除，冲突解决:合并链，线性探测，双重哈希，二次探测，均匀哈希，简单均匀哈希，分离链，直接链，聚类。



另请参阅
布隆过滤器，巨大的稀疏数组。



注意:
复杂度取决于哈希函数和冲突解决方案，但如果表足够大或增长，复杂度可能是恒定的(Θ(1))。一些开放寻址方案比其他方案更容易受到集群的影响。

表可以是一个桶数组，以便轻松处理某些数量的冲突，但仍然必须为桶溢出做一些准备。


作者:钢


哈希和各种冲突解决技术的解释和示例。



历史上的注意
“哈希的想法似乎是由h.p. Luhn提出的，他在1953年1月写了一份IBM内部备忘录”[Knuth98, 3:547, Sect. 6.4]。他继续用一页多的篇幅讲述历史。








条目修改于2022年4月20日。
HTML页面格式化星期三四月20 09:32:15 2022。



引用如下:
Paul E. Black，“哈希表”，in
算法与数据结构词典[在线]，Paul E. Black主编，2022年4月20日。(今天访问)
可从:https://www.nist.gov/dads/HTML/hashtab.html获得