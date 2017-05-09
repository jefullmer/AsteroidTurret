## space_ship_game.py
## James
## Spring 16

import pygame, sys
import datetime
from pygame.locals import *
from bulletClass import bullet
from meteorClass import meteor
from spaceSHIPclass import spaceSHIP
from vector2class import vector2
from textClass import textGraphic
from backgroundClass import background
from menuClass import menu
from dictionaryClass import dictionary
from highScoreClass import highScoreCon
from random import *

space_background = 'sprites//spaceBack.png'
space_ship_image = 'sprites//turret2.png'
menu_background = 'sprites//spaceMenu.png'
pygame.mixer.pre_init(44100, -16, 2, 1024*4)
pygame.init()
FPSCLOCK = pygame.time.Clock()
BULLETSPEED = 10
meteorLIST = pygame.sprite.Group()
bulletLIST = pygame.sprite.Group()
FPS = 120
DWIDTH = 800
DHEIGHT = 600
ssPos = [vector2(int(DWIDTH * .0833), int(DHEIGHT * .875)), vector2(int(DWIDTH * .5), int(DHEIGHT * .875)), vector2(int(DWIDTH * .9166), int(DHEIGHT * .875))]
ssSIZE = (int(DWIDTH * .125), int(DHEIGHT * .25))
bulletSIZE = 10


STARTspPOS = vector2(DWIDTH//2, DHEIGHT//2)
DISPLAYSURF = pygame.display.set_mode((DWIDTH, DHEIGHT), HWSURFACE | DOUBLEBUF)
BGimage = pygame.image.load(space_background).convert()
BGwidth, BGheight = BGimage.get_size()
BGimage = pygame.transform.scale(BGimage, (BGwidth, BGheight))

menuImage = pygame.image.load(menu_background).convert()
BGwidth, BGheight = BGimage.get_size()
BGimage = pygame.transform.scale(BGimage, (BGwidth, BGheight))
wht = (255,255,255)

arrowDown = pygame.image.load('sprites//arrow.png')
arrowDown = pygame.transform.flip(arrowDown, False, True)
highScore = highScoreCon(DISPLAYSURF)



#bg = background(DISPLAYSURF, BGimage)


explosion_sound = pygame.mixer.Sound("audio//explosion.wav")
hit_sound = pygame.mixer.Sound("audio//hit.wav")
laser_sound = pygame.mixer.Sound("audio//laserShoot.wav")
loseLife_sound = pygame.mixer.Sound("audio//loseLife.wav")
gameOver_sound = pygame.mixer.Sound("audio//gameOver.wav")
gameStart_sound = pygame.mixer.Sound("audio//gameStart.wav")


overWorld = menu(DISPLAYSURF, space_background)
overWorld.makeText([int(DWIDTH * .12), int(DHEIGHT * .0625)], 'Score: 0', [int(DWIDTH * .0125), int(DHEIGHT * .01875)], (210, 210, 210))
overWorld.makeText([int(DWIDTH * .12), int(DHEIGHT * .0625)], 'Lives: 5', [int(DWIDTH * .833), int(DHEIGHT * .01875)], (210, 210, 210))
overWorld.makeText([int(DWIDTH * .7), int(DHEIGHT * .2)], 'Wave 1', [int(DWIDTH * .155), int(DHEIGHT * .375)], (210, 210, 210))

gameOver = menu(DISPLAYSURF, menu_background)
gameOver.makeText((DWIDTH, int(DHEIGHT * .25)), 'GAME OVER!',[0,0], (255, 255, 255))
gameOver.makeText((int(DWIDTH * .625), int(DHEIGHT * .083)), 'Push enter to go to the main menu', [int(DWIDTH * .125),int(DHEIGHT * .666)], (255,255,255))
gameOver.makeText((int(DWIDTH * .625), int(DHEIGHT * .083)), 'Push escape to close the game', [int(DWIDTH * .125),int(DHEIGHT * .7416)], (255,255,255))
gameOver.makeText((int(DWIDTH * .625), int(DHEIGHT * .083)), 'You Reached Wave: 0', [int(DWIDTH * .125),int(DHEIGHT * .333)], (255,255,255))
gameOver.makeText((int(DWIDTH * .625), int(DHEIGHT * .083)), 'You Had Score: 0', [int(DWIDTH * .125),int(DHEIGHT * .425)], (255,255,255))

mainMenu = menu(DISPLAYSURF, menu_background)
mainMenu.makeText((DWIDTH, int(DHEIGHT * .25)), 'Asteroid Defence', [0,0], (255, 255, 255))
mainMenu.makeButton([int(DWIDTH * .125), int(DHEIGHT * .0833)], pygame.image.load('sprites//start.png').convert(), [int(DWIDTH * .4375), int(DHEIGHT * .40)])
mainMenu.makeButton([int(DWIDTH * .125), int(DHEIGHT * .0833)], pygame.image.load('sprites//exit.png').convert(), [int(DWIDTH * .4375), int(DHEIGHT * .70)])
mainMenu.makeButton([int(DWIDTH * .125), int(DHEIGHT * .0833)], pygame.image.load('sprites//highScoreBut.png').convert(), [int(DWIDTH * .4375), int(DHEIGHT * .51666)])



highScoreScreen = menu(DISPLAYSURF, menu_background)
highScoreScreen.makeText([800, 150], 'High Scores', [0,0], wht)
highScoreScreen.makeText([75, 50], '1)', [25, 200], wht)
highScoreScreen.makeText([75, 50], 'aaa', [125, 200], wht)
highScoreScreen.makeText([50, 50], '10', [225, 200], wht)
highScoreScreen.makeText([75, 50], '100', [325, 200], wht)
highScoreScreen.makeText([75, 50], '6/11/16', [425, 200], wht)
highScoreScreen.makeText([75, 50], '11:07', [525, 200], wht)

highScoreScreen.makeText([75, 50], '2)', [25, 250], wht)
highScoreScreen.makeText([75, 50], 'bbb', [125, 250], wht)
highScoreScreen.makeText([50, 50], '9', [225, 250], wht)
highScoreScreen.makeText([75, 50], '90', [325, 250], wht)
highScoreScreen.makeText([75, 50], '6/11/16', [425, 250], wht)
highScoreScreen.makeText([75, 50], '11:07', [525, 250], wht)

highScoreScreen.makeText([75, 50], '3)', [25, 300], wht)
highScoreScreen.makeText([75, 50], 'ccc', [125, 300], wht)
highScoreScreen.makeText([50, 50], '8', [225, 300], wht)
highScoreScreen.makeText([75, 50], '80', [325, 300], wht)
highScoreScreen.makeText([75, 50], '6/11/16', [425, 300], wht)
highScoreScreen.makeText([75, 50], '11:07', [525, 300], wht)

highScoreScreen.makeText([75, 50], '4)', [25, 350], wht)
highScoreScreen.makeText([75, 50], 'ddd', [125, 350], wht)
highScoreScreen.makeText([50, 50], '7', [225, 350], wht)
highScoreScreen.makeText([75, 50], '70', [325, 350], wht)
highScoreScreen.makeText([75, 50], '6/11/16', [425, 350], wht)
highScoreScreen.makeText([75, 50], '11:07', [525, 350], wht)

highScoreScreen.makeText([75, 50], '5)', [25, 400], wht)
highScoreScreen.makeText([75, 50], 'eee', [125, 400], wht)
highScoreScreen.makeText([50, 50], '6', [225, 400], wht)
highScoreScreen.makeText([75, 50], '60', [325, 400], wht)
highScoreScreen.makeText([75, 50], '6/11/16', [425, 400], wht)
highScoreScreen.makeText([75, 50], '11:07', [525, 400], wht)

highScoreScreen.makeButton([100, 50], pygame.image.load('sprites//spaceBackBut.png').convert(), [650, 500])



chars = dictionary()
submitScoreScreen = menu(DISPLAYSURF, menu_background)
submitScoreScreen.makeText([800, 150], 'Submit Score', [0,0], wht)
submitScoreScreen.makeText([200, 50], 'Wave: 1', [25, 150], wht)
submitScoreScreen.makeText([250, 50], 'Score: 100', [525, 150], wht)
submitScoreScreen.makeText([100, 100], 'A', [150, 325], wht)
submitScoreScreen.makeText([100, 100], 'A', [350, 325], wht)
submitScoreScreen.makeText([100, 100], 'A', [550, 325], wht)
submitScoreScreen.makeText([250, 50], '6/11/16 14:31', [250, 175], wht)
submitScoreScreen.makeText([250, 50], 'Date and Time', [250, 125], wht)

charNums = [3, 4, 5]

submitScoreScreen.makeButton([50, 50], pygame.image.load('sprites//arrow.png'), [175, 250])
submitScoreScreen.makeButton([50, 50], pygame.image.load('sprites//arrow.png'), [375, 250])
submitScoreScreen.makeButton([50, 50], pygame.image.load('sprites//arrow.png'), [575, 250])

upBut = [0, 1, 2]

submitScoreScreen.makeButton([50, 50], arrowDown, [175, 450])
submitScoreScreen.makeButton([50, 50], arrowDown, [375, 450])
submitScoreScreen.makeButton([50, 50], arrowDown, [575, 450])

downBut = [3, 4, 5]

submitScoreScreen.makeButton([100, 50], pygame.image.load('sprites//spaceSubmit.png'), [650, 500])

submitBut = 6

pauseMenu = menu(DISPLAYSURF, 'none')
pauseMenu.makeText([400, 150], 'Pause', [200, 150], wht)

def makeMeteors(metNum):
    
    meteors = metNum

    while meteors > 0:
        randx = randrange(20, DWIDTH - 40)
        randy = randrange(-1000, -100)

        if  not (randx > 0 and randx < DWIDTH and randy > 0 and randy < DHEIGHT):
            v1 = vector2(randx,randy)
            v2 = vector2.fromPoints((randx, randy), (randx, DHEIGHT))
            v2 = v2.normalizeV2()
            meteorLIST.add(meteor(v1, DISPLAYSURF, v2, 1, 40))
            meteors -= 1
def changeTurret(currentSelected, direction, ssActiveList):
    currentSelected += direction
    if currentSelected < 0:
        currentSelected = 2
    elif currentSelected > 2:
        currentSelected = 0
        
    if ssActiveList[0] == False and ssActiveList[1] == False and ssActiveList[2] == False:
        return 3
    
    if not ssActiveList[currentSelected]:
        return changeTurret(currentSelected, direction, ssActiveList)
    else:
        return currentSelected
def displayAllTurrets(SS):    
    for x in SS:
        x.displaySpaceSHIP()
        
def waveAnimate(counter, seconds, blinkCount, animating):
    counter += 1
    blinkCount += 1
    if counter >= FPS//2:
        counter = 0
        seconds += 1
    if seconds % 2 == 0:
        overWorld.textList[2].active = False
        blinkCount = 0
    if blinkCount >= FPS//4 and overWorld.textList[2].active == False:
        overWorld.textList[2].active = True
        counter = 0
    if seconds >= 6:
        animating = False
    return counter, seconds, blinkCount, animating







def gameOverScreen(waveNum, scoreNum):
    gg = True
    highScore.loadFile()
    gameOver.textList[3].changeText('You Reached Wave: ' + str(waveNum))
    gameOver.textList[4].changeText('You Had Score: ' + str(scoreNum))
    while gg == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:        
                    gg = False      
        gameOver.displayBackground()
        
        gameOver.displayScreen()
        pygame.display.update()         
    if highScore.checkNewScore(scoreNum):
        submitScoreMenu(waveNum, scoreNum)
    main()
    
def mainMenuScreen():
    mm = True
    while mm == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()  
            elif event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                if mainMenu.buttonList[0].clicked(mouseXY):
                    mm = False
                if mainMenu.buttonList[1].clicked(mouseXY):
                    pygame.quit()
                    sys.exit()            
                if mainMenu.buttonList[2].clicked(mouseXY):
                    highScoreMenu()
        mainMenu.displayBackground()
        
        mainMenu.displayScreen()
        pygame.display.update()
        
        
        
def changeHighScoreText(name, wave, score, date, time):
    ind = 0
    a = -1
    lineCheck = [[2, 8, 14, 20, 26], [3, 9, 15, 21, 27], [4, 10, 16, 22, 28], 
                 [5, 11, 17, 23, 29], [6, 12, 18, 24, 30]]
    for i in range(31):
        a += 1                
        if ((ind * 6 )+a) == lineCheck[0][ind]:
            highScoreScreen.textList[i].changeText(name[ind])
        elif ((ind * 6 )+a) == lineCheck[1][ind]:
            highScoreScreen.textList[i].changeText(str(wave[ind]))
        elif ((ind * 6 )+a) == lineCheck[2][ind]:
            highScoreScreen.textList[i].changeText(str(score[ind]))
        elif ((ind * 6 )+a) == lineCheck[3][ind]:
            highScoreScreen.textList[i].changeText(date[ind])
        elif ((ind * 6 )+a) == lineCheck[4][ind]:
            highScoreScreen.textList[i].changeText(time[ind])
        if a % 6 == 0 and a != 0:
            a = 0
            ind += 1
            if ind > 4:
                ind = 4       
        

def highScoreMenu():
    show = True
    highScore.loadFile()
    changeHighScoreText(highScore.nameList, highScore.waveList, highScore.scoreList, highScore.dateList, highScore.timeList)
    while show:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()             
            elif event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:            
                if highScoreScreen.buttonList[0].clicked(mouseXY):
                    show = False
        highScoreScreen.displayBackground()
        highScoreScreen.displayScreen()
        pygame.display.update()        

def submitScoreMenu(wave, score):
    show = True
    highScore.loadFile()
    chars.charNum = [0, 0, 0]
    chars.charList = ['A', 'A', 'A']
    submitScoreScreen.textList[charNums[0]].changeText(chars.charList[0])
    submitScoreScreen.textList[charNums[1]].changeText(chars.charList[1])
    submitScoreScreen.textList[charNums[2]].changeText(chars.charList[2])
    t = datetime.datetime.now()
    timeList = []
    for attr in [ 'month', 'day', 'year', 'hour', 'minute']:
        timeList.append(str(getattr(t, attr)))
    newTime = (timeList[3] + ':' + timeList[4])
    newDate = (timeList[0] + '/' + timeList[1] + '/' + timeList[2])
    submitScoreScreen.textList[1].changeText('Wave: ' + str(wave))
    submitScoreScreen.textList[2].changeText('Score: ' + str(score))
    submitScoreScreen.textList[6].changeText(newTime)
    while show:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()             
            elif event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                if submitScoreScreen.buttonList[upBut[0]].clicked(mouseXY):
                    chars.changeChar(0, 1)
                    submitScoreScreen.textList[charNums[0]].changeText(chars.charList[0])
                if submitScoreScreen.buttonList[upBut[1]].clicked(mouseXY):
                    chars.changeChar(1, 1)
                    submitScoreScreen.textList[charNums[1]].changeText(chars.charList[1])
                if submitScoreScreen.buttonList[upBut[2]].clicked(mouseXY):
                    chars.changeChar(2, 1)
                    submitScoreScreen.textList[charNums[2]].changeText(chars.charList[2])
                if submitScoreScreen.buttonList[downBut[0]].clicked(mouseXY):
                    chars.changeChar(0, -1)
                    submitScoreScreen.textList[charNums[0]].changeText(chars.charList[0])
                if submitScoreScreen.buttonList[downBut[1]].clicked(mouseXY):
                    chars.changeChar(1, -1)
                    submitScoreScreen.textList[charNums[1]].changeText(chars.charList[1])
                if submitScoreScreen.buttonList[downBut[2]].clicked(mouseXY):
                    chars.changeChar(2, -1)
                    submitScoreScreen.textList[charNums[2]].changeText(chars.charList[2])
                if submitScoreScreen.buttonList[submitBut].clicked(mouseXY):
                    name = (chars.charList[0] + chars.charList[1] + chars.charList[2])
                    highScore.submitNewScore(name, wave, score, newDate, newTime)
                    highScore.saveFile()
                    show = False
        submitScoreScreen.displayBackground()
        submitScoreScreen.displayScreen()
        pygame.display.update()
    main()
    

def reset():
    overWorld.textList[0].changeText('Score: 0')
    overWorld.textList[1].changeText('Lives: 5')
    overWorld.textList[2].changeText('Wave 1')
    meteorLIST.empty()
    bulletLIST.empty()

def pauseScreen():
    pause = True
    while pause == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYUP:
                if event.key == pygame.K_RETURN:
                    pause = False
        pauseMenu.displayScreen()
        pygame.display.update()

def gameLoop():
    gameStart_sound.play()

    TEMPvector = vector2.fromPoints((STARTspPOS.vX, STARTspPOS.vY), (STARTspPOS.vX + 0, STARTspPOS.vY - 10))
    TEMPvector = TEMPvector.normalizeV2()
    
    currentSelected = 1    
    
    rotationL = 0.0
    rotationR = 0.0
    spriteROT = [0.0, 0.0, 0.0]
    RATE = 1
    
    SS = [spaceSHIP(ssPos[0], ssSIZE, space_ship_image, DISPLAYSURF), 
          spaceSHIP(ssPos[1], ssSIZE, space_ship_image, DISPLAYSURF), 
          spaceSHIP(ssPos[2], ssSIZE, space_ship_image, DISPLAYSURF)]
    
    ssActiveList = [SS[0].active, SS[1].active, SS[2].active]
    
    makeMeteors(3)
    score = 0
    lives = 5
    scoreCheck = 10000
    
    wave = 1
    meteors = 5
    isAnimating = True
    isBlink = False
    animateTime = 0
    seconds = 0
    counting = 0
    playGame = True
    
    allActive = True

    while playGame:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                

                if event.key == K_d and allActive:
                    rotationR = - RATE
                elif event.key == K_a and allActive:
                    rotationL =  RATE

            elif event.type == KEYUP:
                if event.key == K_d and allActive:
                    rotationR = 0
                elif event.key == K_a and allActive:
                    rotationL = 0
                if event.key == K_LEFT and allActive:
                    currentSelected = changeTurret(currentSelected, -1, ssActiveList)
                elif event.key == K_RIGHT and allActive:
                    currentSelected = changeTurret(currentSelected, 1, ssActiveList)
                elif event.key == K_SPACE and allActive:
                    laser_sound.play()
                    bulletLIST.add(bullet(ssPos[currentSelected], DISPLAYSURF, vector1, BULLETSPEED, 30))
                if event.key == K_RETURN:
                    pauseScreen()
                    
        spriteROT[currentSelected] += rotationR + rotationL
        if spriteROT[currentSelected] >= 60:
            spriteROT[currentSelected] = 60
        if spriteROT[currentSelected] <= -60:
            spriteROT[currentSelected] = -60

        if len(meteorLIST) <= 0:
            makeMeteors(meteors)
            meteors += 2
            wave += 1
            overWorld.textList[2].changeText(('Wave ' + str(wave)))
            isAnimating = True
            counting = seconds = animateTime = 0

            
        DISPLAYSURF.fill((0,0,0))
        overWorld.displayBackground()

        bulletmeteorCollisions = pygame.sprite.groupcollide(meteorLIST, bulletLIST, True, True)
        if allActive:
            for i in SS:
                if i.active:
                    meteorSScollisions = pygame.sprite.spritecollide(i, meteorLIST, True)
                for col in meteorSScollisions:
                    i.health -= 1
                    hit_sound.play()
                    if i.health <= 0:
                        i.active = False
        
        
        if SS[0].active == False and SS[1].active == False and SS[2].active == False:
            allActive = False               
        
        if SS[currentSelected].active == False and allActive:
            currentSelected = changeTurret(currentSelected, 1, ssActiveList)
               
        
        
        for hit in bulletmeteorCollisions:
            explosion_sound.play()
            score += 100
            overWorld.textList[0].changeText(('Score: ' + str(score)))
            if score >= scoreCheck:
                lives += 1
                scoreCheck += 10000
                overWorld.textList[1].changeText(('Lives: ' + str(lives)))

        for BX in bulletLIST:
            if BX.rect.x > 0 and BX.rect.y > 0 and BX.rect.x< DWIDTH and BX.rect.y < DHEIGHT:
                BX.displayBullet()
            else:
                bulletLIST.remove(BX)
                
        for MX in meteorLIST:
            MX.displayMeteor()
            if MX.rect.top > DHEIGHT:
                lives -= 1
                loseLife_sound.play()
                meteorLIST.remove(MX)
                overWorld.textList[1].changeText(('Lives: ' + str(lives)))
                if lives <= 0:
                    playGame = False
        for i in range(len(SS)):
            SS[i].rotateSS(spriteROT[i])
            SS[i].healthColor = (100, 100, 100)
        
        if allActive:    
            SS[currentSelected].healthColor = (200, 200, 200)
        
        if isAnimating:
            counting, seconds, animateTime, isAnimating = waveAnimate(counting, seconds, animateTime, isAnimating)
        
        vector1 = TEMPvector.rotateV2(-spriteROT[currentSelected])
        displayAllTurrets(SS)
        overWorld.displayScreen()
        ssActiveList = [SS[0].active, SS[1].active, SS[2].active]
        
        FPSCLOCK.tick(FPS)

        pygame.display.update()
    reset()
    SS.clear()
    gameOver_sound.play()
    gameOverScreen(wave, score)

def main():
    mainMenuScreen()
    gameLoop()

if __name__ == '__main__': main()

