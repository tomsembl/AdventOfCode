a="""Begin in state A.
Perform a diagnostic checksum after 12861455 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state E.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.

In state E:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state F.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""

test="""In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""

LEFTMOST = None

class Bit():
    
    def __init__(self,val=0):
        self.prev=None
        self.next=None
        self.val=val

    def move(self,dir):
        global LEFTMOST
        if dir==1:
            if not self.next:
                self.next = Bit()
                self.next.prev = self
            return self.next
        if not self.prev:
            self.prev = Bit()
            self.prev.next = self
            LEFTMOST = self.prev
        return self.prev
		

STATE = 0
NODE = Bit()
LEFTMOST = NODE
def f(v,d,s):
    global NODE, STATE
    NODE.val = v
    NODE = NODE.move(d)
    STATE = s
#0,1,2,3,4,5
#A,B,C,D,E,F
fa = lambda x: f(1,1,1) if x==0 else f(0,0,1)
fb = lambda x: f(1,0,2) if x==0 else f(0,1,4)
fc = lambda x: f(1,1,4) if x==0 else f(0,0,3)
fd = lambda x: f(1,0,0)
fe = lambda x: f(0,1,0) if x==0 else f(0,1,5)
ff = lambda x: f(1,1,4) if x==0 else f(1,1,0)

iterations = 12861455 
funcs=[fa,fb,fc,fd,fe,ff]
for i in range(iterations):
    if i%1_000_000==0:print(i)
    funcs[STATE](NODE.val)

node = LEFTMOST
total = 0
while True:
    total += node.val
    if not node.next: break
    node = node.next
print(total)
#2556 too low