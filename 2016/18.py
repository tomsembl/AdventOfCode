a="""^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^"""
h=40
test=".^^.^.^^^^"
b=[a]
for j in range(1,h):
    newRow = ""
    for i in range(len(a)):
        start, mid, end = ("." if i==0 else ''), b[j-1][0 if i==0 else i-1:i+2], ("." if i==len(a)-1 else '')
        slice = start + mid + end 
        newRow += "^" if slice in ["^^.",".^^","^..","..^"] else "."
    b.append(newRow)
for y in b: print(y)
print(sum([y.count(".") for y in b]))# part 1

safes = a.count(".")
for _ in range(400_000-1):
    newRow = ""
    for i in range(len(a)):
        start, mid, end = ("." if i==0 else ''), a[0 if i==0 else i-1:i+2], ("." if i==len(a)-1 else '')
        slice = start + mid + end 
        newRow += "^" if slice in ["^^.",".^^","^..","..^"] else "."
    a=newRow
    safes += a.count(".")
print(safes)