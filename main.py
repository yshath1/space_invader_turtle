import turtle

starting_y = -300
starting_x = 0


def move_left():
    global starting_x
    starting_x -= 10
    player.setx(starting_x)


def move_right():
    global starting_x
    starting_x += 10
    player.setx(starting_x)


window = turtle.Screen()
window.title("Space Invaders")
window.setup(500, 700)
window.bgpic(picname="original.gif")

"""Player"""
player = turtle.Turtle()
turtle.register_shape("ship.gif")
player.penup()
player.shape("square")
player.shapesize(stretch_wid=1, stretch_len=3)
player.setposition(starting_x, starting_y)
player.color("blue")
player.showturtle()

##Stores all bullets
bullets = []


def player_bullet():
    global aliens
    barrel = -300
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.setposition(starting_x, barrel)
    bullet.color("blue")
    bullet.shape("triangle")
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullets.append(bullet)
    while True:
        if barrel > 300:
            bullet.ht()

        for bullet in bullets:
            for alien in aliens:
                alien.setheading(-90)
                alien.forward(.02)
                if bullet.distance(alien) <= 11:
                    aliens.pop(aliens.index(alien))
                    alien.ht()
                    # Send the bullet to another dimension
                    bullet.ht()
                    bullet.setposition(330, 300)
                elif alien.ycor() < -300:
                    label = turtle.Turtle()
                    label.hideturtle()
                    label.penup()
                    label.color("white")
                    label.goto(0, 0)
                    label.write("Game Over!", align="center", font=("Courier", 24, "normal"))
                    break

            bullet.forward(1)

        turtle.update()


"""Enemy"""
enemy_y = 300
enemy_x = 110
aliens = []
for enemy in range(14):

    alien = turtle.Turtle()
    alien.penup()
    alien.shape("triangle")
    alien.color("red")
    alien.shapesize(stretch_wid=1, stretch_len=1)
    alien.setposition(enemy_x, enemy_y)
    turtle.tracer(0)
    aliens.append(alien)
    if enemy == 6:
        enemy_y -= 50
        enemy_x = 90
        alien.setposition(enemy_x, enemy_y)
    elif enemy == 11:
        enemy_y -= 50
        enemy_x = 40
        alien.setposition(enemy_x, enemy_y)

    enemy_x -= 50

turtle.onkeypress(move_left, key="Left")
turtle.onkeypress(move_right, key="Right")
turtle.onkeypress(player_bullet, key="space")
turtle.listen()
turtle.update()

window.mainloop()