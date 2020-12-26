"""Module: read_realtion for Computer Discrete Math project

    Functions
    ---------
        strip_int: [additional fuction] strip and convert str to int
"""


def strip_int(el):
    """
    Funtion strips str and convert it to integer
    >>> strip_int(' 3')
    3
    """
    return int(el.strip())


def read_relat(file_path):
    relation_lst = []
    with open(file_path, 'r') as relation:
        for row in relation:
            one_row = row.strip().split(',')
            one_row = list(map(strip_int, one_row))
            for element in one_row:
                if element != 0 and element != 1:
                    return "Invalid relation in file"
            relation_lst.append(one_row)
    return relation_lst


