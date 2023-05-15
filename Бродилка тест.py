import random
XP=0
X=int(input("X - "))
Y=int(input("Y - "))
N=int(input("N XP - "))
PLPosXY=[0]*2
PointsX=[]
PointsY=[]
for i in range(0,N):
    a=random.randint(0,X)
    PointsX.append(a)
for i in range(0,N):
    b=random.randint(0,X)
    PointsY.append(b)
print(PointsX,PointsY,end=' ')

z=1
while z==1:
    z1=1
    while z1==1:
        print("Текущие координаты: X-",PLPosXY[0]," Y-",PLPosXY[1])
        print("Твоя экспа - ",XP,"XP")
        H=int(input("Ход: "))
        if H==8:
            PLPosXY[0]+=1
            if PLPosXY[0]>X:
                print("Переход...")
                PLPosXY[0]=0
            for i in range(0,N):
                if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                    XP+=1
                    PointsX[i]=X+10
                    PointsY[i]=Y+10
        elif H==5:
            PLPosXY[0]-=1
            if PLPosXY[0]<0:
                print("Переход...")
                PLPosXY[0]=X
            for i in range(0,N):
                if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                    XP+=1
                    PointsX[i]=X+10
                    PointsY[i]=Y+10
        elif H==4:
            PLPosXY[1]-=1
            if PLPosXY[1]<0:
                print("Переход...")
                PLPosXY[1]=Y
            for i in range(0,N):
                if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                    XP+=1
                    PointsX[i]=X+10
                    PointsY[i]=Y+10
        elif H==6:
            PLPosXY[1]+=1
            if PLPosXY[1]>Y:
                print("Переход...")
                PLPosXY[1]=0
            for i in range(0,N):
                if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                    XP+=1
                    PointsX[i]=X+10
                    PointsY[i]=Y+10
        else:
            z+=1
            z1+=1
print(XP)
