def getNeighs(stone):
    x,y=stone
    return [(x+xx,y+yy) for xx,yy in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]]

def first_impossible(stones):
    print(stones)
    def readGrid(grid,target):
        blankNeighs={}
        output=[]
        for stone in grid:
            for neigh in getNeighs(stone):
                if neigh not in grid: 
                    if neigh not in blankNeighs: blankNeighs[neigh]=[]
                    blankNeighs[neigh].append(stone)
        for stone in blankNeighs:
            total=0
            for neigh in blankNeighs[stone]:
                total += grid[neigh]
            if total==target:
                output.append(stone)
        return output
    
    max=1
    grid={stone:1 for stone in stones}
    queue=[(2,grid)]
    while queue:
        current,grid = queue.pop()
        if current>max: max=current
        for newStone in readGrid(grid,current):
            gridCopy=grid.copy()
            gridCopy[newStone]=current
            queue.append((current+1,gridCopy))
    print(max)
    return max
    

sample_test_cases = [
    ('2 stones', [
        ([(0,0), (0,3)],   2),
        ([(0,0), (0,2)],   6),
        ([(0,0), (1,0)],  11),
        ([(1,2), (3,3)],  13),
        ([(0,0), (2,2)],  17),
    ]),
    ('3 stones', [
        ([(0,4), (1,0), (4,4)],   2),
        ([(0,0), (0,1), (1,1)],  15),
        ([(2,0), (0,2), (2,2)],  19),
        ([(0,2), (3,0), (5,2)],  26),
    ]),
    ('4–6 stones', [
        ([(0,0), (2,1), (2,2), (3,3)],                25),
        ([(3,2), (3,0), (1,6), (0,7), (3,1)],         23),
        ([(8,2), (1,0), (2,5), (0,7), (3,6), (6,8)],  34),
    ]),
]

for name, test_cases in sample_test_cases:
    print(name)
    for stones, expected in test_cases:
        print("test",stones, first_impossible(stones), expected)