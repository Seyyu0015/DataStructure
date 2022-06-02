"""
单链表

实现单链表的算法
"""


class SingleNode(object):
    """单链表"""

    def __init__(self, item):
        """链表的单个节点"""
        self.item = item  # item是内容
        self.next = None  # next是指针


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self) -> bool:
        """
        判断链表是否为空
        :return:{bool}链表是否为空
        """
        if self.__head is None:
            return True
        else:
            return False

    def length(self) -> int:
        """
        获取链表长度
        :return:{int} 链表长度
        """
        # 指针指向首节点
        cur = self.__head

        # 从0开始计数
        count = 0
        # 如果指针所在节点不是空的
        while cur is not None:
            count += 1  # 计数1
            cur = cur.next  # 指针移动到下一个节点
        return count

    def travel(self) -> str:
        """
        遍历链表
        :return:{str} 链表内容
        """
        # 指针指向首节点
        cur = self.__head
        str_print = '['

        # 如果指针所在节点不是空的
        while cur is not None:
            str_print = str_print + str(cur.item)
            cur = cur.next
            if cur is not None:
                str_print = str_print + ', '
        str_print = str_print + ']'
        return str_print

    def append(self, item):
        """
        向链表尾部添加元素
        :param item: 元素内容
        """
        # 创建新节点
        node = SingleNode(item)

        # 空链表的情况
        if self.is_empty():
            self.__head = node

        else:
            cur = self.__head
            # 找到最后一个节点
            while cur.next is not None:
                cur = cur.next
            cur.next = node  # 使最后一个节点指向新节点

    def add(self, item):
        """
        向链表头部添加元素
        :param item: 内容
        """
        # 创建新节点
        node = SingleNode(item)
        # 新节点指向原头部
        node.next = self.__head
        # 头部设置为新节点
        self.__head = node

    def insert(self, pos, item):
        """
        向指定位置插入数据
        :param pos: 位置
        :param item: 内容
        """
        # 特例
        # 头部插入
        if pos <= 0:
            self.add(item)
        # 尾部插入
        elif pos > self.length() - 1:
            self.append(item)

        # 插入
        else:
            node = SingleNode(item)  # 创建新节点
            pre = self.__head  # 插入位置的前一个节点,初始为head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """根据内容删除节点"""
        cur = self.__head
        pre = None

        while cur is not None:  # 遍历链表
            if cur.item == item:  # 找到相同内容的节点
                # 删除节点
                if cur == self.__head:  # 删除节点为头部
                    self.__head = cur.next
                else:  # 删除节点不为头部
                    pre.next = cur.next
                break
            else:
                # 移动
                pre = cur
                cur = cur.next

    def search(self, item) -> bool:
        """
        根据内容查找节点是否存在
        :param item: 查找的内容
        :return:节点是否存在
        """
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                # 内容不匹配 游标继续移动
                cur = cur.next
        return False

