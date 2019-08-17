# learn_python
记录学习python的一些内容

1. pathlib_learn.py

pathlib 是Python内置库，Python 文档给它的定义是 Object-oriented filesystem paths（面向对象的文件系统路径）。pathlib 提供表示文件系统路径的类，其语义适用于不同的操作系统。路径类在纯路径之间划分，纯路径提供纯粹的计算操作而没有I / O，以及具体路径，它继承纯路径但也提供I / O操作。

pathlib 不单纯是对 os 中一些模块或方法进行封装，而是为了兼容不同的操作系统，它为每类操作系统定义了接口。你希望在UNIX机器上操作Windows的路径，然而直接操作是做不到的，所以为你创建了一套接口 PurePath，你可以通过接口来实现你的目的（反之亦然）

官方文档：https://docs.python.org/zh-cn/3/library/pathlib.html
