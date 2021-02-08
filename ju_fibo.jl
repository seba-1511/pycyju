
function fibo(x::Int)::Int
    x==0 && return one(x)
    x==1 && return one(x)
    return fibo(x-1) + fibo(x-2)
end

function ju_fibonacci(result, length::Int)
    for i = 1:length
        result[i] = fibo(i-1)
    end
    return addr
end

function ju_fibonacci_ptr(addr, length::Int)
    result = unsafe_wrap(Array{UInt64}, Ptr{UInt64}(addr), length)
    for i = 1:length
        result[i] = fibo(i-1)
    end
    return addr
end
