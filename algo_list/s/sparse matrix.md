# 稀疏矩阵


(数据结构)



定义:
具有相对较少的非零(或“有趣”)项的矩阵。它可以在小于n × m的空间中表示。



聚合子(…)是我的一部分或在我身上使用。)
列表，正交列表，数组或点访问方法。



另请参阅
粗糙矩阵，巨大稀疏数组，邻接矩阵表示，k²-树。



注意:
如果k << n × m，则具有k个非零条目的n × m矩阵是稀疏的。将矩阵紧凑地表示为坐标格式的非零条目列表(值及其行/列位置)，作为条目列表的列表或数组(每一行一个列表)，两个正交列表(每列一个列表和每一行一个列表)，通过点访问方法或k²树可能会更快。


作者:钢


Yousef Saad的稀疏线性系统的迭代方法(PDF)，涵盖线性代数和矩阵类型的教科书的第1-3章。稀疏矩阵的实现，包括坐标格式，开始于第85页(PDF页97)。更新版本的其他格式和信息。


Entry modified 8 June 2023.
HTML page formatted Wed Aug  9 16:21:12 2023.



Cite this as:
Paul E. Black, "sparse matrix", in
Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 8 June 2023. (accessed TODAY)
Available from: https://www.nist.gov/dads/HTML/sparsematrix.html


