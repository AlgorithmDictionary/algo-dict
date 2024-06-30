# invertible Bloom lookup table


(数据结构)



定义:
算法和存储键/值对的单元格数组。每个单元格都有一个计数，表示有多少对映射到该单元格、映射到该单元格的键的和以及映射到该单元格的值的和。使用k个哈希函数，将每对哈希映射到T[h1(k)]， T[h2(k)]，…T[香港(k)]。



也被称为IBLT。



概括(我是一种……)
字典，加上listEntries()操作和处理重复键的能力。



聚合子(…)是我的一部分或在我身上使用。)
数组，哈希函数。



另请参阅
布隆过滤器。



注意:
实现细节保证在很大的概率下，每个键/值对本身至少有一个单元格，其计数为1。可以从该单元格中检索值和键。

必须特别注意(a)不要多次插入键或删除不存在的键，或者(b)详细说明算法和数据结构。

listEntries()报告每个单元格中的键/值对，计数为1，然后删除该键/值对。


作者:钢


Michael T. Goodrich和Michael Mitzenmacher，可逆Bloom查找表，2011。(V3是2015年10月。)可在https://arxiv.org/pdf/1101.2245.pdf获得。








2018年6月8日修改。
HTML页面格式化星期三三月13 12:42:46 2019。



引用如下:
Paul E. Black，“可逆Bloom查找表”，in
算法与数据结构词典[在线]，Paul E. Black主编，2018年6月8日。(今天访问)
可从:https://www.nist.gov/dads/HTML/invertibleBloomTable.html获得