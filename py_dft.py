#!/usr/bin/env python
#
# double precision dft subroutine
# xaratustrah
# 2016
#

#import cmath
import math
import numpy as np


def dft(x):
    xre = [s.real for s in x]
    xim = [s.imag for s in x]

    n = len(xre)
    y = [complex(0, 0)] * n
    
    for k in range(n):  # For each output element
        sumreal = 0.0
        sumimag = 0.0
        for t in range(n):  # For each input element
            angle = 2 * math.pi * t * k / n
            sumreal += xre[t] * math.cos(angle) + xim[t] * math.sin(angle)
            sumimag += -xre[t] * math.sin(angle) + xim[t] * math.cos(angle)
        y[k] = complex(sumreal, sumimag)
    return y


# ----------------------------

def main():
    x = [complex(1, 2), complex(2, 3), complex(3, 4), complex(4, 5)]
    y = dft(x)
    print('In:')
    print(x)
    print('Out:')
    print(y)
    print(np.fft.fft(x))

if __name__ == '__main__':
    main()
