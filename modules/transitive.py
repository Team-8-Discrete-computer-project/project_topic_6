def transition_check (relation : list) -> bool :
    '''
    Return True if relation is transitive and False otherwise.
    >>> transition_check ([[1, 0, 1],\
                           [1, 0, 1],\
                           [1, 0, 1]])
    '''
    new_relation = [[0 for _ in range (len(relation))] for _ in range (len(relation))]
    for i in range(len(relation)) :
        for j in range
    return new_relation