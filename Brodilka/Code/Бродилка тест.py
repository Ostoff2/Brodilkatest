import random
import os
# func

# Gamemode
print("Режимы игры:  1-Поиск монеток  2-Редактор Лабиринта  3-Лабиринт")
GM=int(input("Режим: "))
#----------------------Поиск монеток---------------------------------
if GM == 1:
    z2=1
    while z2==1:
        print("Напомнить управление? y/n")
        RulsMon=str(input())
        
        if RulsMon == "y":
            print("w - Вверх, s - Вниз, a - Влево, d - Вправо, Другое - Остановка")
            print("Загрузка...")
            z2+=1
        elif RulsMon == "n":
            print("Загрузка...")
            z2+=1
        else:
            print("Попробуйте ещё раз...")

    XP=0
    XMapMon=int(input("Высота поля - "))
    YMapMon=int(input("Ширина поля - "))
    N=int(input("Кол-во монеток на карте - "))
    
    PLPosXY=[0]*2
    PointsX=[]
    PointsY=[]
    
    for i in range(0,N):
        a=random.randint(0,XMapMon)
        PointsX.append(a)
        
    for i in range(0,N):
        b=random.randint(0,YMapMon)
        PointsY.append(b)
        
    print(PointsX,PointsY,end=' ')

    z=1
    while z==1:
        z1=1
        while z1==1:
            print("Текущие координаты: X-",PLPosXY[0]," Y-",PLPosXY[1])
            print("Твоя экспа - ",XP,"XP")
            H=str(input("Ход: "))
            if H=="w":
                PLPosXY[0]+=1
                if PLPosXY[0]>XMapMon:
                    print("Переход...")
                    PLPosXY[0]=0
                for i in range(0,N):
                    if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                        XP+=1
                        PointsX[i]=XMapMon+10
                        PointsY[i]=YMapMon+10
                        
            elif H=="s":
                PLPosXY[0]-=1
                if PLPosXY[0]<0:
                    print("Переход...")
                    PLPosXY[0]=XMapMon
                for i in range(0,N):
                    if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                        XP+=1
                        PointsX[i]=XMapMon+10
                        PointsY[i]=YMapMon+10
                        
            elif H=="a":
                PLPosXY[1]-=1
                if PLPosXY[1]<0:
                    print("Переход...")
                    PLPosXY[1]=YMapMon
                for i in range(0,N):
                    if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                        XP+=1
                        PointsX[i]=XMapMon+10
                        PointsY[i]=YMapMon+10
                        
            elif H=="d":
                PLPosXY[1]+=1
                if PLPosXY[1]>YMapMon:
                    print("Переход...")
                    PLPosXY[1]=0
                for i in range(0,N):
                    if PLPosXY[0]==PointsX[i] and PLPosXY[1]==PointsY[i]:
                        XP+=1
                        PointsX[i]=XMapMon+10
                        PointsY[i]=YMapMon+10
            else:
                z+=1
                z1+=1
            if XP==N:
                print("Набрано максимальное кол-во монет - ",XP)
                z+=1
                z1+=1
                z2+=1
#----------------------Labirinth Redactor-----------------------------
elif GM == 2:
    z3=1
    while z3==1:
        path="../SavesRedactor/"
        print("Начать новую карту(1) / Загрузить сохранение(0)")
        NMorS=int(input())
        if NMorS==1:
            
            NameMap=str(input("Название новой карты: "))
            NameMap+=".txt"
            path+=NameMap
            
            File=open(path,"")
            File.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
            File.close()
            
            XMapLab=int(input("Введите высоту карты"))
            YMapLab=int(input("Введите ширину карты"))

            try:
                with open(path,"r+") as File:
                    
            except:
                print("Произошла ошибка с файлом")
            z3+=1
        elif NMorS==0:
            NameMap=str(input("Название сохранения: "))
            NameMap+=".txt"
            path+=NameMap
            z3+=1
        else:
            print("Попробуйте снова...")
   
else:
    print("h")

'''Variables:
LINE1=XMapLab         x
LINE2=YMapLab         ^
LINE3=XPoints         |
LINE4=YPoints         |
LINE5=PlPosX          L---->y
LINE6=PlPosY
LINE7=XWalls
LINE8=YWalls
LINE9=XMines
LINE10=YMines
LINE11=XSpawns
LINE12=YSpawns
LINE13=NSpawns
'''





