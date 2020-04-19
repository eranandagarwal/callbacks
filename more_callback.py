import time

def slow_calculation(cb = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if cb:
            cb(i)
    return res


# what if we do not define a function for callback, instead use lambda for same

slow_calculation(lambda num: print (f"Yay !! we have reached {num} iteration"))


# What if we do ot want to write "Yay !!" always and now want to send the exclamation as an argument. we will have to change the callback in slow_calculation fntion as 2 argument. But we can do without that
def show_progress(exclamation,num):
    print (f"{exclamation} we are in {num} iteration")

#now we can call slow calculation passing lambda in below way
slow_calculation(lambda num: show_progress("Awesome !!", num))

# we can do the same without lambda, with a proper function
def show_progress_as_closure(exclamation):
        _inner = lambda iteration: print (f"{exclamation} we are in {iteration} iteration")
        return _inner

slow_calculation (show_progress_as_closure("Nice !!"))

# instead of _inner having the function we can have a fiunction defined as well.

def show_progress_as_function(exclamation):
        def _inner(iteration):
            print (f"{exclamation} we are in {iteration} iteration")
        return _inner

slow_calculation (show_progress_as_function("cool !!"))

# now we can use the above closure function to store a function with a excalmation 
f = show_progress_as_function("great !!")
slow_calculation(f)

# another thing that we can do to make a function that excets 2 argument to take 1 argument is to use partial from functools
from functools import partial

# show_progress is a function that takes 2 argument, exclamation and num. 
f1 = partial (show_progress , "partial !!") # this convert the function to 1 argument where the 1st one is "partial !!"
slow_calculation(f1)