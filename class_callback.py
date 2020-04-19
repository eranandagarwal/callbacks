import time

def slow_calculation(cb = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if cb:
            cb(i)
    return res

# here we are using a class for callback
# Class as such takes a exclamation as an argument and when the object is called __call__ method is called which takes one argument
class show_progress:
    def __init__(self,exclamation):
        self.exclamation = exclamation

    def __call__(self,num):
        print (f"{self.exclamation} we are in {num} iternation")

cb = show_progress("Awesome !!")

#slow_calculation(cb)


#now lets see a senariao where we want to do something before a calculation start and something after the calculation ends.
# thus we have to change the slow_calculation funtion to get 2 callbacks before and after the calculation

def slow_calculation(cb = None):
    res = 0
    for i in range(5):
        if cb:
            cb.before_call(i)  # we have 1 arguments here 
        res += i * i
        time.sleep(1)
        if cb:
            cb.after_call(i, res)  # we have 2 arguments here 
    return res

# *args and **kwargs gives us a flexibility on the way we send arguments

class stepcallback:
    def __init__(self):
        pass

    def before_call(*args , **kwargs):
        ''' this function as *args and **kwargs, thus we can call this function with any number of arguments or noi argument. our fiuntionality does not break'''
        print ("started")
    def after_call(*args , **kwargs):
        print ("done")

cb = stepcallback()

#slow_calculation(cb)

# what if we want to print iternation number in before_call function and internation and result after calculation

class stepcallback_new:
    def __init__(self):
        pass

    def before_call(self, num, **kwargs):
        print (f"before call iternation : {num}")
    def after_call(self,num, res , **kwargs):
        print (f"after calculation {num} : {res}")

#cb1 = stepcallback_new()
#slow_calculation(cb1)


# what is the call back class does not implement a before_call function. in that case slow_calculation call to cb.before_call breaks
#thus we can have a check before 

def slow_calculation(cb = None):
    res = 0
    for i in range(5):
        if cb and hasattr(cb,'before_call'):
            cb.before_call(i)  # we have 1 arguments here 
        res += i * i
        time.sleep(1)
        if cb and hasattr(cb,'after_call'):
            cb.after_call(i, res)  # we have 2 arguments here 
    return res

class stepcallback_new:
    def __init__(self):
        pass
    '''
    def before_call(self, num, **kwargs):
        print (f"before call iternation : {num}")
    def after_call(self,num, res , **kwargs):
        print (f"after calculation {num} : {res}")
    '''
#cb1 = stepcallback_new()
#print (slow_calculation(cb1))

def slow_calculation(cb = None):
    res = 0
    for i in range(5):
        if cb and hasattr(cb,'before_call'):
            cb.before_call(i)  # we have 1 arguments here 
        res += i * i
        time.sleep(1)
        if cb and hasattr(cb,'after_call'):
            if cb.after_call(i,res):
                print ("stopping as the value is more than 10")
                break
    return res



class stepcallback_condition:
    def __init__(self):
        pass

    def before_call(self, num, **kwargs):
        print (f"before call iternation : {num}")
    def after_call(self,num, res , **kwargs):
        print (f"after calculation {num} : {res}")
        if res > 10:
            return True

cb1 = stepcallback_condition()
slow_calculation(cb1)