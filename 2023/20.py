a=r"""%cf -> hl, qt
&bn -> rx
%nb -> vt
%hm -> jp
%vr -> qt, sl
%gq -> hm, nl
%sl -> jx, qt
&pl -> bn
%hf -> vt, ch
%kx -> dq
%fr -> qf
%rh -> vr
&vt -> lz, dh, kr, kq, lm, qk
&dq -> mz, ml, xd, fb, xs, rc, rt
%hn -> qk, vt
%bv -> nl
%jv -> rh, qt
%kq -> lm
%nd -> hp
%gj -> bv, nl
%lv -> xs, dq
%ch -> vt, kd
%sm -> qt, nd
%nt -> jv
%qk -> cb
%jx -> cf
%hl -> qt, ng
&qt -> sm, rh, nd, jx, nt, pl
%bh -> nl, fr
%kd -> vt, nb
%gx -> mh, dq
%hp -> nt, qt
%rc -> lv
broadcaster -> kr, zb, sm, xd
&mz -> bn
%qf -> rd, nl
%sk -> nl, bh
%rb -> nl, sk
%cb -> hf, vt
%fb -> rt
&lz -> bn
%mh -> dq, kx
%rt -> mt
%xd -> dq, fb
%lm -> hn
%hh -> vt, dh
%ml -> ts
%mt -> rc, dq
%ts -> gx, dq
%rd -> nl, gq
%zb -> nl, rb
%kr -> hh, vt
&nl -> fr, zb, hm, zm
&zm -> bn
%dh -> kq
%ng -> qt
%xs -> ml
%jp -> nl, gj"""
test=r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
test=r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
#a=test
b=[x for x in a.splitlines()]
OutputMapping={}
InputMapping={}
#[0] = type (%,&), [1] = connections
for x in b:
    connections = x.split(" -> ")[1].split(", ")
    if x.startswith("broadcaster"):
        name = "broadcaster"
        type = "low"
    else:
        type = x[0]
        name = x[1:].split(" -> ")[0]
    OutputMapping[name] = [type, connections]
    for y in connections:
        InputMapping.setdefault(y,[]).append(name)
    
# for x in OutputMapping:
#     print(x,OutputMapping[x])
# print("\ninput Mapping\n")
# for x in InputMapping:
#     print(x,InputMapping[x])
    
#timestamp, name, signalReceived (0=low, 1=high)
memory = {}
for x in OutputMapping:
    if OutputMapping[x][0] == "%":
        memory[x] = 0
    elif OutputMapping[x][0] == "&":
        memory[x] = {x:0 for x in InputMapping[x]}
lowHighPulses = [0,0]

def buttonPush():
    queue = [[0, "button", "broadcaster", 0]]
    while queue:
        timestamp, nameFrom, nameTo, signalReceived = queue.pop(0)
        lowHighPulses[signalReceived] += 1
        #print(timestamp, nameFrom, ["low","high"][signalReceived], nameTo)
        type, connections = OutputMapping[nameTo]
        if type == "%":
            if signalReceived == 0:
                memory[nameTo] = 1-memory[nameTo]
                signalSent = memory[nameTo]
            else: continue
        elif type == "&":
            memory[nameTo][nameFrom] = signalReceived
            signalSent = 0 if all([y==1 for y in memory[nameTo].values()]) else 1
        else:
            signalSent = signalReceived
        for connection in connections:
            if connection not in OutputMapping:
                #print(nameTo, ["low","high"][signalSent], connection)
                lowHighPulses[signalSent] += 1
                continue
            queue.append([timestamp+1, nameTo, connection, signalSent])
for _ in range(1000):
    buttonPush()
    #print()
result = 1
#print(lowHighPulses)
for lh in lowHighPulses:
    result *= lh
print(result)