# 阿克曼函数

## 历史
阿克曼函数（Ackermann）是非原始递归函数的例子。它需要两个自然数作为输入值，输出一个自然数。它的输出值增长速度非常快，仅是对于(4,3)的输出已大得不能准确计算。

## 定义
Ackermann函数定义如下：　若m=0，返回n+1。
若m>0且n=0，返回Ackermann(m-1,1)。
若m>0且n>0，返回Ackermann(m-1,Ackermann(m,n-1))。

## 参考文献
https://baike.baidu.com/item/%E9%98%BF%E5%85%8B%E6%9B%BC%E5%87%BD%E6%95%B0/10988285?fr=ge_ala
https://xlinux.nist.gov/dads/HTML/ackermann.html
