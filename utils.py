import numpy as np

def polynomialFactors(n):
    tab = np.empty(shape = (n + 1), dtype = 'double')
    for i in range(int(n) + 1):
        print("Podaj wspolczynnik " + str(i) + ":\n")
        factor = input()
        tab[i] = np.double(factor)

    return tab

def choosePolynomialFactors():
    level = input("Podaj stopien wielomianu: ")
    factors = polynomialFactors(int(level))
    print("Tablica wspolczynnikow wielomianu: \n" + str(factors) + "\n")
    return factors


def chooseFactors():
    a = input('Podaj a: ')
    b = input('Podaj b: ')
    a = np.double(a)
    b = np.double(b)
    return a, b