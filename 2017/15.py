fa=16807
fb=48271
mod1=2147483647

a=516
b=190

#test
# a=65
# b=8921

mod2 = 2**16

def part1():
    iterations = 40_000_000
    total = 0
    for _ in range(iterations):
        a = ((a * fa) % mod1)# % mod2
        b = ((b * fb) % mod1)# % mod2
        if a % mod2 == b % mod2: total += 1
    print(total)
#part1()

def part2():
    global a,b
    iterations = 5_000_000
    total = 0
    qa,qb=[],[]
    while iterations > 0:
        while not qa:
            a = ((a * fa) % mod1)# % mod2
            if a%4==0: 
                qa.append(a)
        while not qb:
            b = ((b * fb) % mod1)# % mod2
            if b%8==0: 
                qb.append(b)
        if qa and qb:
            if iterations%10_000 == 0: print(iterations, len(qa), len(qb))
            iterations-=1
            a2,b2 = qa.pop(0),qb.pop(0)
            if a2 % mod2 == b2 % mod2: 
                total += 1
    print(total)
part2()
