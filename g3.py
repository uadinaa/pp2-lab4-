def func(n):
    for i in range(n+1):
        if i % 4 == 0:
            if i % 3 == 0:
                print(i)

n = int(input())
func(n)