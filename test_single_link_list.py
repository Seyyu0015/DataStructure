import single_link_list

"""
pytest 测试
"""


def test_is_empty():
    """测试is_empty()"""
    list_empty = single_link_list.SingleLinkList()
    list_not_empty = single_link_list.SingleLinkList()
    list_not_empty.append(1)

    assert list_empty.is_empty()
    assert not list_not_empty.is_empty()
