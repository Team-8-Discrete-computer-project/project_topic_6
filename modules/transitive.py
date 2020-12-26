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
    new_relation = [[0 for _ in range (len(relation))] for _ in range (len(relation))]
    for i in range(len(relation)) :
        for j in range (len(relation)) :
            if relation[i][j] == 1 :
                for k in range(len(relation)) : 
                    if relation[j][k] == 1 :
                        new_relation[i][k] = 1
    for i in range(len(relation)) :
        for j in range(len(relation)) :
            if new_relation[i][j] and not relation[i][j] :
                result = False
    return result

def build_transition_func (relation : list) -> list:
    '''
    '''