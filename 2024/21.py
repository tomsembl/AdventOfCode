aa="""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
    
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
a="""129A
176A
985A
170A
528A"""
test="""029A
980A
179A
456A
379A"""

#a=test
b=[x for x in a.splitlines()]
buttonDirs=["^",">","v","<"]
dirs=[(0,-1),(1,0),(0,1),(-1,0)]

class Keypad():
    def __init__(self):
        self.buttons = {}
        self.buttonPaths = {}
        self.cache = {}
    
    def getPaths(self):
        buttonPaths = {}
        for startButton in self.buttons:
            for targetButton in self.buttons:
                key = (startButton, targetButton)
                if startButton == targetButton:
                    continue
                queue = [(startButton, [])]
                while queue:
                    currentButton, path = queue.pop(0)
                    if currentButton == targetButton:
                        buttonPaths[key] = path
                        break
                    for i, neighbour in enumerate(self.buttons[currentButton].neighbours):
                        if neighbour is not None and neighbour not in path:
                            queue.append((neighbour, path + [i]))
        #removing invalid paths
        for key in buttonPaths:
            startButton, targetButton = key
            path = buttonPaths[key]
            path.sort(key=lambda x:{"<":0,"^":1,"v":2,">":3}[buttonDirs[x]])
            paths = [path, path[::-1]]
            
            for path in paths:
                isValid = True
                currentButton = startButton
                for i in range(len(path)):
                    currentButton = self.buttons[currentButton].neighbours[path[i]]
                    if currentButton is None:
                        isValid = False
                        break
                if isValid:
                    if key not in self.buttonPaths:
                        self.buttonPaths[key] = path
    
    def typeCode(self, code):
        currentButton = "A"
        result = []
        for nextButton in code:
            string = ""
            key = (currentButton, nextButton)
            if key in self.buttonPaths:
                path = self.buttonPaths[key]
                for i in path:
                    currentButton = self.buttons[currentButton].neighbours[i]
                    string += buttonDirs[i]
                string += "A"
            else:
                string += "A"
            result.append(string)
                
        return result
                    

class NumericKeyPad(Keypad):
    def __init__(self):
        self.buttons = {
            '1': Button('1', '4', None, None, '2'),
            '2': Button('2', '5', '0', '1', '3'),
            '3': Button('3', '6', 'A', '2', None),
            '4': Button('4', '7', '1', None, '5'),
            '5': Button('5', '8', '2', '4', '6'),
            '6': Button('6', '9', '3', '5', None),
            '7': Button('7', None, '4', None, '8'),
            '8': Button('8', None, '5', '7', '9'),
            '9': Button('9', None, '6', '8', None),
            '0': Button('0', '2', None, None, 'A'),
            'A': Button('A', '3', None, '0', None),
        }
        self.buttonPaths = {}
    
    
        
class Button():
    def __init__(self, key, up, down, left, right):
        self.key = key
        self.neighbours = [up, right, down, left]

class DirectionalKeypad(Keypad):
    def __init__(self):
        self.buttons = {
            '<': Button('<', None, None, None, 'v'),
            '>': Button('>', 'A', None, 'v', None),
            'v': Button('v', '^', None, '<', '>'),
            '^': Button('^', None, 'v', None, 'A'),
            'A': Button('A', None, '>', '^', None),
        }
        self.buttonPaths = {}

directionalKeypad = DirectionalKeypad()
directionalKeypad.getPaths()
    
numericKeyPad = NumericKeyPad()
numericKeyPad.getPaths()

total = 0
for code in b:
    directionalKeypadStr = "".join(numericKeyPad.typeCode(code))
    for i in range(2):
        result = directionalKeypad.typeCode(directionalKeypadStr)
        directionalKeypadStr = "".join(result)
    leng = len(directionalKeypadStr)
    num = int(code[:-1])
    total += num * leng
print(total)#p1

conversion = {}
for x in directionalKeypad.buttonPaths:
    conversion[x] = "".join([buttonDirs[y] for y in directionalKeypad.buttonPaths[x]]+["A"])
for x,y in directionalKeypad.buttonPaths:
    conversion[(x,x)] = "A"
  
targetLevelsDeep = 25
import functools
@functools.cache
def recurse(string,levelsDeep):
    if levelsDeep == targetLevelsDeep:
        return len(string)
    string = "A" + string
    return sum(recurse(conversion[(string[j],string[j+1])],levelsDeep+1) for j in range(len(string)-1))

total = 0
for code in b:
    directionalKeypadStr = "".join(numericKeyPad.typeCode(code))
    leng = recurse(directionalKeypadStr,0)
    num = int(code[:-1])
    total += num * leng
print(total)#p2
#190482536461218 too high
#167538833832712
    
    
