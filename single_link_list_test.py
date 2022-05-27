import single_link_list

"""
pytest 测试
"""


def test_list():
    """pytest测试"""
    list_test = single_link_list.SingleLinkList()

    # is_empty/append
    assert list_test.is_empty()
    list_test.append(1)
    assert not list_test.is_empty()

    # length
    assert list_test.length() == 1
    list_test.append(2)
    assert list_test.length() == 2

    # travel
    assert list_test.travel() == "[1, 2]"

    # add
    list_test.add(7)
    assert list_test.travel() == "[7, 1, 2]"

    # insert
    list_test.insert(1, 4)
    assert list_test.travel() == "[7, 4, 1, 2]"

    # remove
    list_test.remove(1)
    assert list_test.travel() == "[7, 4, 2]"

    # search
    assert list_test.search(7)
    assert not list_test.search(8)
