#Finonacci

from functools import lru_cache

@lru_cache()

def fibonacci(num):

    if num == 0:
        fib = 0
    elif num == 1:
        fib = 1
    else:
        fib = fibonacci(num-1) + fibonacci(num-2)
    return fib

    #
    # fib = 0
    # fib1 = 1
    # fib2 = fib0+fib1 # 0+1 = 1
    # fib3 = fib2+fib1 # 1+1 = 2
    # fib4 = fib3+fib2 # 2+1 = 3
    # fib5 = fib4+fib3 # 3+2 = 5
    # fib6 = fib5+fib4 # 5+3 = 8
    # fib7 = fib6+fib5 # 8+5 = 13
    # fib8 = fib7+fib6 # 13+8 = 21
    # fib9 = fib8+fib7 # 21+13 = 24

    # if num == 0:
    #     fib = 0
    # if num == 1:
    #     fib = 1
    # if num == 2:
    #     fib = fib2 #F(2)=F(1) + F(0)
    # if num == 3:
    #     fib = fib3
    # if num == 4:
    #     fib = fib4
    # if num == 5:
    #     fib = fib5
    # if num == 6:
    #     fib = fib6
    # if num == 7:
    #     fib = fib7
    # if num == 8:
    #     fib = fib8
    # if num == 9:
    #     fib = fib9
    #
    # return fib

if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
