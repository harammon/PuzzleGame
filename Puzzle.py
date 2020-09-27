from bangtal import *
from random import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)


scene1 = Scene('', 'Images/원본.jpg')
scene2 = Scene('', 'Images/배경.jpg')

timer = Timer(0.5)
showTimer(timer)

A = [50, 200, 350, 500]
B = [96, 246, 396, 546]


P1_1 = Object('Images/잘린파트_001.png')
P1_1.x = A[0]
P1_1.y = B[3]
P1_1.locate(scene1, A[0], B[3])
P1_1.show()

P1_2 = Object('Images/잘린파트_002.png')
P1_2.x = A[1]
P1_2.y = B[3]
P1_2.locate(scene1, A[1], B[3])
P1_2.show()

P1_3 = Object('Images/잘린파트_003.png')
P1_3.x = A[2]
P1_3.y = B[3]
P1_3.locate(scene1, A[2],B[3])
P1_3.show()

P1_4 = Object('Images/잘린파트_004.png')
P1_4.x = A[3]
P1_4.y = B[3]
P1_4.locate(scene1, P1_4.x, P1_4.y)
P1_4.show()

P1_5 = Object('Images/잘린파트_005.png')
P1_5.x = A[0]
P1_5.y = B[2]
P1_5.locate(scene1, A[0], B[2])
P1_5.show()

P1_6 = Object('Images/잘린파트_006.png')
P1_6.x = A[1]
P1_6.y = B[2]
P1_6.locate(scene1, A[1], B[2])
P1_6.show()

P1_7 = Object('Images/잘린파트_007.png')
P1_7.x = A[2]
P1_7.y = B[2]
P1_7.locate(scene1, A[2], B[2])
P1_7.show()

P1_8 = Object('Images/잘린파트_008.png')
P1_8.x = A[3]
P1_8.y = B[2]
P1_8.locate(scene1, A[3], B[2])
P1_8.show()

P1_9 = Object('Images/잘린파트_009.png')
P1_9.x = A[0]
P1_9.y = B[1]
P1_9.locate(scene1, A[0], B[1])
P1_9.show()

P1_10 = Object('Images/잘린파트_010.png')
P1_10.x = A[1]
P1_10.y = B[1]
P1_10.locate(scene1, A[1], B[1])
P1_10.show()

P1_11 = Object('Images/잘린파트_011.png')
P1_11.x = A[2]
P1_11.y = B[1]
P1_11.locate(scene1, A[2], B[1])
P1_11.show()

P1_12 = Object('Images/잘린파트_012.png')
P1_12.x = A[3]
P1_12.y = B[1]
P1_12.locate(scene1, A[3], B[1])
P1_12.show()

P1_13 = Object('Images/잘린파트_013.png')
P1_2.x = A[0]
P1_2.y = B[3]
P1_13.locate(scene1, A[0], B[0])
P1_13.show()

P1_14 = Object('Images/잘린파트_014.png')
P1_14.locate(scene1, A[1], B[0])
P1_14.show()

P1_15 = Object('Images/잘린파트_015.png')
P1_15.locate(scene1, A[2], B[0])
P1_15.show()

P1_16 = Object('Images/잘린파트_016.png')
P1_16.locate(scene1, A[3], B[0])
P1_16.show()
        

class Block:
    def __init__(self, cx, cy, ex, ey):
        self.emptyX = ex
        self.emptyY = ey
        self.changeX = cx
        self.chagneY = cy

    def left_checkin(self, cx, cy):       # x는 바꿀 블록
        return cx == self.emptyX - 150 and cy == self.emptyY
    def right_checkin(self, cx, cy):
        return cx == self.emptyX + 150 and cy == self.emptyY
    def up_checkin(self, cx, cy):
        return cy == self.emptyY + 150 and cx == self.emptyX
    def down_checkin(self, cx, cy):
        return cy == self.emptyY - 150 and cx == self.emptyX

    def lr_change(self):
        cx, self.emptyX = self.emptyX, cx
        P1_4.locate(scene1, self.emptyX, self.emptyY)
    def ud_change(self):
        cy, self.emptyY = self.emptyY, cy
        P1_4.locate(scene1, self.emptyX, self.emptyY)


Blocks = [
Block(A[0], B[3], P1_4.x, P1_4.y),
Block(A[1], B[3], P1_4.x, P1_4.y),
Block(A[2], B[3], P1_4.x, P1_4.y),
Block(A[3], B[3], P1_4.x, P1_4.y),
Block(A[0], B[2], P1_4.x, P1_4.y),
Block(A[1], B[2], P1_4.x, P1_4.y),
Block(A[2], B[2], P1_4.x, P1_4.y),
Block(A[3], B[2], P1_4.x, P1_4.y),
Block(A[0], B[1], P1_4.x, P1_4.y),
Block(A[1], B[1], P1_4.x, P1_4.y),
Block(A[2], B[1], P1_4.x, P1_4.y),
Block(A[3], B[1], P1_4.x, P1_4.y),
Block(A[0], B[0], P1_4.x, P1_4.y),
Block(A[1], B[0], P1_4.x, P1_4.y),
Block(A[2], B[0], P1_4.x, P1_4.y),
Block(A[3], B[0], P1_4.x, P1_4.y),
]

presentX = 3
presentY = 3
Blocknum = 3

Start = Object('Images/start.png')
Start.locate(scene1, 600, 500)
Start.show()

End = Object('Images/end.png')
End.locate(scene1, 600, 450)
End.show()

def clickStart(x, y, action):
    global Blocks
    global Blocknum
    global presentX
    global presentY
    global A
    global B
    for x in range(0,1):
        r = randint(1,4)
        print(r)
        for p in Blocks:
            if r == 1:
                if p.left_checkin(cx, cy):
                    p.lr_change()
                    p.locate(scene1, cx, cy)
                elif p.right_checkin(cx, cy):
                    p.lr_change()
                    p.locate(scene1, cx, cy)
            elif r == 2:
                if p.right_checkin(cx, cy):
                    p.lr_change()
                    p.locate(scene1, cx, cy)
                elif p.right_checkin(cx, cy):
                    p.lr_change()
                    p.locate(scene1, cx, cy)
            elif r == 3:
                if p.up_checkin(cx, cy):
                    p.ud_change()
                    p.locate(scene1, cx, cy)
                elif p.down_checkin(cx, cy):
                    p.ud_change()
                    p.locate(scene1, cx, cy)
            else:
                if p.down_checkin(cx, cy):
                    p.ud_change()
                    p.locate(scene1, cx, cy)
                elif p.up_checkin(cx, cy):
                    p.ud_change()
                    p.locate(scene1, cx, cy)



    '''for x in range(0,1):
        #r = randint(1,4)
        r=1
        print("r", r)
        print("bn", Blocknum)
        #timer.start()
        if r == 1:
            #if Blocknum != 0 and Blocknum != 4 and Blocknum != 8 and Blocknum != 12:
            if presentX != 0:
                Blocks[Blocknum].locate(scene1, A[presentX-1], B[presentY]) #빈블록
                Blocks[presentX - 1].locate(scene1, A[presentX], B[presentY]) #왼블록
                presentX -= 1
                print(presentX)
            else:
                Blocks[Blocknum].locate(scene1,A[presentX+1], B[presentY])
                Blocks[presentX + 1].locate(scene1, A[presentX], B[presentY])
                presentX += 1
                print(presentX)
        elif r == 2:
            #if Blocknum != 3 and Blocknum != 7 and Blocknum != 11 and Blocknum != 15:
            if presentX == 3:
                Blocks[Blocknum].locate(scene1, A[presentX+1], B[presentY]) #빈블록
                Blocks[Blocknum + 1].locate(scene1, A[presentX], B[presentY]) #오른블록
                Blocknum += 1
                presentX += 1
            else:
                Blocks[Blocknum].locate(scene1,A[presentX-1], B[presentY])
                Blocks[Blocknum - 1].locate(scene1, A[presentX], B[presentY])
                Blocknum -= 1
                presentX -= 1
        elif r == 3:
            #if Blocknum != 12 and Blocknum != 13 and Blocknum != 14 and Blocknum != 15:
            if presentY == 0:
                Blocks[Blocknum].locate(scene1, A[presentX], B[presentY-1]) #빈블록
                Blocks[Blocknum + 4].locate(scene1, A[presentX], B[presentY]) #아래블록
                Blocknum += 4
                presentY -= 1
            else:
                Blocks[Blocknum].locate(scene1, A[presentX], B[presentY+1])
                Blocks[Blocknum - 4].locate(scene1, A[presentX], B[presentY])
                Blocknum -= 4
                presentY += 1
        else:
            #if Blocknum != 0 and Blocknum != 1 and Blocknum != 2 and Blocknum != 3:
            if presentY == 3:
                Blocks[Blocknum].locate(scene1, A[presentX], B[presentY+1]) #빈블록
                Blocks[Blocknum - 4].locate(scene1, A[presentX], B[presentY]) #윗블록
                Blocknum -= 4
                presentY += 1
            else:
                Blocks[Blocknum].locate(scene1, A[presentX], B[presentY-1])
                Blocks[Blocknum + 4].locate(scene1, A[presentX], B[presentY])
                Blocknum += 4
                presentY -= 1'''




count = 0
def Timeout():
    global count
    timer.set(0.5)
    count += 1

Start.onMouseAction = clickStart
timer.onTimeout = Timeout()

startGame(scene1)