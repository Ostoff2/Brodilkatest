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
            
            with open(path,"w") as File:
                File.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n")

            try:
                XMapLabint=int(input("Введите высоту карты: "))
                XMapLab=str(XMapLabint)+"\n"
                YMapLabint=int(input("Введите ширину карты: "))
                YMapLab=str(YMapLabint)+"\n"
            except:
                print("Ошибка с файлом")
                os.remove(path)
                
            with open(path,"r+") as File:
                lines = File.readlines()
                lines[0]=XMapLab
                lines[1]=YMapLab
                File.seek(0,0)
                for i in range(0,11):
                    File.write(lines[i])
                    
            z3+=1
        elif NMorS==0:
            NameMap=str(input("Название сохранения: "))
            NameMap+=".txt"
            path+=NameMap
            z3+=1
        else:
            print("Попробуйте снова...")
    z4=1
    while z4==1:
        print("Выбирите действие:\n1.Изменить размер мира по X\n2.Изменить размер мира по Y\n3.Добавить выходы\n4.Убрать выходы\n5.Добавить стены\n6.Убрать стены\n7.Добавить мины\n8.Убрать мины\n9.Выбрать кол-во спаунов\n10.Добавить спаун(после выбора их кол-ва)\n11.Убрать спаун(после выбора их кол-ва)\n12.Сохранить настройки\nДругое.Выход из программы.")
        VD=int(input())
        if VD==1:
            
        elif VD==2:
            
        elif VD==3:
            
        elif VD==4:
            
        elif VD==5:
            
        elif VD==6:
            
        elif VD==7:
            
        elif VD==8:
            
        elif VD==9:
            
        elif VD==10:
            
        elif VD==11:

        elif VD==12:
            
        else:
            print("Выход из программы...")
            z4+=1
            
else:
    print("h")

'''Variables:
LINE1=XMapLab
LINE2=YMapLab
LINE3=XPoints
LINE4=YPoints
LINE5=XWalls
LINE6=YWalls
LINE7=XMines
LINE8=YMines
LINE9=XSpawns
LINE10=YSpawns
LINE11=NSpawns



x
^
|
|
L---->y
'''

