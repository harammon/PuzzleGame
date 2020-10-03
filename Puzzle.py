from bangtal import *
import random
import time

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("겨울왕국", "images/배경.jpg")

startTime = 0
endTime = 0 
def find_index(object):
    for index in range(16):
        if game_board[index] == object:
            return index

def movable(index):
    if index < 0 or index > 15:
        return False
    if index % 4 > 0 and index - 1 == blank:
        return True
    if index % 4 < 3 and index + 1 == blank:
        return True
    if index > 3 and index - 4 == blank:
        return True
    if index < 12 and index + 4 == blank:
        return True
    return False

def move(index):
    global blank
    game_board[index].locate(scene, 369 + 150 * (blank % 4), 567 - 150 * (blank // 4))
    game_board[blank].locate(scene, 369 + 150 * (index % 4), 567 - 150 * (index // 4))

    game_board[blank], game_board[index] = game_board[index], game_board[blank]
    
    blank = index

def completed():
    for index in range(16):
        if game_board[index] != init_board[index]:
            return False
    return True

delta = [-1, 1, -4, 4]
def random_move():
    while True:
        index = blank + delta[random.randrange(4)]
        if movable(index):
            break
    move(index)



def onMouseAction_piece(object, x, y, action):
    #object를 blank와 바꾼다.
    global startTime
    global endTime
    index = find_index(object)
    if movable(index):
        move(index)
        endTime=0
        if completed():
            endTime = time.time()
            msg = str(str(int(endTime - startTime))+"초 걸렸습니다.")
            showMessage(msg)
Object.onMouseActionDefault = onMouseAction_piece


game_board = []
init_board = []
for index in range(16):
    piece = Object("images/" + str(index + 1) + ".png")
    piece.locate(scene, 369 + 150 * (index % 4), 567 - 150 * (index // 4))
    piece.show()

    game_board.append(piece)
    init_board.append(piece)


blank = 15
game_board[blank].hide()

count = 150 
timer = Timer(1)
def onTimeOut():
    random_move()
    global count
    global startTime
    count = count - 1
    if count > 0:
        timer.set(0.05)
        timer.start()
    elif count == 0:
        startTime = time.time()


timer.onTimeout = onTimeOut

timer.start()
showTimer(timer)

startGame(scene)
