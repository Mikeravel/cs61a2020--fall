from lab.lab05.lab05 import branches, is_leaf, label,tree
import math


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(branche) for branche in branches(t)])


def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(branch) for branch in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                         [tree(3),
    ...                         tree(4)]),
    ...                 tree(5,
    ...                     [tree(6,
    ...                         [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
    4
    9
    16
    25
    36
    49
    64
    """
    sq_branches =[square_tree(branch) for branch in branches(t)]
    return tree(label**2, sq_branches)


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

def prune_binary(t, nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [n[1:] for n in nums if n[0] == label(t)]
        new_branches = []
        for b in branches:
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches +[pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)