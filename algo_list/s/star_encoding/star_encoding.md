# 星号编码


(算法)



定义:
使用固定的字典，用包含许多重复字符的字符串(通常是星号或“*”)对文本中的单词进行编码。



另请参阅
霍夫曼编码，Burrows-Wheeler变换。



注意:
这个转换不会压缩文本，而是为压缩做好准备。通过多次运行星号，编码后的文本可能比原始文本更易于压缩。发送者和接收者必须以某种方式交流字典。

字的码串与字的长度相同。Kruse和Mukherjee“从大量参考文本”中构建了一本字典，并仅根据频率分配代码。Mark Nelson根据输入的文本构建了字典，并根据单词分配了代码。


作者:钢


Holger Kruse和Amar Mukherjee，使用文本加密的数据压缩，Proc. Data compression Conference, Snowbird, Utah, USA, pp 447- 1997年3月。Holger Kruse和Amar Mukherjee对文本进行预处理以提高压缩比，Proc.数据压缩会议，Snowbird, Utah, USA, pp 556-464, 1998年4月。








条目修改于2022年4月20日。
HTML页面格式化星期三四月20 09:32:15 2022。



引用如下:
Paul E. Black，“星型编码”，in
算法与数据结构词典[在线]，Paul E. Black主编，2022年4月20日。(今天访问)
可从:https://www.nist.gov/dads/HTML/starEncoding.html获得