"""Module: symmetry for Computer Discrete Math project

    Functions
    ---------
        symmetry_check_func: function checks if relation is symmetrical
        build_symmetry_func: function builds symmetrical relation

"""


import doctest


def symmetry_check_func(relation):
    """
    Function checks if relation is symmetrical
    >>> symmetry_check_func([[0, 0, 0],\
                             [0, 1, 0],\
                             [0, 0, 1]])
    True
    >>> symmetry_check_func([[0, 1, 0],\
                             [0, 1, 0],\
                             [0, 0, 1]])
    False
    """
    t_f = []

    for i in range(len(relation)):
        for j in range(len(relation)):
            if i != j:
                if relation[i][j] == relation[j][i]:
                    t_f.append(True)
                else:
                    t_f.append(False)

    return all(t_f)


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


doctest.testmod()
