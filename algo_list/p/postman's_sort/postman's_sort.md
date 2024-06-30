# 邮差的分类


(算法)



定义:
一种高度工程化的自顶向下基数排序的变体，其中描述了键的属性，以便算法可以有效地分配桶和分发。



概括(我是一种……)
自顶向下基数排序。



另请参阅
多键快速排序。



注意:
这是邮局的信件分拣机使用的算法:首先是州，然后是邮局，然后是路线，等等。由于键不相互比较，排序时间为O(cn)，其中c取决于键的大小和桶的数量。如果你按字母顺序对很多文件进行排序，你可能会使用这种形式:你把每张文件放在它的堆(或桶)里，a、B、C、D等，然后对每一堆进行排序。

这类似于基数排序，但工作方式是“自顶向下”或“最高有效位数优先”，而基数排序工作方式是“自底向上”或“最低有效位数优先”。此外，这不会合并分布项，而基数排序可以。

罗伯特·雷米(ramey@rrsd.com)


作者:钢


Robert Ramey，邮差的分类，C用户杂志，1992年8月。

Entry modified 20 June 2011.
HTML page formatted Wed Mar 13 12:42:46 2019.



Cite this as:
Paul E. Black, "postman's sort", in
Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 20 June 2011. (accessed TODAY)
Available from: https://www.nist.gov/dads/HTML/postmansort.html


