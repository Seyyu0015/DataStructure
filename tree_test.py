import tree

"""
pytest 测试
tree.py
"""


def test_tree():
    """pytest 测试"""
    tree_node_left_left = tree.Tree('D')
    tree_node_left_right = tree.Tree('E')
    tree_node_right_left = tree.Tree('F')
    tree_node_left = tree.Tree('B', tree_node_left_left, tree_node_left_right)
    tree_node_right = tree.Tree('C', tree_node_right_left)
    tree_test = tree.Tree('A', tree_node_left, tree_node_right)
    """
    测试树的结构：
                [A]
            ↙        ↘
        [B]             [C]
      ↙     ↘          ↙
    [D]     [E]     [F]
    """
    # preorder
    assert tree_test.preorder() == ['A', 'B', 'D', 'E', 'C', 'F']

    # inorder
    assert tree_test.inorder() == ['D', 'B', 'E', 'A', 'F', 'C']

    # postorder
    assert tree_test.postorder() == ['D', 'E', 'B', 'F', 'C', 'A']

    # height
    assert tree_test.height() == 3