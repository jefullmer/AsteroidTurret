##High score Main

import pygame,sys
from pygame.locals import *

class highScoreCon(object):
    
    def __init__(self, surf):
        self.surf = surf
        self.nameList = []
        self.waveList = []
        self.scoreList = []
        self.dateList = []
        self.timeList = []        
        self.placement = 5
        
    def loadFile(self):
        objFile = open('highscore.ahs', "r")
        self.nameList = []
        self.waveList = []
        self.scoreList = []
        self.dateList = []
        self.timeList = []
        tempList = []
        
        for line in objFile:
            tempList = line.split()
            x = tempList[1]
            y = tempList[2]
            z = tempList[3]
            d = tempList[4]
            t = tempList[5]
            self.nameList.append(x)
            self.waveList.append(int(y))
            self.scoreList.append(int(z))
            self.dateList.append(d)
            self.timeList.append(t)
        objFile.close()
    
    def checkNewScore(self, score):
        self.placement = 5        
        for i in range(5):
            if score > self.scoreList[i]:
                self.placement = i
                return True
        if self.placement < 5:
            return False
    def submitNewScore(self, name, wave, score, date, time):
        self.__shiftDown()
        self.nameList[self.placement] = name
        self.waveList[self.placement] = wave
        self.scoreList[self.placement] = score
        self.dateList[self.placement] = date
        self.timeList[self.placement] = time        
    
    def __shiftDown(self):
        tempList = []
        a = 5
        for i in range(5):
            a -= 1
            if a <= self.placement:
                break
            tempList = [self.nameList[a-1], self.waveList[a-1], self.scoreList[a-1], self.dateList[a-1], self.timeList[a-1]]
            self.nameList[a] = tempList[0]
            self.waveList[a] = tempList[1]
            self.scoreList[a] = tempList[2]
            self.dateList[a] = tempList[3]
            self.timeList[a] = tempList[4]             
        pass
    
    def saveFile(self):
        stringList = []
        for i in range(5):
            stringList.append(str(i+1) + ' ' + str(self.nameList[i]) + ' ' + str(self.waveList[i]) +
                              ' ' + str(self.scoreList[i]) + ' ' + self.dateList[i] + ' ' + 
                              self.timeList[i])
        objFile = open('highscore.ahs', "w")
        print(stringList[0], file=objFile)
        print(stringList[1], file=objFile)
        print(stringList[2], file=objFile)
        print(stringList[3], file=objFile)
        print(stringList[4], file=objFile)
        objFile.close()

