'''
Module for working with transition.
'''
def build_transition_func (relation : list) -> list:
    '''
    Return transitive composition of given realtion (as list of lists).
    Warshall algorithm.
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
                        #if (i,k) and (k,j) but not (i,j) => no transition
                        result = False
    return result

def count_transitive_relations (num : int) -> int:
    '''
    Return the number of transitive relations on numxnum matrix.
    Precondition! : n < 7.
    >>> count_transitive_relations(4)
    3994
    >>> count_transitive_relations(3)
    171
    '''
    count = 0
    for number in range (2**(num**2)) : #we'll take binary view of each such number
        number = str((bin(number))[2:]).zfill(num**2) #binary view
        relation = [[int(number[i*num+j]) for j in range(num)] for i in range(num)]
        #creating relation from string to work with another function
        if transition_check(relation) :
            count+=1
    return count
