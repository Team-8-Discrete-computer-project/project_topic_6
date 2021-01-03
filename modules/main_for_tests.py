from read_relation import read_relat
from write_relation import write_relat
from reflection import reflection_check_func, build_reflection_func
from symmetry import symmetry_check_func, build_symmetry_func
from transitive import build_transition_func, transition_check, generating_relations

from itertools import product
import numpy as np

relation = read_relat('task6_data/rel_1500_0.01.csv')
# print(transition_check(relation))
write_relat(build_transition_func(relation))
