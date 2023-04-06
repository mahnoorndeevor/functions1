
def all(*i):
    total=0
    for num in i:
        total=total+num
    return total
sum=all(1, 2, 3, 5, 5, 6, 7, 7, 7, 8)
print(sum)