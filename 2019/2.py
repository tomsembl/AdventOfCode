a="""1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0"""
test="""1,9,10,3,2,3,11,0,99,30,40,50"""
# a=test
b=[int(x) for x in a.split(",")]
b[1]=12;b[2]=2
i=0
while b[i]!=99:
    op = b[i]
    x,y,z = b[i+1:i+4]
    if op==1: b[z] = b[x] + b[y]
    if op==2: b[z] = b[x] * b[y]
    i+=4
answer = b[0]
print(answer)#part1


a=[int(x) for x in a.split(",")]
def solve(output):
    for verb in range(100):
        for noun in range(100):
            b=a[::]
            b[1]=verb;b[2]=noun
            i=0
            while b[i]!=99:
                op = b[i]
                x,y,z = b[i+1:i+4]
                if op==1: b[z] = b[x] + b[y]
                if op==2: b[z] = b[x] * b[y]
                i+=4
            if b[0] == output: return (verb,noun)
verb,noun = solve(19690720)
print(verb,noun)
print(100*verb+noun)
#666000 too high