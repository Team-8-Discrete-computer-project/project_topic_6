from read_relation import read_relat
import pprint

rel = read_relat('relation.csv')

# pretty print
pp = pprint.PrettyPrinter(indent=5)
pp.pprint(rel)

print('\n\n')