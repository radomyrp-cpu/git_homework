result = []
def divider(a, b):
    if a < b:
        raise ValueError("a is les than b")
    if b > 100:
        raise IndexError("b is greater than 100")
    return a /b
data = {10: 2,2:5,"123": 4, 18: 0,8: 4}
try:
    data[[]] =15
except TypeError as e:
    print("TypeError:",e)
data[200] = 101
for key in data:
    try:
        res=divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, TypeError, ZeroDivisionError) as e:
        print(type(e).__name__ +":",e)
print(result)