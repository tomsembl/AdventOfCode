def rec(x,y):
    print(x)
    ytemp = y
    y = x + y
    x = ytemp
    if x > 100: 
        return
    rec(x,y)

rec(0,1)