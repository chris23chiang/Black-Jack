# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:15:05 2021

@author: Chris Chiang

♠♥♦♣
print("\N{black spade suit}") #或 print(chr(9824))
print("\N{black heart suit}") #或 print(chr(9829))
print("\N{black diamond suit}") #或 print(chr(9830))
print("\N{black club suit}") #或 print(chr(9827))

"""

print("歡迎光臨江江Black Jack!")

import random

def printCard(c):
    for i in c:
        if i //13 == 0:
            print(chr(9824),end="")
        elif i//13 ==1:
            print(chr(9829),end="")
        elif i//13 ==2:
            print(chr(9830),end="")
        else:
            print(chr(9827),end="")
        if i % 13 ==0:
            print("A", end=" ")
        elif i % 13 ==10:
            print("J", end=" ")
        elif i % 13 ==11:
            print("Q", end=" ")
        elif i % 13 ==12:
            print("K", end=" ")
        else:
            print(i%13+1, end=" ")
    print()       

def printMessage():
    print ("玩家的牌: ",end="")
    printCard(playerCard)
    print ("玩家的牌面點數: ",sum(playerPoint))
    print("莊家的牌:",end="")
    printCard(bankerCard)
    print ("莊家的牌面點數: ",sum(bankerPoint))
    print ("***********************")

def cardPoint(x):
    if x % 13 ==0:
        return 11
    elif x % 13 > 9:
        return 10
    else:
        return x % 13 +1
    
def deal(gamerCard,gamerPoint):
    temp = card.pop()
    gamerCard.append(temp)
    gamerPoint.append(cardPoint(temp))

card = list(range(0,52))
random.shuffle(card)
#print (card)

playerCard=[]
playerPoint=[]
bankerCard=[]
bankerPoint=[]

for i in range(2):
    deal(playerCard, playerPoint)

deal(bankerCard,bankerPoint)

printMessage()

while True:
    ans = input("玩家要加牌嗎(Y/N)? ")
    if ans == 'N' or ans == 'n':
        break
    deal(playerCard,playerPoint)
    if sum(playerPoint) > 21:
        if 11 in playerPoint:
            playerPoint[playerPoint.index(11)]=1
            printMessage()
        else:
            printMessage()
            print ("玩家爆牌，莊家獲勝!")
            break
        
    else:
        printMessage()
        
if sum(playerPoint) < 22:
    while sum(bankerPoint) < 17:
        deal(bankerCard,bankerPoint)
        if sum(bankerPoint) > 21:
            if 11 in bankerPoint:
                bankerPoint[bankerPoint.index(11)]=1
        printMessage()
        
    if sum(bankerPoint)>21:
        print("莊家爆牌，玩家獲勝!")
    elif sum(playerPoint) > sum(bankerPoint):
        print("玩家勝利!")
    elif sum(bankerPoint) > sum(playerPoint):
        print("莊家勝利!")
    else:
        print("點數相同!和局!")





