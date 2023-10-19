bossHp=71
bossDmg=10
myHp=50
myMana=500
#         mana duration damage heal mana armour
# Missile  53   0        4      0    0    0
# Drain    73   0        2      2    0    0
# Shield   113  6        0      0    0    7
# Poison   173  6        3      0    0    0
# Recharge 229  5        0      0    101  0
spellLetters={"M":"Missile","D":"Drain","S":"Shield","P":"Poison","R":"Recharge"}
manas = {"Missile":53,"Drain":73,"Shield":113,"Poison":173,"Recharge":229}
durations = {"Shield":6,"Poison":6,"Recharge":5}
damages = {"Missile":4,"Drain":2,"Poison":3}
heals = {"Drain":2}
manas = {"Recharge":101}
armours = {"Shield":7}
turn = 0
myTurn = True
activeSpells={}
while myHp>0 and bossHp>0:
    if myTurn:
        while True:
            try:
                letter = input("M D S P R: ")
                spell = spellLetters[letter]
                if myMana < manas[spell]: 
                    print("insufficient mana")
                    raise ValueError
                break
            except: pass
        if spell == "Missile":
    else:
        myHp 
    myTurn = not myTurn