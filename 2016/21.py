a="""move position 2 to position 6
move position 0 to position 5
move position 6 to position 4
reverse positions 3 through 7
move position 1 to position 7
swap position 6 with position 3
swap letter g with letter b
swap position 2 with position 3
move position 4 to position 3
move position 6 to position 3
swap position 4 with position 1
swap letter b with letter f
reverse positions 3 through 4
swap letter f with letter e
reverse positions 2 through 7
rotate based on position of letter h
rotate based on position of letter a
rotate based on position of letter e
rotate based on position of letter h
rotate based on position of letter c
move position 5 to position 7
swap letter a with letter d
move position 5 to position 6
swap position 4 with position 0
swap position 4 with position 6
rotate left 6 steps
rotate right 4 steps
rotate right 5 steps
swap letter f with letter e
swap position 2 with position 7
rotate based on position of letter e
move position 4 to position 5
swap position 4 with position 2
rotate right 1 step
swap letter b with letter f
rotate based on position of letter b
reverse positions 3 through 5
move position 3 to position 1
rotate based on position of letter g
swap letter c with letter e
swap position 7 with position 3
move position 0 to position 3
rotate right 6 steps
reverse positions 1 through 3
swap letter d with letter e
reverse positions 3 through 5
move position 0 to position 3
swap letter c with letter e
move position 2 to position 7
swap letter g with letter b
rotate right 0 steps
reverse positions 1 through 3
swap letter h with letter d
move position 4 to position 0
move position 6 to position 3
swap letter a with letter c
reverse positions 3 through 6
swap letter h with letter g
move position 7 to position 2
rotate based on position of letter h
swap letter b with letter h
reverse positions 2 through 6
move position 6 to position 7
rotate based on position of letter a
rotate right 7 steps
reverse positions 1 through 6
move position 1 to position 6
rotate based on position of letter g
rotate based on position of letter d
move position 0 to position 4
rotate based on position of letter e
rotate based on position of letter d
rotate based on position of letter a
rotate based on position of letter a
rotate right 4 steps
rotate based on position of letter b
reverse positions 0 through 4
move position 1 to position 7
rotate based on position of letter e
move position 1 to position 7
swap letter f with letter h
move position 5 to position 1
rotate based on position of letter f
reverse positions 0 through 1
move position 2 to position 4
rotate based on position of letter a
swap letter b with letter d
move position 6 to position 0
swap letter e with letter b
rotate right 7 steps
move position 2 to position 7
rotate left 4 steps
swap position 6 with position 1
move position 3 to position 5
rotate right 7 steps
reverse positions 0 through 6
swap position 2 with position 1
reverse positions 4 through 6
rotate based on position of letter g
move position 6 to position 4"""
text = "abcdefgh"
#text = "abcde"
text = [x for x in text]
test="""swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""
#a=test
def scramble(text):
    b=[x for x in a.splitlines()]
    for z in b:
        if z.startswith("swap position "):
            x,y = int(z.split()[2]),int(z.split()[5])
            valX = text[x]
            valY = text[y]
            text[x] = valY
            text[y] = valX
        if z.startswith("swap letter "):
            x,y = z.split()[2],z.split()[5]
            ix = text.index(x)
            iy = text.index(y)
            text[ix] = y
            text[iy] = x
        if z.startswith("rotate l") or z.startswith("rotate r"):
            dir,x = z.split()[1], int(z.split()[2])
            text = text[-x:]+text[:-x] if dir == "right" else text[x:]+text[:x]
        if z.startswith("rotate based "):
            x = z.split()[-1]
            x = text.index(x)
            x = x+2 if x>=4 else x+1
            x %= len(text)
            text = text[-x:]+text[:-x]
        if z.startswith("reverse positions "):
            x,y = int(z.split()[2]), int(z.split()[4])
            text = text[:x] + text[x:y+1][::-1] + text[y+1:]
        if z.startswith("move position "):
            x,y = int(z.split()[2]), int(z.split()[5])
            xVal = text[x]
            text = text[:x] + text[x+1:]
            text.insert(y,xVal)
    return "".join(text)
print(scramble(text))#part 1
from itertools import permutations

for perm in permutations("abcdefgh",8):
    #print(perm)
    if scramble(list(perm)) == "fbgdceah":
        print("".join(perm))#part 2
        break