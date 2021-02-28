from ursina import *  # import everything we need with one line.
import random

app = Ursina()
EditorCamera()


lText = Text("Green wins!", color=color.green, scale=(1, 1), y=.45, x=-.08, enabled=False)
rText = Text("Orange wins!", color=color.orange, scale=(1, 1), y=.45, x=-.08, enabled=False)

ceiling = Entity(model='quad', y=3, scale=(13, .3), collider='box')
floor = duplicate(ceiling, y=-3)

left_paddle = Entity(model='quad', color=color.green, x=-6, scale=(0.1, 1.4), collider='box')
right_paddle = duplicate(left_paddle, color=color.orange, x=6)

left_wall = Entity(model='quad', x=-6.5, scale=(.3, 6.3), collider='box')
right_wall = duplicate(left_wall, x=6.5)

centers = []
for posy in range(-240, 280, 60):
    center = Entity(model='quad', scale=(0.15, 0.4), y=posy / 100)
    centers.append(center)

ball = Entity(model='circle', color=color.white, scale=.2, speed=18, collider='box', rotation_z=0,
              colison_cooldown=time.dt)
placares = []
placar_0 = Entity(model='circle', color=color.white, scale=.2, x=-4.5, y=3.3)
placar_1 = duplicate(placar_0, x=-4.2)
placar_2 = duplicate(placar_0, x=-3.9)

placar_3 = duplicate(placar_0, x=4.5)
placar_4 = duplicate(placar_0, x=4.2)
placar_5 = duplicate(placar_0, x=3.9)
placares.append(placar_0)
placares.append(placar_1)
placares.append(placar_2)
placares.append(placar_3)
placares.append(placar_4)
placares.append(placar_5)
r_score = 0
l_score = 0


def update():
    global r_score
    global l_score




    left_paddle.y += (held_keys['w'] - held_keys['s']) * time.dt * 3
    right_paddle.y += (held_keys['up arrow'] - held_keys['down arrow']) * time.dt * 3
    ball.position += ball.right * ball.speed * time.dt

    if left_paddle.y > 3:
        left_paddle.y = 3
    if left_paddle.y < -3:
        left_paddle.y = -3

    if right_paddle.y > 3:
        right_paddle.y = 3
    if right_paddle.y < -3:
        right_paddle.y = -3

    hit_info = ball.intersects()
    if hit_info.hit:
        r_value = random.randint(-45, 45)

        if hit_info.entity == right_paddle:
            delta = ball.y - right_paddle.y
            ball.rotation_z = (180 + delta * 80) + r_value
            ball.speed = ball.speed * 1.05
            if ball.speed > 20:
                ball.speed == 20

        if hit_info.entity == left_paddle:
            delta = ball.y - left_paddle.y
            ball.rotation_z = (0 - delta * 80) + r_value
            ball.speed = ball.speed * 1.05
            if ball.speed > 20:
                ball.speed == 20

        if hit_info.entity == ceiling:
            ceiling.collision = False
            ball.rotation_z = (ball.rotation_z * -1)
            ceiling.collision = True
        if hit_info.entity == floor:
            floor.collision = False
            ball.rotation_z = (ball.rotation_z * -1)
            floor.collision = True

        if hit_info.entity == right_wall:
            right_wall.collision = False
            ball.position = (0, 0)
            ball.speed = 18
            ball.rotation_z = 0
            right_wall.collision = True
            l_score += 1
            if l_score == 1:
                placar_0.color = color.green
            if l_score == 2:
                placar_1.color = color.green
            if l_score == 3:
                placar_2.color = color.green
                l_win()

        if hit_info.entity == left_wall:
            left_wall.collision = False
            ball.position = (0, 0)
            ball.speed = 18
            ball.rotation_z = 180
            left_wall.collision = True
            r_score += 1
            print(r_score)
            if r_score == 1:
                placar_3.color = color.orange
            if r_score == 2:
                placar_4.color = color.orange
            if r_score == 3:
                placar_5.color = color.orange
                r_win()


def r_win():
    rText.enabled = True
    finish()


def l_win():
    lText.enabled = True
    finish()

def finish():
    global r_score
    global l_score

    ball.position = (0, 0)
    ball.speed = 18
    left_paddle.position = (-6, 0)
    right_paddle.position = (6, 0)
    r_score = 0
    l_score = 0
    ball.speed = 0


def input(key):
    if key == 'space':
        start()

def start():
    global r_score
    global l_score

    lText.enabled = False
    rText.enabled - False
    ball.position = (0, 0)
    ball.speed = 18
    left_paddle.position = (-6, 0)
    right_paddle.position = (6, 0)
    r_score = 0
    l_score = 0
    for placar in placares:
        placar.color = color.white



app.run()
