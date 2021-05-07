from turtle import *
from random import randrange
from random import randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y



def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insideFood(foodHead):
    "Return True if head inside boundaries."
    return -200 < foodHead.x < 190 and -200 < foodHead.y < 190

def move():
    "Move snake forward one segment."
    foodHead = food.copy()
    head = snake[-1].copy()
    head.move(aim)

    #for pos in range(100):
    #food.x = (food.x)+(randrange(-1,1)*randrange(-1, 1)*10)
    #food.y = (food.y)+(randrange(-1,1)*randrange(-1, 1)*10)
    luck=randint(0,3)
    print(luck)
    
    if luck == 0:
        food.x = (food.x)+(randint(-1, 1)*10)
    
    if luck == 1:
        food.y = (food.y)+(randint(-1,1)*randint(-1, 1)*10)

    if not insideFood(foodHead) :
        food.x = 0
        food.y = 0

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        
        
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()