from functools import reduce

l = [0, "", None, 100]

reduce(lambda a, b: bool(a) or bool(b), l)
