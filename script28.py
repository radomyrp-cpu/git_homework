import time
def timer(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper
@timer
def add(a,b):
    return a +b
@timer
def wait(seconds):
    time.sleep(seconds)
    return "Done"
def test_add():
    result, seconds =add(2,3)
    assert result==5
    assert seconds>=0
def test_wait():
    result, seconds=wait(0.1)
    assert result=="Done"
    assert seconds>=0.1
def test_arguments():
    result, seconds=add(a=4, b=6)
    assert result==10
    assert seconds>=0
test_add()
test_wait()
test_arguments()
print("All tests passed")
result,seconds=wait(0.1)
print("Time:",seconds)