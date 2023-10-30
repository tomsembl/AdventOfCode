target = [3075,2981]

matrix = [[0 for x in range(7)] for y in range(7)]
code=20151125
y=1
while True:
    for i in range(y):
        if [1+i,y-i] == target:
            print(code)
        code = (code * 252533) % 33554393
    y += 1