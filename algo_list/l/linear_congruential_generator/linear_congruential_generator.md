# linear congruential generator


(算法)



定义:
一类伪随机数生成器算法。下一个数由当前个数通过rn+1 = (A × rn+ B) mod M生成，其中A和M是相对素数。



概括(我是一种……)
伪随机数生成器。



注意:
在软件中实现时，可以选择A和B，这样几乎每一步都有整数溢出，因此序列的可预测性较低，避免了mod操作。低阶位往往比高阶位更不随机。这可以通过丢弃一些低阶位来改进。因此，随机数的范围小于计算中使用的整数的范围。

更好的算法是可用的，但它们更复杂。


作者:BB







条目于2021年7月26日修改。
Mon Jul 26 11:58:06 2021。



引用如下:
Bob Bockholt，“线性同余生成器”，于
算法和数据结构词典[在线]，Paul E. Black，编辑，2021年7月26日。(今天访问)
可从:https://www.nist.gov/dads/HTML/linearCongruentGen.html获得