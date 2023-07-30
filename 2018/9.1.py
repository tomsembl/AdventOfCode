players=405
last=71700*100
# players=9
# last=25


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


marble = 1
startNode = Node(0)
startNode.next = startNode
startNode.prev = startNode
node = startNode
player = 1
scores={x:0 for x in range(1,players+1)}

def endTurn():
    global player, marble
    player += 1
    if player > players: player = 1
    if marble == last: return True
    marble += 1
    return False

while True:
    if marble % 23 == 0:
        scores[player] += marble
        for _ in range(7):
            node = node.prev
        scores[player] += node.value
        node.prev.next = node.next
        node.next.prev = node.prev
        node = node.next
        if endTurn(): break
        continue

    node = node.next
    newNode = Node(marble)
    node.next.prev = newNode
    newNode.next = node.next
    node.next = newNode
    newNode.prev = node
    node = newNode

    if endTurn(): break

print(max(scores.values()))
