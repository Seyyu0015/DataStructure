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
        前序遍历：
        首先访问根结点然后遍历左子树，最后遍历右子树。
        在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。
        :return:包含所有节点的item的列表(前序)
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
        中序遍历：
        首先遍历左子树，然后访问根结点，最后遍历右子树。
        :return:包含所有节点的item的列表(中序)
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

    def postorder(self) -> list:
        """
        后序遍历：
        首先遍历左子树，然后遍历右子树，最后访问根结点。
        :return:包含所有节点的item的列表(后序)
        """
        global NODE_LIST
        NODE_LIST = []
        self.postorder_node()
        return NODE_LIST

    def postorder_node(self):
        """
        后序遍历的单个节点,当调用postorder()并创建完成用于记录的NODE_LIST之后
        此方法会以中序遍历的方式向NODE_LIST末尾添加元素
        """
        global NODE_LIST
        if self.left is not None:
            self.left.postorder_node()
        if self.right is not None:
            self.right.postorder_node()
        if self.item is not None:
            NODE_LIST.append(self.item)

    def height(self) -> int:
        """
        树的高度：
        空树高度为0,只有root节点的树高度为1
        :return: 树的高度
        """
        if self.item is None:  # 空树高度为0
            return 0
        elif self.left is None and self.right is None:  # 只有root节点的树高度为1
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def level_order(self) -> list:
        """
        层序遍历:
        逐层进行遍历,即将每层的节点存在队列当中，
        然后进行出队（取出节点）和入队（存入下一层的节点）的操作，
        以此达到遍历的目的。
        :return:包含所有节点的item的列表(层序排列)
        """

        def left_child_of_node(tree_node) -> Tree:
            """
            返回父节点的左孩子
            :param tree_node: 父节点
            :return: 节点的左孩子
            """
            return tree_node.left if tree_node.left is not None else None

        def right_child_of_node(tree_node) -> Tree:
            """
            返回父节点的右孩子
            :param tree_node: 父节点
            :return: 右孩子
            """
            return tree_node.right if tree_node.right is not None else None

        # 层序遍历列表
        level_order_list = []  # 用于遍历的列表，储存树
        level_order = []  # 用于返回的列表，储存节点的内容

        # 根节点中的数据
        if self.item is not None:
            level_order_list.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order_list[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if left_child_of_node(node):
                        level.append(left_child_of_node(node))
                    # 如果右孩子非空，则添加右孩子
                    if right_child_of_node(node):
                        level.append(right_child_of_node(node))
                # 如果该层非空，则添加该层
                if level is not None:
                    level_order_list.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order_list[i])):
                    level_order.append(level_order_list[i][index].item)

        return level_order
