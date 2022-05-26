"""
单链表

算法.单链表
"""


class SingleNode(object):
    """
    链表的单个节点
    ┌─────┬─────┐
    │data │next │
    └─────┴─────┘
    """

    def __init__(self, item):
        self.item = item  # item是内容
        self.next = None  # next是指针


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self) -> bool:
        """
        判断链表是否为空
        :return: True / False
        """
        if self.__head is None:
            return True
        else:
            return False

    def length(self):
        """
        获取链表长度
        :return:int
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

    def travel(self):
        """遍历链表"""
        # 指针指向首节点
        cur = self.__head

        # 如果指针所在节点不是空的
        while cur is not None:
            print(cur.item, end=',')
            cur = cur.next

    def append(self, item):
        """
        向链表尾部添加元素
        :param item: 元素内容
        :return:
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
        :param item:
        :return:
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
        :return:
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

    def search(self, item):
        """
        根据内容查找节点是否存在
        :param item: 查找的内容
        :return: True / False
        """
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                # 内容不匹配 游标继续移动
                cur = cur.next
        return False


"""pytext测试"""


def test_is_empty():
    """测试is_empty()"""
    list_empty = SingleLinkList()
    list_not_empty = SingleLinkList()
    list_not_empty.append(1)

    assert list_empty.is_empty() and not list_not_empty.is_empty()

