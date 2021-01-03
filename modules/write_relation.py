"""Module: write_relation for Computer Discrete Math project

    Functions
    ---------
        write_relat: get relation in lists in list view and write it into "written_relation.csv"
        in a proper view
"""
from typing import List


def write_relat(relation: List[List[int]]):
    """
    Function get relation in lists in list view and write it into "written_relation.csv"
    in a proper view
    """
    with open('written_relation.csv', 'w', encoding='utf-8') as w_relation:
        for row in relation:
            for num in range(len(row)):
                if num == len(row) - 1:
                    w_relation.write(f'{row[num]}')
                else:
                    w_relation.write(f'{row[num]} ')
            w_relation.write('\n')
