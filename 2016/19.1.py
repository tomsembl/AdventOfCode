#getting the pattern
for x in range(5,100):
    y = [z for z in range(x)]
    i=0
    while len(y)>1:
        z=y[i]
        ly = len(y)
        y.remove(y[(i+ly//2)%ly])
        i=y.index(z)
        i=(i+1)%(ly-1)
    print(x,y[0]+1)

# for input in range(5,50):
input = 3017957
x = 0
while 3**x<input:
    x+=1
x-=1
print(input, input - 3**x + (input - (2*3**x) if input>2*3**x else 0))
#     y = 2
#     x = 5
#     z = 1
#     while True:
#         z += 1 if z <= 3**(y-1) else 2
#         if x == input: 
#             print(z)
#             break
#         if x == 3**y:
#             y += 1
#             z = 0
#         x += 1

