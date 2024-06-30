# DAG shortest paths


(算法)



定义:
解决单源最短路径问题的加权有向无环图1)做一个顶点拓扑排序的优势首先顶点没有传入边缘和顶点,只有传入边缘,2)分配一个无限距离每个顶点(dist (v) =∞)和零距离源,并按照顺序为每个顶点v 3),对于每一个即将离任的边缘e (v, u),如果dist (v) +重量(e) < dist (u),集经销(u) = dist (v) +重量(e)和u, v的前任。



另请参阅
Dijkstra算法，Bellman-Ford算法。


作者:钢







2004年4月19日修改。
HTML页面格式化星期三Mar 13 12:42:45 2019。



引用如下:
Paul E. Black，“DAG最短路径”，在
算法与数据结构词典[在线]，Paul E. Black主编，2004年4月19日。(今天访问)
可从:https://www.nist.gov/dads/HTML/dagShortPath.html获得