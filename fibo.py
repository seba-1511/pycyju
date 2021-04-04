#!/usr/bin/env python3

import numpy as np
import time

import julia
julia.install()
#jl = julia.Julia(compiled_modules=False)
jl = julia.Julia()
ju_fibonacci = jl.eval('include("ju_fibo.jl")')

import pyximport
pyximport.install()
from cy_fibo import cy_fibonacci


def fibo(i):
    if i == 0 or i == 1:
        return 1
    return fibo(i-1) + fibo(i-2)


def py_fibonacci(py_result, length):
    for i in range(length):
        py_result[i] = fibo(i)


if __name__ == '__main__':
    MAX_N = 7
    py_timings = []
    cy_timings = []
    ju_timings = []
    for length in [2, 4, 8, 16, 32, 35, 38, 40, 42]:
        print('\nLength:', length)

        if length <= 32:
            # python benchmark
            py_result = np.zeros(length, dtype=np.uint)
            tic = time.time()
            py_fibonacci(py_result, length)
            toc = time.time()
            py_timings.append(toc - tic)
            print('python:', toc - tic)

        # cython benchmark
        cy_result = np.zeros(length, dtype=np.uint)
        tic = time.time()
        cy_fibonacci(cy_result, length)
        toc = time.time()
        cy_timings.append(toc - tic)
        print('cython:', toc - tic)
#        assert np.linalg.norm(cy_result - py_result) <= 1e-8, 'cython failed'

        # julia benchmark
        ju_result = np.zeros(length, dtype=np.uint)
        ju_ptr = ju_result.ctypes.data
        tic = time.time()
        ju_fibonacci(ju_ptr, length)  # No copy, pass pointer to data
#        ju_result = ju_fibonacci(ju_result, length)  # Makes a copy to AND from julia.
        toc = time.time()
        ju_timings.append(toc - tic)
        print('julia:', toc - tic)
#        assert np.linalg.norm(ju_result - py_result) <= 1e-8, 'julia failed'
