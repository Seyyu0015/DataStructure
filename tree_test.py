import tree

"""
pytest 测试
tree.py
"""


def test_tree():
    tree_node_left = tree.Tree('B')
    tree_node_right = tree.Tree('C')
    tree_test = tree.Tree('A', tree_node_left, tree_node_right)
    assert tree_test.preorder() == ['A', 'B', 'C']
