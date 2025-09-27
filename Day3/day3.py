
numbers = ["1","2","3","4","5"]

def square(a):
    return a ** 2


result = [square(int(num))for num in numbers]

print(result)


h = [(int(num))for num in numbers]

print(h)