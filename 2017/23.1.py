a="""set b 65
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""
r={chr(x):0 for x in range(97,97+8)}
h=0
for b in range(65 * 100 + 100_000, 65 * 100 + 100_000 + 17000 + 1,17):
    for d in range(2,int(b**0.5)+1):
        if b % d == 0:
            h += 1
            break
print(h)#part 2

#part 2
#123500 too high
#500 too low
#501 too low
#1001 not right
#1455 not right

# r["b"]=65
# r["c"] = r["b"]
# if a!=0:
#     r["b"] = r["b"] * 100 + 100_000
#     r["c"] = r["b"] + 17000
# for b in range(106500,123500+1,17):
# #while True:
#     print(r)
#     r["f"] = 1
#     #b = r["b"]
#     for d in range(2,b+1):
#         print(d,r)
#         #b = r["b"]
#         for e in range(2,b+1):
#             if d * e == b:
#                 r["f"] = 0
#     if r["f"] != 0:
#         r["f"] += 1
#     #if r["b"] == r["c"]:
#     #    break
#     #r["b"] += 17
# print(r["h"])


