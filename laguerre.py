import numpy as np
import math

roots = (
    (-0.707107, 0.707107),
    (-1.224745, 0.0, 1.224745),
    (-1.650680, -0.534648, 0.534648, 1.650680),
    (0.263560, 1.413403, 3.596426, 7.085810, 12.640801),
)

coefficients = (
    (0.886227, 0.886227),
    (0.295409, 1.181636, 0.295409),
    (0.081313, 0.804914, 0.804914, 0.081313),
    (0.521756, 0.398667, 0.075942, 0.003612, 0.000032)
)


def laguerre(polylevel, x):
    if polylevel == 0:
        return 1
    elif polylevel == 1:
        return x - 1
    else:
        l = np.zeros(polylevel + 1, dtype="double")
        l[0] = 1
        l[1] = x - 1
        for i in range(1, polylevel):
            l[i + 1] = (((x - (2 * i) - 1) * l[i]) - ((i * i) * l[i - 1]))
        return l[polylevel]


def laguerre_factors(f, numOfNodes, polylevel):
    result = 0.0
    for j in range(numOfNodes - 2):
        result += f(roots[numOfNodes - 2][j]) * coefficients[numOfNodes - 2][j] * laguerre(polylevel, roots[numOfNodes - 2][j])

    print(result)
    return result / (math.factorial(polylevel) ** 2)


