# 选择


(算法)



定义:
选择数组中第k个最小元素的四部分算法。第1部分)将数组视为包含5个元素的组;排序并找出每组的中位数。2)使用Select递归地找到x，即中位数的中位数。3)接下来围绕x对数组进行分区。4)设i为分区低侧的元素个数。如果k≤i，使用Select递归查找低侧的第k个元素。否则选择高边的第k个元素。



另请参阅
select和partition, select第k个元素，Find, MODIFIND, tournament, reservoir sampling。



注意:
源自[CLR90, p 190]。有时被称为“快速选择”。

选择n个数中第i个最小值的比较次数为n+min(i,n-i)+o(n)或Θ(n)。


作者:钢


Robert W. Floyd和Ronald L. Rivest，选择的预期时间限制，ccacm, 18(3):165-172, 1975年3月

Robert W. Floyd和Ronald L. Rivest，算法#489 SELECT, ccacm, 18(3):173, 1975年3月








2009年1月14日修改。
HTML页面格式化星期三三月13 12:42:46 2019。



引用如下:
保罗·e·布莱克，《选择》，进入
算法与数据结构词典[在线]，Paul E. Black主编，2009年1月14日。(今天访问)
可从:https://www.nist.gov/dads/HTML/select.html获得