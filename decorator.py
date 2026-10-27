'''A decorator is a callable that takes another function as argument (the
decorated function).
Decorators have the power to replace the decorated function with a
different one.'''

def decorator(func):
    def wrapper():
        print("Something is happening before the target function is called.")
        func()
        print("Something is happening after the target function is called.")
    return wrapper
def target():
    print("I am a target function!")

target = decorator(target)
target()

#--------------
class MaxVolumeExceededError(Exception):
    pass
def volume_limiter(func):
    def wrapper(self, clip):
        max_volume = self.check_volume(clip)
        if max_volume <= self.desired_level:
            func(self, clip)
        else:
            raise MaxVolumeExceededError(f"{max_volume} exceeded the limit: {self.desired_level}")
    return wrapper

class Earphone:
    def __init__(self):
        self.desired_level = 85
    def check_volume(self, clip):
        return max(clip.volumes)
    @volume_limiter
    def play(self, clip):
        print("Playing clip with volumes:", clip.volumes)
class Clip:
    def __init__(self, volumes):
        self.volumes = volumes

bose = Earphone()
clip1 = Clip([12,34,56,63,85])
clip2 = Clip([12,34,56,63, 89])
try:
    bose.play(clip1)
    bose.play(clip2)
except MaxVolumeExceededError as e:
    print(e)

#----------
def dec1(func):
    def wrapper():
        print("Inner decorator starts")
        func()
        print("Inner decorator ends")
    return wrapper
def dec2(func):
    def wrapper():
        print("Outer decorator starts")
        func()
        print("Outer decorator ends")
    return wrapper

def dec3(func):
    count = 1
    def wrapper():
        nonlocal count
        if count > 0:
            func()
            count -= 1
    return wrapper
@dec3
@dec2
@dec1
def printer():
    print ("Hello")
printer()
print("------------")
printer()
print("------------")
printer()

#-----timing of functions -------------
import functools
from inspect import signature
from os import name
import time

from anyio import value
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])

waste_some_time(1)
waste_some_time(999)

#---debugging--------
import functools
def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug
@debug
def fibonacci(n):
    if n==1 or n==0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))

#register of functions
PLUGINS = dict()
def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func
@register
def say_hello(name):
    return f"Hello {name}"
@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

print(PLUGINS)
















