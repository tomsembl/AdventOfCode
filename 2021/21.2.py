#part 2
goal=21
p1,p2=[8,5]
#p1,p2=[4,8]
p1-=1
p2-=1
dic={}
def recurse(p1,p2,s1,s2):
    if s1 >= goal: return [1,0]
    if s2 >= goal: return [0,1]
    if (p1,p2,s1,s2) in dic: return dic[(p1,p2,s1,s2)]
    answer=[0,0]
    d=[1,2,3]
    for x in [x+y+z for x in d for y in d for z in d]:
        newP1=(p1+x)%10
        newS1=s1+newP1+1
        x1,y1=recurse(p2,newP1,s2,newS1)
        answer=[answer[0]+y1,answer[1]+x1]
    dic[(p1,p2,s1,s2)]=answer
    return answer
print(recurse(p1,p2,0,0))
