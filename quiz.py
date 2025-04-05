import pgzrun, random, time

TITLE = "quiz"
WIDTH = 900
HEIGHT = 650

marquebox = Rect(0,0, 900, 80)
skipbox = Rect(0,0, 150, 330)
timerbox = Rect(0,0, 150, 150)
questionbox = Rect(0,0, 650, 150)
option1 = Rect(0,0, 300, 150)
option2 = Rect(0,0, 300, 150)
option3 = Rect(0,0, 300, 150)
option4 = Rect(0,0, 300, 150)
marquebox.move_ip(0,0)
questionbox.move_ip(20, 100)
skipbox.move_ip(700,270)
timerbox.move_ip(700,100)
option1.move_ip(20,270)
option3.move_ip(20,450)
option2.move_ip(370,270)
option4.move_ip(370,450)
options = [option1, option2, option3, option4]
score = 0
timeleft = 10
mmessage = ""
gamestate = False
qbank = "questions.txt"
questions = []
qindex = 0
questioncount = 0




def draw():
    screen.clear()
    screen.fill("teal")
    screen.draw.filled_rect(marquebox, "black")
    screen.draw.filled_rect(questionbox, "grey")
    screen.draw.filled_rect(skipbox, "blue")
    screen.draw.filled_rect(timerbox, "red")
    for i in options:
        screen.draw.filled_rect(i, "orange")
    mmessage = "Welcome to Quizmaster!"
    mmessage += f"Q: {qindex} of {questioncount}"
    screen.draw.textbox(mmessage, marquebox, color = "white")
    
    screen.draw.textbox(que[0], questionbox, color = "black")
    screen.draw.textbox(str(timeleft), timerbox, color = "black")
    screen.draw.textbox("skip", skipbox, color = "black", angle = 90)
    for i in range(4):
        screen.draw.textbox(que[i + 1], options[i], color = "black")
    
def update():
    marquebox.x-=2
    if marquebox.right<0:
        marquebox.left = WIDTH

def readfile():
    global questions,questioncount
    f = open("questions.txt", "r")
    for q in f:
        print(q)
        questions.append(q)
        questioncount += 1
    f.close()
    print(questions)

def nextquestion():
    global qindex
    qindex += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    global score, que, timeleft, questions
    index = 1
    for box in options:
        if box.collidepoint(pos):
            if index is int(que[5]):
                score += 1
                if questions:
                    que = nextquestion()
                    timeleft = 10
                else: 
                    gameover()
            else:
                gameover()
        index += 1
    if skipbox.collidepoint(pos):
        
        if questions and not gamestate:
            que = nextquestion()
            timeleft = 10
        else:
            gameover()
            
def updatetimer():
    global timeleft
    if timeleft != 0:
        timeleft -= 1
    else:
        gameover()

def gameover():
    global timeleft, gameover, que
    m = f"gameover \n You scored: {score}"
    que = [m, "-","-","-","-", 5]
    timeleft = 0
    gamestate = True
                    
readfile()
que = nextquestion()
print(que)    
clock.schedule_interval(updatetimer, 1)            



    
pgzrun.go()


