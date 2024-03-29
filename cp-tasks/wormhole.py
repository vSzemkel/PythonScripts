def getKey(s):
    n1,n2=map(int,s.strip().split(" "))
    return n2
fin = open('wormhole.in','r')
N = int(fin.readline().strip())

wh= [l.strip() for l in fin.readlines()]
wh.sort(key=getKey)

isLast={}
for i in range(1,N):
    p1,p2=map(int,wh[i-1].strip().split(" "))
    n1,n2=map(int,wh[i].strip().split(" "))
    if p2 != n2:
        isLast[wh[i-1]]=1
    else:
        isLast[wh[i-1]]=0
else:
    isLast[wh[-1]]=1
        
cnt=0
checks=0

def isTrapped(c,i,p,pr):
    if c>N:
        return True
    if wh[i] in p:
        i = wh.index(p[wh[i]])
    else:
        i = wh.index(pr[wh[i]])
    if isLast[wh[i]]:
        return False
    return isTrapped(c+1,i+1,p,pr)

def getPair(i,c,p):
    global cnt, checks
    if c==N//2:
        checks+=1
        for k in range(N):
            pr={v: k for k, v in p.items()}
            if isTrapped(0,k,p,pr):
                cnt+=1
                break
        return
    for j in range(i+1,N):
        isContain=False
        for e in p.items():
            if wh[i] in e or wh[j] in e:
                isContain =True
                break
        if not isContain:
            p[wh[i]]=wh[j]
            getPair(getIndex(p),c+1,p)
        
            if len(p)>0:
                del p[wh[i]]
def getIndex(p):
    for i in range(N):
        for e in p.items():
            if wh[i] in e:
                break
        else:
            return i

p={}
getPair(0,0,p)

with open('wormhole.out','w') as fout:
    fout.write(f"{cnt}\n")
print(checks)