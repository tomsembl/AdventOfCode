a="""deal into new stack
deal with increment 65
cut -850
deal with increment 73
cut -691
deal with increment 59
cut 10000
deal with increment 72
deal into new stack
cut -7966
deal with increment 63
cut 1076
deal with increment 33
cut -7818
deal with increment 35
cut 4420
deal with increment 35
cut -4594
deal with increment 10
cut -8389
deal into new stack
deal with increment 2
cut -3087
deal into new stack
cut 3795
deal with increment 27
cut -9961
deal with increment 63
cut -3494
deal with increment 43
cut -1920
deal with increment 58
cut 3436
deal with increment 29
cut 6173
deal with increment 27
cut 5631
deal into new stack
cut -6605
deal with increment 19
cut 5337
deal with increment 7
cut 6315
deal into new stack
deal with increment 28
deal into new stack
deal with increment 35
deal into new stack
cut -6216
deal with increment 58
deal into new stack
deal with increment 16
cut 7413
deal into new stack
cut 5449
deal into new stack
cut -3801
deal with increment 35
cut -6555
deal with increment 41
cut 7341
deal with increment 48
deal into new stack
deal with increment 49
cut 8059
deal with increment 16
cut 9144
deal with increment 45
deal into new stack
cut 3195
deal with increment 2
cut -5432
deal with increment 22
cut -7629
deal with increment 70
cut -4118
deal with increment 53
deal into new stack
deal with increment 30
cut 4189
deal with increment 19
cut -9197
deal with increment 55
cut -347
deal into new stack
cut 4040
deal with increment 34
cut -2743
deal into new stack
cut -6206
deal with increment 48
cut -7099
deal with increment 75
cut -9572
deal with increment 41
cut 7531
deal with increment 59
deal into new stack
cut -5
deal into new stack"""
test="""deal with increment 7
deal into new stack
deal into new stack
"""
test = """cut 6
deal with increment 7
deal into new stack"""

test = """deal with increment 7
deal with increment 9
cut -2"""

test="""deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""
#a=test
b=[x.split() for x in a.splitlines()]
size = 119315717514047

deck=[x for x in range(size)]
for instr in b:
    n = instr[-1]
    if n[-1].isnumeric(): n = int(n)
    else:
        deck = deck[::-1] #reverse
        continue
    if instr[0] == "cut":
        deck = deck[n:] + deck[:n]
        continue
    if instr[0:2] == ["deal","with"]:
        dicti = {(x*n%size):x for x in range(size)}
        deck = [deck[dicti[x]] for x in range(size)]
print(deck.index(2020))