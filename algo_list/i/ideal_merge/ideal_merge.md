# ideal merge


(算法)



定义:
将n个排序流合并为一个输出流。首先，流是按每个头元素的值排序的。然后移除第一个流的头，它是流排序后最小的，并写入输出。该流根据其新头部插入流列表中。取第一个流的头并重新插入该流，直到处理完所有元素为止。使用线性搜索将流插入到列表中，执行时间为Θ(M N)，其中M是元素的总数。将流保存在堆中，执行时间为Θ(M log N)。



另请参阅
简单合并，最优合并，UnShuffle排序，合并排序。



注意:
理想合并是Art S. Kagel作为UnShuffle排序实现的一部分首先提到的。


作者:问







条目于2009年1月9日修改。
HTML页面格式化星期三三月13 12:42:46 2019。



引用如下:
Art S. Kagel，“理想的合并”，在
算法与数据结构词典[在线]，Paul E. Black主编，2009年1月9日。(今天访问)
可从:https://www.nist.gov/dads/HTML/idealmerge.html获得