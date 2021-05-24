import numpy as np
import math

roots = (
    (-0.707107, 0.707107),
    (-1.224745, 0.0, 1.224745),
    (-1.650680, -0.534648, 0.534648, 1.650680),
    (-2.020183, -0.958572, 0.0, 0.958572, 2.020183),
)

coefficients = (
    (0.886227, 0.886227),
    (0.295409, 1.181636, 0.295409),
    (0.081313, 0.804914, 0.804914, 0.081313),
    (0.019953, 0.393619, 0.954309, 0.393619, 0.019953)
)


def laguerre(polylevel, x):
    if polylevel == 0:
        return 1
    elif polylevel == 1:
        return x - 1
    else:
        l = np.zeros(polylevel, dtype="double")
        l[0] = 1
        l[1] = x - 1
        for i in range(1, polylevel - 1):
            l[i + 1] = (((x - (2 * i) - 1) * l[i]) - ((i * i) * l[i - 1]))
            return l[polylevel - 1]



def laguerre_factors(f, numOfNodes, polylevel):
    result = np.zeros(polylevel, dtype="double")
    for i in range(polylevel):
        for j in range(numOfNodes):
            result[i] += f(roots[numOfNodes - 2][j]) * coefficients[numOfNodes - 2][j] * laguerre(polylevel, roots[numOfNodes - 2][j])


    return result / math.factorial(polylevel) ** 2
