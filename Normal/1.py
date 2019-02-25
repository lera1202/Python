#a = input()
#x = max(a)
#print(x)


x = int(input())
_max = 0
while x > 0:
    a = x % 10
    if a > _max:
        _max = a
    x //= 10
print(_max)



