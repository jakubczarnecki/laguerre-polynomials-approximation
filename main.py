import numpy as np

from functions import *

if __name__ == '__main__':
    print("\n\nMetody numeryczne - zadanie 5. Aproksymacja")
    print("Wariant 3 - wielomiany Laguerre'a\n")

    funcs = {
        "1": f1,
        "2": f2,
        "3": f3,
        "4": f4,
        "5": f5,
        "6": f6
    }

    func = input("\n 1. f(x) = |2x - 3|"
                 "\n 2. f(x) = sin(x)"
                 "\n 3. f(x) = cos(2x)"
                 "\n 4. f(x) = x^2"
                 "\n 5. f(x) = cos(sin(x))"
                 "\n 6. f(x) = 3x^4 - 2x^3 + 4x^2 + x + 1"
                 "\n Wybierz funkcję: ")

    left = np.double(input("podaj lewą stronę przedziału aproksymacji:"))
    right = np.double(input("podaj prawą stronę przedziału aproksymacji:"))
