import requests
import os

session = "53616c7465645f5fdafba19a72e09bbba124002ae729b6c034cd0eb868342455046900c29b32592461042869ddfebab282d4b3ca7af4eb447a9b042786140379"
def get_input(year,day):
    try:
        with open(f"input/{year}/{day}.txt") as f:
            return f.read()
    except FileNotFoundError:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        headers = {'Cookie': 'session=' + session}
        r = requests.get(url, headers=headers)
        os.makedirs(f"input/{year}", exist_ok=True)
        with open(f"input/{day}.txt", "w") as f:
            f.write(r.text)
        return r.text

a=get_input(2017,10)[:-1]
b=[ord(x) for x in a] + [17, 31, 73, 47, 23]
size=5
size = 256
c = list(range(size))
pos = 0
skip = 0
for round in range(64):
    for length in b:
        slice = (c*2)[pos:pos+length]
        endPos = (pos+length)%size
        antiSlice = c[endPos:]+c[:pos] if endPos >= pos else c[endPos:pos]
        c = slice[::-1] + antiSlice
        c = (c*2)[size-pos:2*size-pos]
        pos += length + skip
        pos %= size
        skip += 1
sparseHash = c
denseSize = 16
denseHash = []
for i in range(denseSize):
    string1 = str(sparseHash[i*denseSize : (i+1)*denseSize])[1:-1].replace(", ","^")
    denseHash.append(eval(string1))
denseHashHex = "".join([hex(x)[2:].zfill(2) for x in denseHash])
print(denseHashHex) #part 2: 96de9657665675b51cd03f0b3528ba26