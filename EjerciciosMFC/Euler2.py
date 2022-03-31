import numpy as np

np.set_printoptions(suppress=True)
tam = 6
path = np.zeros((tam, tam))
for r in range(tam):
    for c in range(tam):
        if c > 0:
            if r == 0:
                path[r, c] = 1
            else:
                path[r, c] = path[r-1, c] + path[r, c-1]
                val = path[r, c]
        elif r > 0:
            path[r, c] = 1

print(path)
print(val)