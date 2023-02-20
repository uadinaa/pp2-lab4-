def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
even_num = even(n)
even_str = ",".join(str(num) for num in even_num)
print(even_str)
