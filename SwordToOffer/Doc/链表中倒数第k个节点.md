# 链表中倒数第k个节点

<center>知识点：链表</center>


## 题目描述
输入一个链表，输出该链表中倒数第k个结点。

## 解题思路
设两个指针，初始使都指向head节点，然后让第一个指针先走k步，然后之后的步骤让两个指针一起向后移动，当第一个指针到达最后的时候第二个指针刚好会在倒数第k个位置，需要注意head为空或者k小于0或者k的长度大于链表的节点个数的情况。


## 代码

[这里](../Code/13.py)