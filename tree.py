"""
二叉树

实现二叉树的算法
未完成
"""


class Tree:
    """
    二叉树的单个节点
    ┌─────┬─────┬─────┐
    │item │left │right│
    └─────┴─────┴─────┘
             ↓     ↓
    """
    def __init__(self, item, left, right):
        """

        :param item: 数据
        :param left: 左子树
        :param right: 右子树
        """
        self.item = item
        self.left = left
        self.right = right
