"""Module: build_reflection_func for Computer Discrete Math project

    Functions
    ---------
        build_reflection_func: function builds  reflection relation
"""


def build_reflection_func(relation):
    """
    Function build reflection relation
    >>> build_reflection_func([[1, 0, 0],\
                               [0, 0, 0],\
                               [0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> build_reflection_func([[0, 0, 0],\
                               [0, 1, 0],\
                               [0, 0, 1]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    >>> build_reflection_func([[1, 0, 0],\
                               [0, 1, 0],\
                               [0, 0, 1]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    for num in range(len(relation)):
        relation[num][num] = 1

    return relation
