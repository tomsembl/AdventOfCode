# for x in range(31):
#     output = ""
#     if x % 3 == 0: output += "fizz"
#     if x % 5 == 0: output += "buzz"
#     print(x if output=="" else output)

for x in range(31): print(x if (output:=("fizz" if x % 3 == 0 else "") + ("buzz" if x % 5 == 0 else ""))=="" else output)