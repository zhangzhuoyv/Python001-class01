from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrap_timer(*args,**kwargs):
        start_time =time.time()
        result = func(*args,**kwargs)
        stop_time = time.time()
        run_time=stop_time - start_time
        print(f'程序 {func.__name__} 运行时间为{run_time}')
        return result
    return wrap_timer



@timer
def add(x,y):
    return x+y


add(5,6)


