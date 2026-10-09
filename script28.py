class Counter:
    def __init__(self,max_number):
        self.max_number=max_number
    def __iter__(self):
        for i in range(1, self.max_number+1):
            yield i
count= Counter(5)
iterator =iter(count)
print(type(iterator))
for elem in iterator:
    print(elem)