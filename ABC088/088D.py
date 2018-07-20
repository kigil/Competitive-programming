h,w=map(int,input().split())
s=[[] for j in range(h)]
t=[[0]*w for k in range(h)]
t[0][0]=1
q=0
u=[]
for i in range(h):
    s[i]+=list(input())
    q+=s[i].count("#")
u.append((0,0))
while u!=[]:
    (x,y)=u[0]
    if x!=h-1:
        if t[x+1][y]==0 and s[x+1][y]==".":
            t[x+1][y]=t[x][y]+1
            u.append((x+1,y))
    if y!=w-1:        
        if t[x][y+1]==0 and s[x][y+1]==".":
            t[x][y+1]=t[x][y]+1
            u.append((x,y+1))
    if x!=0:        
        if t[x-1][y]==0 and s[x-1][y]==".":
            t[x-1][y]=t[x][y]+1
            u.append((x-1,y))
    if y!=0:        
        if t[x][y-1]==0 and s[x][y-1]==".":
            t[x][y-1]=t[x][y]+1
            u.append((x,y-1))
    u.pop(0)
if t[h-1][w-1]==0:
    print(-1)
else:    
    print((h*w-t[h-1][w-1])-q)    
        
        
    
    
