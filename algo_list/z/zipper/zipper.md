# 拉链


(数据结构)



定义:
一种相当于二叉树的数据结构，它被“打开”，以便可以访问某些节点。它由一对组成:当前节点，以及重建树的信息。重构信息称为路径或上下文。移动到左子操作返回左子树，以及一个新路径，该路径具有(i) left值，(ii)当前节点，(iii)右子树，以及(iv)任何先前的路径。类似的操作移动到右子节点。向上移动操作返回根据路径信息和当前节点以及前一个路径重新构建的树。



注意:
在函数式编程语言中，拉链充当指向树的“指针”。这个名称来自于将移动到子操作可视化为解压缩树。(不过，move-to-child并没有将这些碎片分成两半，而是将它们保存在k元树中:路径。)


作者:钢


关于用拉链拉大树的消息。



g<s:1> rard Huet，拉链，函数式程序设计学报，7(5):549-554,1997。








条目于2021年6月29日修改。
Tue Jun 29 14:14:59 2021。



引用如下:
保罗·e·布莱克，《拉链》，在
算法与数据结构词典[在线]，Paul E. Black主编，2021年6月29日。(今天访问)
可从:https://www.nist.gov/dads/HTML/zipper.html获得