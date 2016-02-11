#!/usr/bin/env python
#
# double precision dft subroutine
# xaratustrah
# 2016
#

import cmath


def dft(x):
    xre = [s.real for s in x]
    xim = [s.imag for s in x]
    n = len(xre)
    y = [complex(0, 0)] * n
    for k in range(n):  # For each output element
        sumreal = 0.0
        sumimag = 0.0
        for t in range(n):  # For each input element
            angle = 2 * cmath.pi * t * k / n
            sumreal += xre[t] * cmath.cos(angle) + xim[t] * cmath.sin(angle)
            sumimag += -xre[t] * cmath.sin(angle) + xim[t] * cmath.cos(angle)
        y[k] = complex(sumreal, sumimag)
    return y


# ----------------------------

def main():
    x = [complex(1, 2), complex(2, 3), complex(3, 4), complex(4, 5)]
    y = dft(x)
    print(x)
    print(y)


if __name__ == '__main__':
    main()
