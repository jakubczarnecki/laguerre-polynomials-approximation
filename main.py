import numpy as np

from hermite import gauss_hermite
import functions as f
from utils import *
from functions import *

if __name__ == '__main__':
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

    if func == "6":
        factors = choosePolynomialFactors()

    left = np.double(input("podaj lewą stronę przedziału aproksymacji:"))
    right = np.double(input("podaj prawą stronę przedziału aproksymacji:"))
    nodes = np.int(input("podaj liczbę węzłów całkowania metodą Gaussa-Hermite'a:"))

    integral = gauss_hermite(funcs.get(func), int(nodes))





