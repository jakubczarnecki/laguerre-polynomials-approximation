import numpy as np
import matplotlib.pyplot as plt

from laguerre import *
from hermite import gauss_hermite
import functions as f
from utils import *
from functions import *
from horner import horner

if __name__ == '__main__':
    a = np.zeros(5)
    print(a)
    print("\n\nMetody numeryczne - zadanie 5. Aproksymacja")
    print("Wariant 3 - wielomiany Laguerre'a\n")

    funcs = {
        "1": f.f1,
        "2": f.f2,
        "3": f.f3,
        "4": f.f4,
        "5": f.f5,
        "6": f.f6
    }

    func = input("\n 1. f(x) = |2x - 3|"
                 "\n 2. f(x) = sin(x)"
                 "\n 3. f(x) = cos(2x)"
                 "\n 4. f(x) = x^2"
                 "\n 5. f(x) = cos(sin(x))"
                 "\n 6. wielomian n-tego stopnia\n"
                 "\n Wybierz funkcję: ")

    level = int(input("podaj stopien wielomianu aproksy:"))
    left = np.double(input("podaj lewą stronę przedziału aproksymacji:"))
    right = np.double(input("podaj prawą stronę przedziału aproksymacji:"))
    nodes = int(input("podaj liczbę węzłów całkowania metodą Gaussa-Hermite'a:"))

    xs = np.linspace(left, right, 1000, endpoint=True)
    ys = []
    for x in xs:
        ys.append(polynomial(x, laguerre_factors(funcs.get(func), nodes, level)))

    xs2 = np.linspace(left, right, 1000, endpoint=True)
    ys2 = []
    for x in xs2:
        ys2.append(funcs.get(func)(x))

    plt.plot(xs, ys, 'r', label='aproksy')
    plt.plot(xs2, ys2, 'y', label='real')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(title='Legenda', loc='best', fontsize='xx-small')
    plt.grid(b=True, axis='both')
    plt.show()







