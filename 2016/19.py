#getting the pattern
for x in range(5,50):
    y = [1 for _ in range(x)]
    i=0
    take = False
    while y.count(1)>1:
        if y[i] == 1:
            if take: 
                y[i] = 0
                take = False
            else:
                take = True
        i+=1
        i%=x
    print(x,y.index(1)+1)
#for input in range(5,50):
input = 3017957
n=0
while 2**n<=input:
    n+=1
n-=1
print(input,2*(input-2**n)+1)
