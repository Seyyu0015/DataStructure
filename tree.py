"""
二叉树

实现二叉树的算法
未完成
"""

global NODE_LIST  # 用于遍历时记录节点内容的列表


class Tree:
    """二叉树"""
    def __init__(self, item=None, left=None, right=None):
        """
        二叉树的一个节点
        :param item: 数据
        :param left: 左子树
        :param right: 右子树
        """
        self.item = item
        self.left = left
        self.right = right

    def preorder(self) -> list:
        """
        前序遍历首先访问根结点然后遍历左子树，最后遍历右子树。
        在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。
        :return:包含所有节点的item的列表
        """
        global NODE_LIST
        NODE_LIST = []
        self.preorder_node()
        return NODE_LIST

    def preorder_node(self):
        """
        前序遍历的单个节点,当调用preorder()并创建完成用于记录的NODE_LIST之后
        此方法会以前序遍历的方式向NODE_LIST末尾添加元素
        """
        global NODE_LIST
        if self.item is not None:
            NODE_LIST.append(self.item)
        if self.left is not None:
            self.left.preorder_node()
        if self.right is not None:
            self.right.preorder_node()

    def inorder(self) -> list:
        """
        中序遍历首先遍历左子树，然后访问根结点，最后遍历右子树。
        :return:包含所有节点的item的列表
        """
        global NODE_LIST
        NODE_LIST = []
        self.inorder_node()
        return NODE_LIST

    def inorder_node(self):
        """
        中序遍历的单个节点,当调用inorder()并创建完成用于记录的NODE_LIST之后
        此方法会以中序遍历的方式向NODE_LIST末尾添加元素
        """
        global NODE_LIST
        if self.left is not None:
            self.left.inorder_node()
        if self.item is not None:
            NODE_LIST.append(self.item)
        if self.right is not None:
            self.right.inorder_node()
