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


def test_is_empty():
    """使用pytext测试is_empty方法"""
    list_s = SingleLinkList()
    assert list_s.is_empty() == True
