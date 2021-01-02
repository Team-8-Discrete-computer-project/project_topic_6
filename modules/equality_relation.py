def equality_classes(relation: list) -> list:
    '''
    Return list of lists, each list - equality class of given relation.
    '''
    classes_list = []
    for i in range(len(relation)):
        for j in range(len(relation[i])):
            if relation[i][j]:
                if not classes_list:
                    if i != j:
                        new_class = [i, j]
                    else:
                        new_class = [i]
                    classes_list.append(new_class)
                else:
                    count = 0
                    for our_class in classes_list:
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
                    if count == len(classes_list):
                        if i != j:
                            new_class = [i, j]
                        else:
                            new_class = [i]
                        classes_list.append(new_class)
    return classes_list
