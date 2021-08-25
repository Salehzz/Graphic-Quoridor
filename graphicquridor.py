from graphics import *
win=""
class players(object):
    def __init__(self ,color ,xstart , ystart):
        self.player = Circle(Point(xstart, ystart),12)
        self.player.setFill(color)
    def move(self , k):
        if(k == 'Up' or k=="w"):self.player.move(0,-50)
        elif (k == 'Down' or k=="s"):self.player.move(0,50)
        elif(k=='Left' or k=="a"):self.player.move(-50,0)
        elif(k=='Right' or k=="d"):self.player.move(50,0)
def Quoridor(player_numbers,player):
    a=[[0 for i in range(17)] for j in range(17)]
    if(player_numbers==4):i=[0]*4;j=[0]*4;s=[10]*4
    if(player_numbers==2):i=[0]*2;j=[0]*2;s=[10]*2
    a[0][8]=1
    i[0]=0;j[0]=8
    a[16][8]=2
    i[1]=16;j[1]=8
    if(player_numbers==4):
    	a[8][0]=3;a[8][16]=4
    	i[2]=8;j[2]=0
    	i[3]=8;j[3]=16
    p=0;t=0
    show(a)
    while(1):
        if(s[t]>0):
            q=Text(Point(218,30),"player %d \nenter w for wall or m for move"%(t+1)).draw(win)
            while(1):
                n=win.getKey()
                if(n=='w' or n=='m'):break
            q.undraw()
            if(n=='w'):s[t]-=1;chob(a,i,j,player_numbers)
            elif(n=='m'):p,i[t],j[t]=move(a,i[t],j[t],t+1,player)
        else:
            q=Text(Point(218,44),"player %d \nyou have to move"%(t+1)).draw(win)
            p,i[t],j[t]=move(a,i[t],j[t],t+1)
        q.undraw()
        if(p):break
        t+=1;t=t%(player_numbers)
def chob(a,p,m,t):
    i=0
    z=Text(Point(218,30),"press where you want to add a wall").draw(win)
    while(i!=1):
        while(1):
            k=win.getMouse()
            if(k.getX()-(k.getX()//50)*50>35 and k.getY()-70-((k.getY()-70)//50)*50<35 and k.getX()<400 and 70<k.getY()<456):
                j="a";b=int(((k.getY()-70)//50)*2)+1;c=int((k.getX()//50)*2)+1;break
            elif(k.getX()-(k.getX()//50)*50<35 and k.getY()-70-((k.getY()-70)//50)*50>35 and k.getX()<386 and 70<k.getY()<470):
                j="o";b=int(((k.getY()-70)//50)*2)+1;c=int((k.getX()//50)*2)+1;break
        if(j=='o' and 1<=b<=15 and 1<=c<=15 and a[b][c-1]==0 and a[b][c]==0 and a[b][c+1]==0):
            a[b][c-1]='-';a[b][c]='-';a[b][c+1]='-'
            for u in range(t):
                g=[[1 for o in range(17)] for j in range(17)]
                if(dfs(a,p[u],m[u],u+1,g)!=1):break
            else:
                i=1
                x=Line(Point((k.getX()//50)*50,((k.getY()-70)//50)*50+113),Point((k.getX()//50)*50+86,((k.getY()-70)//50)*50+113))
                x.setFill("brown");x.setWidth(10);x.draw(win)
            if(i==0):a[b][c-1]=0;a[b][c]=0;a[b][c+1]=0
        elif(j=='a' and 1<=b<=15 and 1<=c<=15 and a[b-1][c]==0 and a[b][c]==0 and a[b+1][c]==0):
            a[b-1][c]='|';a[b][c]='|';a[b+1][c]='|'
            for u in range(t):
                g=[[1 for o in range(17)] for j in range(17)]
                if(dfs(a,p[u],m[u],u+1,g)!=1):break
            else:
                i=1
                x=Line(Point((k.getX()//50)*50+43,(k.getY()//50)*50+20),Point((k.getX()//50)*50+43,(k.getY()//50)*50+106))
                x.setFill("brown");x.setWidth(10);x.draw(win)
            if(i==0):a[b-1][c]=0;a[b][c]=0;a[b+1][c]=0
    z.undraw()
def move(a,i1,j1,t,player):
    i=0
    q=Text(Point(218,17),"w(up) or a(left) or s(down) or d(right)").draw(win)
    while(i!=1):
        d=win.getKey()
        if((d=='s' or d=='Down')and 0<=i1<=14 and 0<=j1<=16 and a[i1+1][j1]!='-' and a[i1+2][j1]==0):a[i1][j1]=0;i1+=2;a[i1][j1]=t;i=1;player[t-1].move("s")
        elif((d=='s' or d=='Down') and 0<=i1<=12 and 0<=j1<=16 and a[i1+1][j1]!='-' and a[i1+2][j1]!=0 and a[i1+3][j1]!='-'and a[i1+4][j1]==0):a[i1][j1]=0;i1+=4;a[i1][j1]=t;i=1;player[t-1].move("s");player[t-1].move("s")
        elif((d=='s' or d=='Down') and 0<=i1<=14 and 2<=j1<=14 and a[i1+1][j1]!='-' and a[i1+2][j1]!=0 and a[i1+3][j1]=='-'):
            z=Text(Point(218,45),"a(left) or d(right)").draw(win)
            k=win.getKey()
            z.undraw()
            if((k=='a' or k=='Left') and a[i1+2][j1-1]!='|'):a[i1][j1]=0;i1+=2;j1-=2;a[i1][j1]=t;i=1;player[t-1].move("s");player[t-1].move("a")
            if((k=='d' or k=='Right') and a[i1+2][j1+1]!='|'):a[i1][j1]=0;i1+=2;j1+=2;a[i1][j1]=t;i=1;player[t-1].move("s");player[t-1].move("d")
        if((d=='a' or d=='Left')and 0<=i1<=16 and 2<=j1<=16 and a[i1][j1-1]!='|' and a[i1][j1-2]==0):a[i1][j1]=0;j1-=2;a[i1][j1]=t;i=1;player[t-1].move("a")
        elif((d=='a' or d=='Left') and 0<=i1<=16 and 4<=j1<=16 and a[i1][j1-1]!='|' and a[i1][j1-2]!=0 and a[i1][j1-3]!='|' and a[i1][j1-4]==0):a[i1][j1]=0;j1-=4;a[i1][j1]=t;i=1;player[t-1].move("a");player[t-1].move("a")
        elif((d=='a' or d=='Left') and 2<=i1<=14 and 2<=j1<=16 and a[i1][j1-1]!='|' and a[i1][j1-2]!=0 and a[i1][j1-3]=='|'):
            z=Text(Point(218,45),"w(up) or s(down)").draw(win)
            k=win.getKey()
            z.undraw()
            if((k=='w' or k=='Up') and a[i1-1][j1-2]!='-'):a[i1][j1]=0;i1-=2;j1-=2;a[i1][j1]=t;i=1;player[t-1].move("a");player[t-1].move("w")
            if((k=='s' or k=='Down') and a[i1+1][j1-2]!='-'):a[i1][j1]=0;i1+=2;j1-=2;a[i1][j1]=t;i=1;player[t-1].move("a");player[t-1].move("s")
        if((d=='w' or d=='Up') and 2<=i1<=16 and 0<=j1<=16 and a[i1-1][j1]!='-' and a[i1-2][j1]==0):a[i1][j1]=0;i1-=2;a[i1][j1]=t;i=1;player[t-1].move("w")
        elif((d=='w' or d=='Up') and 4<=i1<=16 and 0<=j1<=16 and a[i1-1][j1]!='-' and a[i1-2][j1]!=0 and a[i1-3][j1]!='-' and a[i1-4][j1]==0):a[i1][j1]=0;i1-=4;a[i1][j1]=t;i=1;player[t-1].move("w");player[t-1].move("w")
        elif((d=='w' or d=='Up') and 2<=i1<=16 and 2<=j1<=14 and a[i1-1][j1]!='-' and a[i1-2][j1]!=0 and a[i1-3][j1]=='-'):
            z=Text(Point(218,45),"a(left) or d(right)").draw(win)
            k=win.getKey()
            z.undraw()
            if((k=='a' or k=='Left') and a[i1-2][j1-1]!='|'):a[i1][j1]=0;i1-=2;j1-=2;a[i1][j1]=t;i=1;player[t-1].move("w");player[t-1].move("a")
            if((k=='d' or k=='Right') and a[i1-2][j1+1]!='|'):a[i1][j1]=0;i1-=2;j1+=2;a[i1][j1]=t;i=1;player[t-1].move("w");player[t-1].move("d")
        if((d=='d' or d=='Right') and 0<=i1<=16 and 0<=j1<=14 and a[i1][j1+1]!='|' and a[i1][j1+2]==0):a[i1][j1]=0;j1+=2;a[i1][j1]=t;i=1;player[t-1].move("d")
        elif((d=='d' or d=='Right') and 0<=i1<=16 and 0<=j1<=12 and a[i1][j1+1]!='|' and a[i1][j1+2]!=0 and a[i1][j1+3]!='|' and a[i1][j1+4]==0):a[i1][j1]=0;j1+=4;a[i1][j1]=t;i=1;player[t-1].move("d");player[t-1].move("d")
        elif((d=='d' or d=='Right') and 2<=i1<=14 and 0<=j1<=14 and a[i1][j1+1]!='|' and a[i1][j1+2]!=0 and a[i1][j1+3]=='|'):
            z=Text(Point(218,45),"w(up) or s(down)").draw(win)
            k=win.getKey()
            z.undraw()
            if((k=='w' or k=='Up') and a[i1-1][j1+2]!='-'):a[i1][j1]=0;i1-=2;j1+=2;a[i1][j1]=t;i=1;player[t-1].move("d");player[t-1].move("w")
            if((k=='s' or k=='Down') and a[i1+1][j1+2]!='-'):a[i1][j1]=0;i1+=2;j1+=2;a[i1][j1]=t;i=1;player[t-1].move("d");player[t-1].move("s")
    q.undraw()
    return(winnerq(a),i1,j1)
def show(a):
    for i in range(9):
        for j in range(9):
            Rectangle(Point(50*i,50*j+70),Point(50*i+36,50*j+106)).draw(win)
def dfs(a,i,j,t,b):
    if(i==16 and t==1):return(1)
    if(i==0 and t==2):return(1)
    if(j==16 and t==3):return(1)
    if(j==0 and t==4):return(1)
    if(j>=2 and a[i][j-1]!="|" and b[i][j-2]==1):
        b[i][j-2]=0;k=dfs(a,i,j-2,t,b)
        if(k==1):return(1)
    if(j<=14 and a[i][j+1]!="|" and b[i][j+2]==1):
        b[i][j+2]=0;k=dfs(a,i,j+2,t,b)
        if(k==1):return(1)
    if(i>=2 and a[i-1][j]!="-" and b[i-2][j]==1):
        b[i-2][j]=0;k=dfs(a,i-2,j,t,b)
        if(k==1):return(1)
    if(i<=14 and a[i+1][j]!="-" and b[i+2][j]==1):
        b[i+2][j]=0;k=dfs(a,i+2,j,t,b)
        if(k==1):return(1)
def winnerq(a):
    for j in a[0]:
        if(j==2):
            print("player 2 win")
            return 1
    for j in a[16]:
        if(j==1):
            print("player 1 win")
            return 1
    for j in a:
        if(j[0]==4):
            print("player 4 win")
            return 1
    for j in a:
        if(j[-1]==3):
            print("player 3 win")
            return 1
    return 0
def main():
	global win
	player_numbers=int(input("enter the number of players"))
	win = GraphWin("My Game",437,507)
	win.setBackground("white")
	player1 = players("red",218,88)
	player2 = players("blue",218,488)
	if(player_numbers==4):player3 = players("yellow",18,288);player4 = players("green",418,288)
	player1.player.draw(win)
	player2.player.draw(win)
	if(player_numbers==4):
		player3.player.draw(win)
		player4.player.draw(win)
	if(player_numbers==4):player=[player1,player2,player3,player4]
	else:player=[player1,player2]
	Quoridor(player_numbers,player)
main()
