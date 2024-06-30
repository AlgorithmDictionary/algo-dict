# bucket trie


(数据结构)



定义:
树的一种变体，其中叶节点是存放k个字符串的桶。通常意味着固定大小的桶。



概括(我是一种……)
单词查找树。



专业化(…是一种我。)
elastic-bucket单词查找树。



注意:
结合终端串可以大大缩短分支。例如，“extraordinary”，“extraordininess”和“extraordinary”可以存储在一个短分支末端的一个桶中，以区分它们与extran…和extrap……而不是公共子字符串的长分支…ordinary…

这个名字来自于检索，读作“树”。请参阅trie的历史注释。


作者:钢


Edward H. Sussenguth, Jr.，树形结构在文件处理中的应用，中国计算机学报，6(5):272-279,May 1963。








条目于2019年9月3日修改。
HTML页面格式化星期五Sep 6 15:26:10 2019。



引用如下:
保罗·e·布莱克，《桶形树》，in
《算法与数据结构词典》，Paul E. Black主编，2019年9月3日。(今天访问)
可从:https://www.nist.gov/dads/HTML/bucketTrie.html获得