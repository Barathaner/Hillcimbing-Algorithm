# Press the green button in the gutter to run the script.

import random
import numpy as np


def mutiere(a):
    a=a.copy()
    index = random.randint(0, (len(a)-1))
    if a[index] == 0:
        a[index] = 1
    elif a[index] == 1:
        a[index] = 0
    return a


def binmutiere(x):
    x= x.copy()
    probMut = 1.0 / (len(x))
    for i in range(0, len(x)):
        u = random.uniform(0.0, 1.0)
        if u <= probMut:
            if x[i] == 0:
                x[i] = 1
            elif x[i] == 1:
                x[i] = 0
    return x


def onemax(a):
    bewertung = 0
    for i in a:
        if i == 1:
            bewertung += 1
    return bewertung



def leadingzeros(a):
    zerocounter = 0
    for i in range(0,(len(a))):
        if zerocounter== i and a[i] == 0:
            zerocounter+=1
    return zerocounter


def balancedleadingzeros(a):
    return min(leadingzeros(a),onemax(a))


def hillclimbing(bewertungsfunc):
    a = np.random.choice([0, 1], size=(10,), p=[1. / 3, 2. / 3])
    counter = 0
    while bewertungsfunc(a) != 5:
        print(counter, " - Alt ", a)
        b = binmutiere(a)
        print("Neu- ", b)
        bewertunga = bewertungsfunc(a)
        bewertungB = bewertungsfunc(b)
        if bewertungB >= bewertunga:
            a = b
        counter += 1
    return a


if __name__ == '__main__':
    hillclimbing(balancedleadingzeros)
