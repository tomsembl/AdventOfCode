a="""Step X must be finished before step M can begin.
Step A must be finished before step R can begin.
Step C must be finished before step K can begin.
Step H must be finished before step G can begin.
Step R must be finished before step Z can begin.
Step S must be finished before step K can begin.
Step K must be finished before step G can begin.
Step O must be finished before step Z can begin.
Step Q must be finished before step G can begin.
Step E must be finished before step Y can begin.
Step U must be finished before step I can begin.
Step G must be finished before step N can begin.
Step M must be finished before step P can begin.
Step Y must be finished before step I can begin.
Step I must be finished before step V can begin.
Step Z must be finished before step B can begin.
Step W must be finished before step V can begin.
Step D must be finished before step P can begin.
Step L must be finished before step J can begin.
Step N must be finished before step T can begin.
Step T must be finished before step P can begin.
Step B must be finished before step F can begin.
Step F must be finished before step P can begin.
Step J must be finished before step V can begin.
Step V must be finished before step P can begin.
Step Z must be finished before step F can begin.
Step B must be finished before step J can begin.
Step B must be finished before step P can begin.
Step X must be finished before step F can begin.
Step Y must be finished before step N can begin.
Step W must be finished before step D can begin.
Step G must be finished before step B can begin.
Step L must be finished before step V can begin.
Step K must be finished before step L can begin.
Step W must be finished before step P can begin.
Step E must be finished before step F can begin.
Step Y must be finished before step J can begin.
Step J must be finished before step P can begin.
Step A must be finished before step O can begin.
Step O must be finished before step E can begin.
Step T must be finished before step V can begin.
Step S must be finished before step E can begin.
Step I must be finished before step L can begin.
Step E must be finished before step B can begin.
Step G must be finished before step J can begin.
Step Z must be finished before step J can begin.
Step K must be finished before step T can begin.
Step L must be finished before step F can begin.
Step X must be finished before step S can begin.
Step U must be finished before step G can begin.
Step K must be finished before step N can begin.
Step Q must be finished before step W can begin.
Step H must be finished before step F can begin.
Step O must be finished before step P can begin.
Step M must be finished before step D can begin.
Step T must be finished before step J can begin.
Step G must be finished before step T can begin.
Step N must be finished before step P can begin.
Step O must be finished before step V can begin.
Step Q must be finished before step I can begin.
Step Z must be finished before step T can begin.
Step C must be finished before step J can begin.
Step D must be finished before step J can begin.
Step G must be finished before step W can begin.
Step U must be finished before step L can begin.
Step R must be finished before step B can begin.
Step H must be finished before step K can begin.
Step X must be finished before step I can begin.
Step X must be finished before step B can begin.
Step I must be finished before step P can begin.
Step L must be finished before step N can begin.
Step O must be finished before step Y can begin.
Step F must be finished before step J can begin.
Step E must be finished before step I can begin.
Step G must be finished before step M can begin.
Step Q must be finished before step E can begin.
Step D must be finished before step F can begin.
Step A must be finished before step Z can begin.
Step I must be finished before step D can begin.
Step B must be finished before step V can begin.
Step U must be finished before step J can begin.
Step Y must be finished before step T can begin.
Step O must be finished before step M can begin.
Step M must be finished before step B can begin.
Step M must be finished before step L can begin.
Step N must be finished before step B can begin.
Step X must be finished before step U can begin.
Step E must be finished before step Z can begin.
Step Z must be finished before step L can begin.
Step R must be finished before step E can begin.
Step M must be finished before step I can begin.
Step H must be finished before step N can begin.
Step X must be finished before step J can begin.
Step C must be finished before step S can begin.
Step R must be finished before step I can begin.
Step E must be finished before step D can begin.
Step Y must be finished before step L can begin.
Step S must be finished before step D can begin.
Step U must be finished before step Z can begin.
Step A must be finished before step C can begin.
Step Y must be finished before step W can begin."""
test="""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
#a=test
# for x in a.splitlines(): print(x)
#(y[1],y[7])
b=[[x.split(" ")[1],x.split(" ")[7]] for x in a.splitlines()]
tree={}
prerequisites={}
for x,y in b: 
    # print(x,y)
    if x not in tree: tree[x]=[]
    tree[x].append(y)
    if y not in prerequisites: prerequisites[y]=[]
    prerequisites[y].append(x)
# for x in tree: print(x,tree[x])
# print("________________________________________")
# for x in prerequisites: print(x,prerequisites[x])
# print("________________________________________")
completed = []

end = [letter for letter in prerequisites if letter not in tree][0]
stack = set([letter for letter in tree if letter not in prerequisites])
current = sorted(list(stack))[0]
while True:
    completed.append(current)
    if current == end: break
    for x in tree[current]: 
        if x not in completed: stack.add(x)
    stack.remove(current)
    for candidate in sorted(list(stack)):
        if candidate not in prerequisites or all([prereq in completed for prereq in prerequisites[candidate]]):
            current = candidate
            #print(candidate)
            #if candidate in prerequisites: print(prerequisites[candidate])
            break

print("".join(completed)) #part 1

numWorkers = 5
ordNum = ord("A") - 61
if a==test: 
    ordNum = ord("A") - 1
    numWorkers = 2

completed = []
workers = {}
end = [letter for letter in prerequisites if letter not in tree][0]
stack = set([letter for letter in tree if letter not in prerequisites])
seconds=0
while True:
    for candidate in sorted(list(stack)):
        if len(workers)>=numWorkers: break
        if candidate not in prerequisites or all([prereq in completed for prereq in prerequisites[candidate]]):
            if candidate not in workers:
                time = ord(candidate) - ordNum
                workers[candidate] = time
                stack.remove(candidate)
                
    seconds+=1
    for worker in list(workers.keys()):
        workers[worker] -= 1
        if workers[worker] == 0:
            workers.pop(worker)
            completed.append(worker)
            if worker in tree:
                for x in tree[worker]: 
                    if x not in completed and x not in workers: 
                        stack.add(x)

    if len(workers)==0 and end in completed: break
    
print(seconds) #part 2