"""
二叉树

实现二叉树的算法
未完成
"""
global NODE_LIST  # 用于遍历时记录节点内容的列表


class Tree:
    """
    二叉树的单个节点
    │ item │ left │ right │
    """

    def __init__(self, item, left=None, right=None):
        """

        :param item: 数据
        :param left: 左子树
        :param right: 右子树
        """
        self.item = item
        self.left = left
        self.right = right

    def preorder(self) -> list:
        """
        前序遍历
        :return:{list} 包含所有节点的item的列表
        """
        global NODE_LIST
        NODE_LIST = []
        self.preorder_node()
        return NODE_LIST

    def preorder_node(self):
        global NODE_LIST
        if self.item is not None:
            NODE_LIST.append(self.item)
        if self.left is not None:
            self.left.preorder_node()
        if self.right is not None:
            self.right.preorder_node()
