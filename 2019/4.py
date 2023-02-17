def check(x):
    x=str(x)
    last=x[0]
    double=False
    for i,y in enumerate(x):
        if y<last: return False
        if y==last and i!=0: double=True
        last=y
    return double

total=0
for x in range(108457,562041+1):
    if check(x):
        total+=1
print(total)
#2863 too high