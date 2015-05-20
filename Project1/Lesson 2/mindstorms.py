import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(150)
		some_turtle.right(90)
def draw_triangle(some_turtle):
	for i in range(1,4):
		some_turtle.forward(220)
		some_turtle.left(120)
def draw_circle(some_turtle):
	some_turtle.circle(100)


def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("#002F3E")

	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("#009CC7")
	brad.speed(10)
	
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("#C7C7C7")
	angie.speed(10)

	for i in range(1,37):
		draw_circle(angie)
		angie.right(10)
	

	tvd = turtle.Turtle()
	tvd.shape("turtle")
	tvd.color("#01AEA5")
	tvd.speed(10)

	for i in range(1,37):
		draw_triangle(tvd)
		tvd.right(10)

	brad.right(90)
	brad.forward(400)

	window.exitonclick()

draw_shapes()