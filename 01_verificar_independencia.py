from src.linear_independence import is_linearly_independent

v1 = [1, 0, 0]
v2 = [0, 1, 0]
v3 = [1, 1, 0]
v4 = [0, 0, 1]

print(" {v1, v2, v4} independente?", is_linearly_independent([v1, v2, v4]))
print(" {v1, v2, v3} independente?", is_linearly_independent([v1, v2, v3]))
