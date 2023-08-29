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

a=get_input(2017,9)
print(a)

tests=[
    "<>", #0 characters.
    "<random characters>", #17 characters.
    "<<<<>", #3 characters.
    "<{!>}>", #2 characters.
    "<!!>", #0 characters.
    "<!!!>>", #0 characters.
    "<{o\"i!a,<{i<a>", #10 characters.
]
#for test in tests:
#    a=test
depth = 0
garbage = False
cancel = False
groupCount = 0
garbageCount = 0
for x in a:
    if garbage:
        if cancel:
            cancel = False
            continue
        elif x==">":
            garbage = False
            continue
        elif x=="!":
            cancel = True
            continue
        else: garbageCount += 1
    else:
        if x=="<":
            garbage = True
            continue
        elif x=="{":
            depth += 1
            groupCount += depth
            continue
        elif x=="}":
            depth -= 1
            continue
    
print(groupCount)#part 1: 12396
print(garbageCount)#part 2: 6346
#7663 too high
#6782 too high