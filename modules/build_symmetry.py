"""Module: build_symmetry_func for Computer Discrete Math project

    Functions
    ---------
        build_symmetry_func: function builds symmetrical relation
"""


def build_symmetry_func(relation):
    """
    Function build symmetrical relation
    >>> build_symmetry_func([[1, 1, 1],\
                             [0, 1, 0],\
                             [0, 0, 1]])
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    >>> build_symmetry_func([[0, 1, 0],\
                             [0, 0, 1],\
                             [0, 0, 0]])
    [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    """
    for i in range(len(relation)):
        for j in range(len(relation)):
            if i != j:
                if (relation[i][j] == 1 and relation[j][i] == 0) or (relation[i][j] == 0 and relation[j][i] == 1):
                    relation[i][j] = 1
                    relation[j][i] = 1
    return relation
