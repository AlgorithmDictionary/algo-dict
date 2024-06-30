# inversion list


(数据结构)



定义:
一组不重叠的数字范围，按递增顺序存储在数组中。奇数索引中的项开始范围，偶数索引中的项是结束后的第一个数字。

使用一种形式的二进制搜索来确定一个数字是否在任何范围内。如果搜索以奇数索引(开头)结束，则该数字在集合中。如果搜索结束于偶数索引(后端)或在数组之外，则它不在集合中。



概括(我是一种……)
集。



聚合子(…)是我的一部分或在我身上使用。)
数组，二进制搜索。



另请参阅
反向索引。



注意:
例如，要表示10- 14,25和37-42范围，倒排列表将是:10 15 25 26 37 43

有线性算法的并，交，集差，否定等。

术语倒排表也用于指存储位序列，作为0和1位之间的每个开关的数字位置。参见Teodor Ziatanov在Perl中的InversionList。有些作者把倒排索引称为倒排表。


作者:JH


定义改编自Inversion_list [Wikipedia]。更多的解释和代码见Richard Gillam, A Practical Programmer's Guide to Encoding Standard，第13章，第504ff页，Addison-Wesley Professional, 2002。








条目于2021年7月19日修改。
Mon Jul 19 10:37:07 2021。



引用如下:
Jarkko Hietaniemi，“倒排表”，in
算法和数据结构词典[在线]，Paul E. Black编辑，2021年7月19日。(今天访问)
可从:https://www.nist.gov/dads/HTML/inversionList.html获得