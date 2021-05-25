import numpy as np
import math

roots = (
    (0.585786, 3.414214),
    (0.415775, 2.294280, 6.289945),
    (0.322548, 1.745761, 4.536620, 2.395071),
    (0.263560, 1.413403, 3.596426, 7.085810, 12.640801),
)

coefficients = (
    (0.853553, 0.146447),
    (0.711093, 0.278518, 0.010389),
    (0.603154, 0.357419, 0.038888, 0.000539),
    (0.521756, 0.398667, 0.075942, 0.003612, 0.000032)
)


def laguerre(deg, x):
    if deg == 0:
        return 1
    elif deg == 1:
        return x - 1
    else:
        l = np.zeros(deg + 1, dtype="double")
        l[0] = 1
        l[1] = x - 1
        for i in range(1, deg):
            l[i + 1] = (((x - (2 * i) - 1) * l[i]) - ((i * i) * l[i - 1]))
        return l[deg]


def laguerre_factors(f, quadlevel, polylevel):
    result = 0.0
    for j in range(0, quadlevel):
        result += f(roots[quadlevel - 2][j]) * coefficients[quadlevel - 2][j] * laguerre(polylevel, roots[quadlevel - 2][j])

    print(result)
    return result / (math.factorial(polylevel) ** 2)



