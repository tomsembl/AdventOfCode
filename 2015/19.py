a="""Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""
test="""H => HO
H => OH
O => HH"""
#a=test
c="CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
# c="HOH"
# c="HOHOHO"
b=[z.split(" => ") for z in a.splitlines()]

def splitElements(y):
    output=[]
    for x in y:
        if x.upper()==x or x=="e":
            output.append(x)
        else:
            output[-1] += x
    return output

dic={}
for x,y in b:
    if x not in dic: dic[x]=[]
    dic[x].append(splitElements(y))

sett=set()
for i,x in enumerate(splitElements(c)):
    for y in dic:
        if y==x:
            for z in dic[y]:
                startElement = splitElements(c)
                newElement = startElement[:i] + z + startElement[i+1:]
                sett.add("".join(newElement))
print(len(sett))

def reduceOneMolecule(c):
    for i in range(len(c)-1,-1,-1): #going backwards instead of forwards magically fixed it
        for y,z in b:
            if c[i:].startswith(z):
                return c[:i]+y+c[i+len(z):]

steps = 0
while c!= "e":
    c = reduceOneMolecule(c)
    steps += 1
print(steps)