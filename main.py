import turtle
import sys

turtle.color('black')
style = ('Arial', 30, 'italic')
turtle.hideturtle()

def Win():
    if Kevin.position() == (540.00,0.00):
        turtle.write('Win!', font=style, align='center')
def Loose():
    if Kevin.position() == (-540.00,0.00):
        turtle.write('Loose!', font=style, align='center')

Kevin = turtle.Pen()
Kevin.up()
print("What is 2 + 2?")
question1 = int(sys.stdin.readline())
if question1 == 4:
    Kevin.forward(90)
else:
    Kevin.backward(90)
Win()
Loose()

print("What is 10 - 5?")
question2 = int(sys.stdin.readline())
if question2 == 5:
    Kevin.forward(90)
else:
    Kevin.backward(90)
Win()
Loose()

print("What is 2 * 12?")
question3 = int(sys.stdin.readline())
if question3 == 24:
    Kevin.forward(90)
else:
    Kevin.backward(90)
Win()
Loose()

print("What is 6 / 2?")
question4 = int(sys.stdin.readline())
if question4 == 3:
    Kevin.forward(90)
else:
    Kevin.backward(90)
Win()
Loose()

print("What is 9 - 3?")
question5 = int(sys.stdin.readline())
if question5 == 6:
    Kevin.forward(90)
else:
    Kevin.backward(90)
Win()
Loose()

print("What is 44 - 11?")
question6 = int(sys.stdin.readline())
if question6 == 33:
    Kevin.forward(90)
else:
    Kevin.backward(90)
Win()
Loose()

print(Kevin.position())
turtle.mainloop()