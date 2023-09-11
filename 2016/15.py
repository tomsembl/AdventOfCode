a="""Disc #1 has 5 positions; at time=0, it is at position 2.
Disc #2 has 13 positions; at time=0, it is at position 7.
Disc #3 has 17 positions; at time=0, it is at position 10.
Disc #4 has 3 positions; at time=0, it is at position 2.
Disc #5 has 19 positions; at time=0, it is at position 9.
Disc #6 has 7 positions; at time=0, it is at position 0."""
test="""Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""
a=[[5,2],[13,7],[17,10],[3,2],[19,9],[7,0]]
test=[[5,4],[2,1]]
#a=test
def part(p):
    if p==2: a.append([11,0])
    i=0
    l=len(a)
    for i in range(10_000_000):
        iCopy = i
        continuer = False
        for j in range(l):
            i+=1
            y,x=a[j]
            if (i + x) % y != 0:
                continuer = True
                break
        if continuer: continue 
        print(iCopy)
        break

        i+=1
part(1)
part(2)