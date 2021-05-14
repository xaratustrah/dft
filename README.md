# dft
testing dft algorithm with fortran and python to check the speed and usage of f2py. Python code inspired by [this page](https://github.com/xaratustrah/dft). Fortran code written accordingly.

Before binding into python, first try to check the codes separately by themselves::

    gfortran fort_dft.f95 && ./a.out
    ./py_dft.py
    
After seeing the same results, proceed to the next section: Compile with

    f2py -c --fcompiler=gnu95 -m fort_dft fort_dft.f95
    
in iPython one can check the results, comparing the inefficient DFT fortran code, with the inefficient DFT python code. Finally the results from the highly efficient numpy FFT and Scipy FFT code is also included for comparison.

    import fort_dft, py_dft
    import random, numpy as np, scipy
    
    print(fort_dft.dft.__doc__)
    
    c = [complex(random.random(), random.random()) for s in range(2**12)]
    
    %timeit py_dft.dft(c)
    1 loops, best of 3: 29.5 s per loop
    
    %timeit fort_dft.dft(c)
    1 loops, best of 3: 563 ms per loop
    
    %timeit np.fft.fft(c)
    1000 loops, best of 3: 241 µs per loop
    
    %timeit scipy.fft(c)
    1000 loops, best of 3: 238 µs per loop


wow! :-)
