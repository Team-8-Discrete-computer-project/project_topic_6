"""Module: reflection for Computer Discrete Math project

    Functions
    ---------
        reflection_check_func: function checks if relation is reflection
        build_reflection_func: function builds  reflection relation

"""


def reflection_check_func(relation):
    """
    Function checks if relation is reflection
    >>> reflection_check_func([[1, 0, 0],\
                               [0, 1, 0],\
                               [0, 0, 1]])
    True
    >>> reflection_check_func([[0, 0, 0],\
                               [0, 1, 0],\
                               [0, 0, 1]])
    False
    """
    t_f = []
    for num in range(len(relation)):
        t_f.append(bool(relation[num][num]))

    return all(t_f)


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
