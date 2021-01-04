def equality_classes(relation: list) -> list:
    '''
    Return list of lists, each list - equality class of given relation.
    >>> equality_classes ([[1, 0, 0, 0],\
                           [0, 1, 0, 0],\
                           [0, 0, 1, 0],\
                           [0, 0, 0, 1]])
    [[0], [1], [2], [3]]
    >>> equality_classes ([[1, 1, 0, 0],\
                           [1, 1, 0, 0],\
                           [0, 0, 1, 1],\
                           [0, 0, 1, 1]])
    [[0, 1], [2, 3]]
    >>> equality_classes ([[1, 1, 1, 1],\
                           [1, 1, 1, 1],\
                           [1, 1, 1, 1],\
                           [1, 1, 1, 1]])
    [[0, 1, 2, 3]]
    '''
    classes_list = []
    for i in range(len(relation)):
        for j in range(len(relation)):
            if relation[i][j]:
                if not classes_list:  # creating first class
                    if i != j:  # we dont need class as [0, 0]
                        new_class = [i, j]
                    else:
                        new_class = [i]
                    classes_list.append(new_class)
                else:  # if we have some classes (at least one)
                    count = 0
                    for our_class in classes_list:  # checking each class
                        if i in our_class and j not in our_class:
                            our_class.append(j)
                            break
                        elif j in our_class and i not in our_class:
                            our_class.append(i)
                            break
                        elif i in our_class and j in our_class:
                            break
                        else:
                            count += 1
                            # counter for finding out pair (i,j) which has separate class
                    if count == len(classes_list):
                        if i != j:
                            new_class = [i, j]
                        else:
                            new_class = [i]
                        classes_list.append(new_class)
    return classes_list
