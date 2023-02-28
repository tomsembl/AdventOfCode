a="""2 KBRD => 3 NSPQ
1 TMTNM, 5 WMZD => 4 JVBK
3 TMTNM => 8 JTPF
3 NDXL => 2 BDQP
2 VTGNT => 2 TNWR
1 ZQRBC => 2 WGDN
2 MJMC => 3 QZCZ
10 MDXVB, 3 DHTB => 1 SRLP
1 KBRD, 1 PNPW => 6 SQCB
1 KDTRS, 4 VTGNT => 7 NDXL
1 FZSJ => 1 CJPSR
6 TKMKD => 8 FTND
2 ZNBSN => 4 DNPT
16 SKWKQ, 2 FZSJ, 3 GSQL, 1 PNRC, 4 QNKZW, 4 RHZR, 10 MTJF, 1 XHPK => 3 RJQW
1 NHQW => 8 QNKZW
16 JZFCN, 9 KWQSC, 1 JGTR => 7 TMTNM
2 PNRC => 7 LCZD
1 NLSNC, 14 SXKC, 2 DHTB => 1 ZQRBC
1 MXGQ, 2 KWQPL => 3 FZSJ
6 DWKLT, 1 VHNXW, 3 NSPQ => 1 BQXNW
23 KDTRS => 1 XHPK
1 PFBF, 3 KBLHZ => 3 MBGWZ
5 NSPQ => 3 TPJP
27 SRLP, 12 KWQSC, 14 ZNBSN, 33 HQTPN, 3 HWFQ, 23 QZCZ, 6 ZPDN, 32 RJQW, 3 GDXG => 1 FUEL
2 NSPQ, 5 ZNBSN, 1 TPJP => 8 PFBF
1 MSCRZ => 3 ZNBSN
1 TNWR, 2 ZNBSN => 5 MDXVB
10 SQCB => 5 MXGQ
3 JVBK, 1 MTJF, 1 KBLHZ => 2 HQTPN
2 MJMC => 2 KMLKR
2 BQXNW, 1 CJPSR, 25 KWQPL => 4 PNRC
1 VHNXW, 3 KWZKV => 4 TKMKD
10 VTGNT, 4 JTPF => 9 KWZKV
168 ORE => 3 JZFCN
173 ORE => 5 KBRD
2 TNWR, 1 MBGWZ, 3 NSPQ => 8 SKWKQ
1 KWZKV, 2 MJMC, 14 SKWKQ => 9 NSTR
4 JZFCN, 13 PNPW => 2 WMZD
6 JQNGL => 6 MGFZ
1 SQCB, 4 NLSNC => 5 DHTB
5 MGFZ, 39 WGDN, 1 MBGWZ, 2 NSTR, 1 XKBND, 1 SXKC, 1 JVBK => 5 ZPDN
7 NSPQ, 6 PNPW => 7 NLSNC
3 TNWR => 9 KWQPL
9 NLSNC, 4 NDXL, 1 MDXVB => 4 MTJF
2 VTJC => 7 PNPW
2 JZFCN => 8 MSCRZ
134 ORE => 3 JGTR
3 HQTPN => 4 GSQL
154 ORE => 9 VTJC
1 KWQSC, 14 KBRD => 4 JQCZ
7 PNRC, 1 XKBND => 8 RHZR
1 JQCZ => 4 VTGNT
6 BDQP => 6 JQNGL
7 FTND => 3 XKBND
2 XHPK, 4 NHQW => 1 MJMC
1 JQCZ => 5 KDTRS
1 DNPT => 4 KBLHZ
1 KMLKR, 26 ZNBSN, 1 LCZD, 11 QNKZW, 2 SQCB, 3 FTND, 24 PNRC => 4 HWFQ
179 ORE => 6 KWQSC
2 TKMKD, 3 FZSJ => 2 SXKC
2 JTPF => 7 VHNXW
1 FTND => 7 DWKLT
13 TNWR, 2 QNKZW, 6 SQCB => 5 GDXG
5 JTPF, 4 ZNBSN, 8 WMZD => 8 NHQW"""
test="""10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
test="""9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""
test="""157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
test="""2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""
test="""171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""
#a=test
b={(v:=(y:=x.split(" => "))[1].split(" "))[1]:{"ingr":{z.split(" ")[1]:int(z.split(" ")[0]) for z in y[0].split(", ")},"qty":int(v[0])} for x in a.splitlines()}

def traverse(node,qty):
    global totalOre
    if node=="ORE": 
        totalOre += qty
        return
    stdQty = b[node]["qty"]
    if leftovers[node]>qty:
        leftovers[node]-=qty
        qty=0
    else: 
        qty-=leftovers[node]
        leftovers[node]=0
    if qty==0: return
    finalQty = 1 if stdQty>=qty else -(-qty//stdQty)
    leftovers[node]+=(finalQty*stdQty)-qty
    ingrs=b[node]["ingr"]
    for ingr in ingrs:
        ingrQty=ingrs[ingr]
        traverse(ingr,finalQty*ingrQty)

def makeNfuel(n):
    global leftovers,totalOre
    leftovers={x:0 for x in b}
    totalOre=0
    traverse("FUEL",n)
    return totalOre
part1 = makeNfuel(1)
print(part1)#part1

tril=1_000_000_000_000
n=tril//part1
totalOre = makeNfuel(n)
n=int(n/(totalOre/tril))
print(n)
while True:
    totalOre = makeNfuel(n)
    if totalOre>tril: 
        print(n-1)#part2
        break
    n+=1

#218452 too high
#6984557 too low