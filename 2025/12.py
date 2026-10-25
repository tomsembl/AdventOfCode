a=""""""
test="""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
a=test
shapes=[x.splitlines()[1:] for x in a.split("\n\n")[:-1]]
shape_areas=[x.count("#") for x in a.split("\n\n")[:-1]]
areas=[[[int(y) for y in x.split(": ")[0].split("x")], [int(y) for y in x.split(": ")[1].split()]] for x in a.split("\n\n")[-1].splitlines()]

print(shape_areas,"\n",areas)
for (x,y),counts in areas:
    area = x*y
    total_area = sum([shape_areas[i]*x for i,x in enumerate(counts)])
    print(area, total_area)