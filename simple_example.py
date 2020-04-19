import time

def slow_calculation(cb = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if cb:
            cb()
    return res

# We can call this "slow_calculation fuction without a callback and it will work fine"
print (slow_calculation())


# but we can have a callback, a function (cb) passed to it where it just prints "Yay !! a calculation is done"

def print_a_statement():
    print ("Yay !! a calculation is done")


slow_calculation(print_a_statement)

# we can have a callback that takes a parameter.. let say we want to know what value of i is calculated

def print_with_param(num):
    print("Yay ### just completed "+ str(num) + " iteration")

# to pass this callback function to slow calculation function we need to pass a parameter to cb in original function.
def slow_calculation_with_callback_param(cb = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if cb:
            cb(i)
    return res

slow_calculation_with_callback_param(print_with_param)