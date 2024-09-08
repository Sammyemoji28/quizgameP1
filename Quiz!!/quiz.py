
import pgzrun

HEIGHT = 650
WIDTH = 870

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

score = 0
timeLeft = 10
fileName = "questions.txt"
isGameover = False
marqueeMessage = ""
questions = []
question = []
answerBoxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questionCount = 0
questionIndex = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marqueeMessage
    screen.clear()
    screen.fill("black")
    screen.draw.rect(marquee_box,"black")
    screen.draw.rect(question_box,"green")
    screen.draw.rect(timer_box,"red")
    screen.draw.rect(skip_box,"purple")
    for answerbox in answerBoxes:
        screen.draw.rect(answerbox,"yellow")
    marqueeMessage = f"Welcome to the quiz! Question: {questionIndex} out of {questionCount}."
    screen.draw.textbox(marqueeMessage, marquee_box, color = "white")
    screen.draw.textbox(str(timeLeft), timer_box, color = "white", shadow = (0.5,0.5), scolor = "dim grey")
    screen.draw.textbox("Skip", skip_box, color = "white", shadow = (0.5,0.5), scolor = "dim grey", angle = -90)
    #screen.draw.textbox(question[0].strip(), question_box, color = "white", shadow = (0.5,0.5), scolor = "dim grey")
    index = 1
    for answerbox in answerBoxes:
        #screen.draw.textbox(question[index].strip, answerbox, color = "white", shadow = (0.5,0.5), scolor = "dim grey")
        index += 1

def moveMarquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update():
    moveMarquee()
     

pgzrun.go()