# 布隆过滤器


(数据结构)



定义:
一种具有概率算法的数据结构，可以使用多个散列函数在单个位数组中快速测试大集合中的成员关系。



聚合父级(我是…的一部分或在…中使用)
hsadelta。



聚合子(…)是我的一部分或在我身上使用。)
位数组，哈希函数。



另请参阅
可逆Bloom查找表，位置敏感哈希。



注意:
一个Bloom过滤器对于秘密共享是很好的:给一个Bloom过滤器可以让别人看到你是否有一个项目(它是在Bloom过滤器中找到的)，但是重新创建整个集合是不切实际的。


作者:钢


下面的Bose、Guo、Kranakis等人的论文表明，“实际的假阳性率严格大于”Bloom的公式。Bloom_filter [Wikipedia]提供了许多变体和扩展。权衡和工程技术与链接的网站与最近的论文，哈希函数等。另一个解释错别字:误报的概率少了一个负号;指数应该是。e-kn / m。使用Bloom滤镜。语言是Perl。杰森戴维斯的互动动画帮助人们了解布鲁姆过滤器是如何工作的。



Burton Bloom，含允许错误的哈希编码的空间/时间权衡，ccacm, 13(7):422-426, July 1970。Prosenjit Bose, Hua Guo, Evangelos Kranakis, Anil Maheshwari, Pat Morin, Jason Morrison, michael Smid, Yihui Tang, Bloom过滤器的误报率研究，技术报告r -07-07, Carleton大学计算机科学学院，2007年3月1日。他们还得出结论:“我们的上限表明，对于足够大的m值和较小的k值，pk和实际假阳性率之间的差异可以忽略不计。”








条目于2020年11月9日修改。
星期一11月9日16:41:25 2020。



引用如下:
保罗·e·布莱克，“布隆过滤器”，在
算法与数据结构词典[在线]，Paul E. Black主编，2020年11月9日。(今天访问)
可从:https://www.nist.gov/dads/HTML/bloomFilter.html获得