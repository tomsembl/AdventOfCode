from copy import deepcopy

manas = {"Missile":53,"Drain":73,"Shield":113,"Poison":173,"Recharge":229}
effects = [x for x in manas]
durations = {"Missile":0,"Drain":0,"Shield":6,"Poison":6,"Recharge":5}
damages = {"Missile":4,"Drain":2,"Shield":0,"Poison":3,"Recharge":0}
heals = {"Missile":0,"Drain":2,"Shield":0,"Poison":0,"Recharge":0}
manaRecharges = {"Missile":0,"Drain":0,"Shield":0,"Poison":0,"Recharge":101}
armours = {"Missile":0,"Drain":0,"Shield":7,"Poison":0,"Recharge":0}
timedEffects = ["Shield","Poison","Recharge"]

def part(p):


    class GameState():
        def __init__(self):

            # self.bossHp = 14 #test
            # self.bossDmg = 8
            # self.myHp = 10
            # self.myMana = 250

            self.bossHp = 71 #prod
            self.bossDmg = 10
            self.myHp = 50
            self.myMana = 500

            self.manaSpent = 0
            self.durations = {x:0 for x in durations}

        def tick(self):
            for effect in timedEffects:
                if self.durations[effect] != 0: 
                    self.effect(effect)
                    self.durations[effect] -= 1

        def myTurn(self,effect):
            if p==2: self.myHp -= 1
            self.tick()
            self.myMana -= manas[effect]
            self.manaSpent += manas[effect]
            if effect in timedEffects:
                self.durations[effect] = durations[effect]
            else:
                self.effect(effect)

        def bossTurn(self):
            self.tick()
            if self.endCheck():
                return True
            armour = 7 if self.durations["Shield"] != 0 else 0
            self.myHp -= self.bossDmg - armour
            if self.endCheck():
                return True
            return False

        def effect(self,effect):
            self.bossHp -= damages[effect]
            self.myMana += manaRecharges[effect]
            self.myHp += heals[effect]

        def endCheck(self):
            if self.bossHp <= 0 or self.myHp <= 0: 
                return True
            return False

    queue = [GameState()]
    minMana = 2399
    while queue:
        gs = queue.pop()
        for effectCandidate in [x for x in effects if gs.durations[x]<2 and gs.myMana >= manas[x]]:
            if gs.manaSpent + manas[effectCandidate] >= minMana : 
                if effectCandidate == "Missile": 
                    break
                continue
            newGs = deepcopy(gs)
            newGs.myTurn(effectCandidate)
            isFinished = newGs.bossTurn()
            if isFinished:
                if newGs.myHp <= 0:
                    continue
                if newGs.manaSpent < minMana: 
                    minMana = newGs.manaSpent
                continue
            queue.append(newGs)
    print(minMana)

part(1)
part(2)
# effect=None
# gs.myTurn(effect)
# isFinished = gs.bossTurn()
# if isFinished:
#     pass


# effects=["Poison","Missile"]
# effects=["Recharge","Shield","Drain","Poison","Missile"]
# gs = GameState()
# for effect in effects:
#     print()
#     print(f"\n-- Player turn --\n- Player has {gs.myHp} hit points, {7 if gs.durations['Shield']!=0 else 0} armor, {gs.myMana} mana\n- Boss has {gs.bossHp} hit points")
#     gs.myTurn(effect)
#     print(gs.durations)
#     print(f"\n-- Boss turn --\n- Player has {gs.myHp} hit points, {7 if gs.durations['Shield']!=0 else 0} armor, {gs.myMana} mana\n- Boss has {gs.bossHp} hit points")
#     isFinished = gs.bossTurn()
#     print(gs.durations)
#     if isFinished:
#         print("Boss Win" if gs.myHp <= 0 else "My Win", gs.manaSpent)

# gs = GameState()
# letters = {"M":"Missile","D":"Drain","S":"Shield","P":"Poison","R":"Recharge"}
# while True:
#     print("myHp:",gs.myHp," myArmour:",gs.myArmour," myMana:",gs.myMana," bossHp:",gs.bossHp)
#     try:
#         letter = input("M D S P R: ")
#         effect = letters[letter]
#         if gs.myMana < manas[effect]: 
#             print("insufficient mana")
#             raise ValueError
#         gs.myTurn(effect)
#         isFinished = gs.bossTurn()
#         if isFinished:
#             print("Boss Win" if gs.myHp <= 0 else f"My Win {gs.manaSpent}")
#             break
#     except: pass

# for effect in manas:
#     print("\n",effect)
#     gs = GameState()
#     print("before  ","bossHp:",gs.bossHp,"myHp:",gs.myHp,"myMana:",gs.myMana,"myArmour:",gs.myArmour)
#     gs.effect(effect)
#     print("after   ","bossHp:",gs.bossHp,"myHp:",gs.myHp,"myMana:",gs.myMana,"myArmour:",gs.myArmour)


# bossHp=71
# bossDmg=10
# myHp=50
# myMana=500
#         mana duration damage heal mana armour
# Missile  53   0        4      0    0    0
# Drain    73   0        2      2    0    0
# Shield   113  6        0      0    0    7
# Poison   173  6        3      0    0    0
# Recharge 229  5        0      0    101  0

# turn = 0
# myTurn = True
# activeSpells={}
# while myHp>0 and bossHp>0:
#     if myTurn:
#         while True:
#             try:
#                 letter = input("M D S P R: ")
#                 spell = spellLetters[letter]
#                 if myMana < manas[spell]: 
#                     print("insufficient mana")
#                     raise ValueError
#                 break
#             except: pass
#         if spell == "Missile":
#     else:
#         myHp 
#     myTurn = not myTurn

#2398 too high
#1355 too low
#1824