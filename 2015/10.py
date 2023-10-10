a="1321131112"
test="111221"
#a=test
def lookAndSay(x):
    last = x[0]
    count=1
    out = ""
    for y in x[1:]:
        if y!=last:
            out += str(count) + last
            count=0
        last = y
        count += 1
    out += str(count) + last
    return out
def part(p):
    a="1321131112"
    for _ in range(40 if p==1 else 50):
        a=lookAndSay(a)
    print(len(a))
part(1)
part(2)