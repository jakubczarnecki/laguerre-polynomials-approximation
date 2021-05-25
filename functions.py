from numpy import sin, cos, e


def polynomial(x, tab):
    numOfFactors = len(tab)
    result = 0
    for i in range(numOfFactors - 1):
        if (i == (numOfFactors - 1)):
            result += tab[i]
        result += tab[i] * x ** (numOfFactors - 1 - i)

    return result


f1 = lambda x: abs(2 * x - 3)

f2 = lambda x: sin(x + 2)

f3 = lambda x: cos(x)

f4 = lambda x: x * x

f5 = lambda x: cos(sin(x))

f6 = lambda x: 3 * x ** 4 - 2 * x ** 3 + 4 * x ** 2 + x + 1  # 3x^4 - 2x^3 + 4x^2 + x + 1
