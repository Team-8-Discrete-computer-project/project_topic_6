"""Module: symmetry_check_func for Computer Discrete Math project

    Functions
    ---------
        symmetry_check_func: function checks if relation is symmetrical
"""


def symmetry_check_func(relation):
    """
    Function checks if relation is reflection
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
