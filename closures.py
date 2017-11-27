class Averager():

    def __init__(self):

        self.series = []

    def __call__(self, new_value):

        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():

    series = []

    def averager(new_value):

        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

#This version is more efficient but we need the nonlocal declaration was introduced in Python 3.
#It lets you flag a variable as a free variable even when it is assigned a new value within the function.
#If a new value is assigned to a nonlocal variable, the binding stored in the closure is changed.

def better_make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

# Simple decorator

import time

def clock(func):

    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s (%s) --> %r' % (elapsed,name,arg_str,result))
        return result

    return clocked

#An improved clock decorator

import time
import functools

#functools.wraps is just one of the ready-to-use decorators in the standard library

def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked

DEFAULT_TIME = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock_d(fmt=DEFAULT_TIME):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))  #matches with variables in the local code
            return _result #substitutes the decorated function so should return the same value
        return clocked
    return decorate



