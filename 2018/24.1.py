a="""Immune System:
1117 units each with 5042 hit points (weak to slashing; immune to fire, radiation, bludgeoning) with an attack that does 44 fire damage at initiative 15
292 units each with 2584 hit points with an attack that does 81 bludgeoning damage at initiative 18
2299 units each with 8194 hit points with an attack that does 35 radiation damage at initiative 7
1646 units each with 6315 hit points (weak to slashing) with an attack that does 37 slashing damage at initiative 14
2313 units each with 6792 hit points (weak to fire, radiation; immune to cold) with an attack that does 29 bludgeoning damage at initiative 9
2045 units each with 8634 hit points (weak to radiation) with an attack that does 36 fire damage at initiative 13
34 units each with 1019 hit points (weak to bludgeoning) with an attack that does 295 cold damage at initiative 6
157 units each with 6487 hit points (weak to slashing, cold) with an attack that does 362 radiation damage at initiative 3
1106 units each with 4504 hit points (weak to cold) with an attack that does 39 slashing damage at initiative 12
5092 units each with 8859 hit points (immune to cold, slashing) with an attack that does 12 radiation damage at initiative 16

Infection:
3490 units each with 20941 hit points (immune to fire) with an attack that does 9 bludgeoning damage at initiative 5
566 units each with 11571 hit points (weak to cold, bludgeoning) with an attack that does 40 bludgeoning damage at initiative 10
356 units each with 30745 hit points (weak to radiation) with an attack that does 147 slashing damage at initiative 8
899 units each with 49131 hit points (weak to slashing; immune to radiation, bludgeoning, fire) with an attack that does 93 cold damage at initiative 19
1203 units each with 27730 hit points (weak to cold) with an attack that does 43 slashing damage at initiative 4
22 units each with 45002 hit points (weak to bludgeoning) with an attack that does 3748 bludgeoning damage at initiative 17
3028 units each with 35744 hit points (weak to bludgeoning) with an attack that does 18 fire damage at initiative 11
778 units each with 17656 hit points (weak to fire) with an attack that does 35 bludgeoning damage at initiative 2
47 units each with 16006 hit points (immune to bludgeoning; weak to cold, radiation) with an attack that does 645 cold damage at initiative 20
4431 units each with 13632 hit points (weak to fire; immune to bludgeoning) with an attack that does 6 bludgeoning damage at initiative 1"""
test="""Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""
#a=test
army = None
class Group():
    def __init__(self,id,army,qty,hp,weakTo,immuneTo,attackType,attackDmg,initiative):
        self.id = id
        self.army = army
        self.qty = qty
        self.hp = hp
        self.weakTo = weakTo
        self.immuneTo = immuneTo
        self.attackType = attackType
        self.attackDmg = attackDmg
        self.initiative = initiative
        self.resetRound()

    def target(self, other):
        self.attacking = other
        other.defendingAgainst = self
    
    def resetRound(self):
        self.attacking = None
        self.defendingAgainst = None

    def effectivePower(self): return self.attackDmg * self.qty

    def calculateDamage(self, other):
        if self.attackType in other.immuneTo: return 0
        if self.attackType in other.weakTo: return 2 * self.effectivePower()
        return self.effectivePower()

    def qualifyTarget(self, other):
        return (self.calculateDamage(other), other.effectivePower(), other.initiative)
    
    def setTarget(self, other):
        self.attacking = other
        other.defendingAgainst = self

    def attack(self):
        other = self.attacking
        damage = self.calculateDamage(other)
        other.qty -= damage // other.hp
        if other.qty < 0: other.qty = 0
        self.attacking = None
        other.defendingAgainst = None
boost = 0
while True:
    print(boost)
    groups = []
    for x in a.splitlines():
        #print(x)
        if x=="":  continue
        if ":" in x:
            army = x[:-1]
            id=1
            continue
        qty = int(x.split()[0])
        hp = int(x.split()[4])
        weakTo, immuneTo = [],[]
        if "(" in x:
            brackets = x.split("(")[1].split(")")[0]
            for y in brackets.split("; "):
                y = y.split(" to ")
                array = weakTo if y[0] == "weak" else immuneTo
                array += [x for x in y[1].split(", ")]
        attackDmg = int(x.split()[-6]) + (boost if army == "Immune System" else 0)
        attackType = x.split()[-5]
        initiative = int(x.split()[-1])
        groups.append(Group(id,army,qty,hp,weakTo,immuneTo,attackType,attackDmg,initiative))
        id+=1
        #print("army:",army,"qty:",qty,"hp:",hp,"attackType:",attackType,"attackDmg:",attackDmg,"initiative:",initiative,"weakTo",weakTo,"immuneTo:",immuneTo)
    while True:
        stalemate=[]
        [x.resetRound() for x in groups]
        #print()
        #print(set([x.army for x in groups if x.qty > 0]))
        if len(set([x.army for x in groups if x.qty > 0])) < 2: break
        groups.sort(key=lambda x: (x.effectivePower(), x.initiative), reverse=True)
        # for g in sorted(groups,key = lambda g: (g.army,g.id)):
        #     if g.qty == 0: continue
            #print(f"{g.army} group {g.id} contains {g.qty} units")
        for g1 in groups:
            if g1.qty == 0: continue
            candidates = [g2 for g2 in groups if g1.army!=g2.army and g2.qty > 0 and g2.defendingAgainst == None]
            #print(len(candidates), "candidates")
            if not candidates: continue
            #for g2 in sorted(candidates,key = lambda g2: g1.qualifyTarget(g2)):
                #print(f"{g1.army} group {g1.id} would deal defending group {g2.id} {g1.qualifyTarget(g2)}")
            target = max(candidates,key = lambda g2: g1.qualifyTarget(g2))
            if g1.calculateDamage(target) == 0: 
                stalemate.append(True)
                continue
            stalemate.append(False)
            g1.setTarget(target)
        if all(stalemate):
            print("stalemate")
            break
        groups.sort(key=lambda x: (x.initiative), reverse=True)
        for g1 in groups:
            if g1.attacking and g1.qty > 0: 
                g2 = g1.attacking
                before = g2.qty
                g1.attack()
                unitsKilled = before - g2.qty
                #print(f"{g1.army} group {g1.id} attacks defending group {g2.id} killing {unitsKilled} units")
    boost+=1
    armiesLeft = set([x.army for x in groups if x.qty > 0])
    if list(armiesLeft) == ["Immune System"]:
        print(sum(set([x.qty for x in groups]))) #part 2
        break