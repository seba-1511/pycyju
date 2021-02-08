# cython: language_level=3


cdef unsigned long fibo(unsigned long i):
    if i == 0 or i == 1:
        return 1
    return fibo(i-1) + fibo(i-2)


cpdef cy_fibonacci(unsigned long[::1] py_result, unsigned long length):
    for i in range(length):
        py_result[i] = fibo(i)


