# Burrows-Wheeler变形


(算法)



定义:
对字符串进行排序。重复的子字符串导致排列字符串中的重复字符，这更容易压缩。知道原始字符串的最后一个字符，就可以从重新排列的字符串中重建原始字符串。



也被称为BWT。



聚合子(…)是我的一部分或在我身上使用。)
排序。



注意:
可以根据后缀数组定义转换，如下所示。结果是一个数组BWT，使得BWT[i] = T[SA[i]-1]，如果SA[i] > 1，否则$，其中T是原始字符串，i从1(基于1的索引)到T的长度，SA是T的后缀数组，$是表示字符串结束的特殊字符。


作者:钢


Burrows-Wheeler_transform(维基百科)。



Michael Burrows和David J. Wheeler，一种块排序无损数据压缩算法，研究报告SRC-124，数字设备公司，加州帕洛阿尔托，1994年5月。这个变换就是本文的算法C。








条目修改于2022年4月20日。
HTML页面格式化星期三四月20 09:32:15 2022。



引用如下:
保罗·e·布莱克，《Burrows-Wheeler变换》，in
算法与数据结构词典[在线]，Paul E. Black主编，2022年4月20日。(今天访问)
可从:https://www.nist.gov/dads/HTML/burrowsWheelerTransform.html获得