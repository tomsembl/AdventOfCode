# monster="""                  # 
# #    ##    ##    ###
#  #  #  #  #  #  #   """
# #
# def hashToBin(h): return int("0b"+"".join(["".join(["1" if y=="#" else "0" for y in x]) for x in h]),2)
# def rotate(x): return [ "".join(y) for y in list(zip(*x[::-1])) ]
# def flip(x): return [ y[::-1] for y in x ]
# monster = monster.splitlines()
# mh,mw = len(monster), len(monster[0])
# monsters=[monster,flip(monster)]
# for m in monsters[::]:
#     for _ in range(3):
#         m = rotate(m)
#         monsters.append(m)
# monsters={hashToBin(x):{"str":x,"h":len(x)} for x in monsters}


# for monster in monsters:
#     print(monster)
#     print(monsters[monster]["h"])
#     for row in monsters[monster]["str"]: 
        
#         print(row)
# for j,row in enumerate()
a=""".####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#"""
count = sum([sum([1 for x in y if x=="#"]) for y in a.splitlines()])
print(count)