''' Transition!:)
'''

from itertools import product
import numpy as np


def transition_check(relation: list) -> bool:
    '''
    Return True if relation is transitive and False otherwise.
    >>> transition_check ([[1, 0, 1],\
                           [1, 0, 1],\
                           [1, 0, 1]])
    True
    >>> transition_check([[1, 0, 0, 1],\
                          [1, 0, 0, 1],\
                          [1, 0, 0, 1],\
                          [1, 0, 0, 1]])
    True
    >>> transition_check([[1, 1, 0, 1],\
                          [1, 0, 0, 1],\
                          [1, 0, 0, 1],\
                          [1, 0, 0, 1]])
    False
    '''
    result = True
    new_relation = [[0 for _ in range(len(relation))]
                    for _ in range(len(relation))]
    for i in range(len(relation)):
        for j in range(len(relation)):
            if relation[i][j] == 1:
                for k in range(len(relation)):
                    if relation[j][k] == 1:
                        new_relation[i][k] = 1
    for i in range(len(relation)):
        for j in range(len(relation)):
            if new_relation[i][j] and not relation[i][j]:
                result = False
    return result


def build_transition_func(relation: list) -> list:
    '''
    Return transitive composition of given realtion (as list of lists).
    >>> build_transition_func ([[1, 0, 0, 1],\
                                [1, 0, 0, 1],\
                                [1, 0, 0, 1],\
                                [1, 0, 0, 1]])
    [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]]
    >>> build_transition_func ([[1, 1, 0, 1],\
                                [1, 0, 0, 1],\
                                [1, 0, 0, 1],\
                                [1, 0, 0, 1]])
    [[1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1]]
    '''
    for k in range(len(relation)):
        for i in range(len(relation)):
            if i != k and relation[i][k]:
                for j in range(len(relation)):
                    relation[i][j] = relation[i][j] or relation[k][j]
    return relation


def generating_relations(num: int) -> list:
    '''
    Return list of lists, each lists represents one of realtions of nxn matrix.
    '''
    relations = product([1, 0], repeat=num*num)
    relations = np.reshape(list(relations), (-1, num, num))
    return relations


def count_transitive_relations(num: int) -> int:
    '''
    Return the number of transitive relations on nxn matrix.
    Precondition! : n < 7.
    '''
    relations = generating_relations(num)
    count = 0
    for relation in relations:
        if transition_check(relation):
            count += 1
    return count
