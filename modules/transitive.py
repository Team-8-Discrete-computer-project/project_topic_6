''' Transition!:)
'''

from itertools import product
import numpy as np

def build_transition_func (relation : list) -> list:
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
    for k in range(len(relation)) :
        for i in range(len(relation)) :
            if i!=k and relation[i][k] :
                for j in range(len(relation)) :
                    relation[i][j] = relation[i][j] or relation[k][j]
    return relation

def transition_check (relation : list) -> bool:
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
    for k in range(len(relation)) :
        for i in range(len(relation)) :
            if relation[i][k] :
                for j in range(len(relation)) :
                    if relation[k][j] and not relation[i][j] :
                        result = False
    return result

def generating_relations (num : int) -> list:
    '''
    Return list of lists, each lists represents one of realtions of nxn matrix.
    '''
    for relation in product([1, 0], repeat = num*num) :
        if transition_check(np.reshape(relation, (num, num))) :
            yield relation

def count_transitive_relations (num : int) -> int:
    '''
    Return the number of transitive relations on nxn matrix.
    Precondition! : n < 7.
    >>> count_transitive_relations(4)
    3994
    >>> count_transitive_relations(3)
    171
    '''
    relations = list(generating_relations(num))
    return len(relations)