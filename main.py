import turtle
import sys
import random

questions = {
    'Where does Cristiano ronaldo play?' : 'Real Madrid\n',
    'Where does Lionel Messi play?' : 'Barcelonda\n',
    'Where does Neymar play?' : 'PSG\n',
    'Where does Kylian Mbappé  play?' : 'PSG\n',
    'Where does Zlatan Ibrahimović play? ' : 'PSG\n',
    'Where does Paul Pogba play?' : 'Manchester United\n',
    'Where does Gareth Bale play?' : 'Real Madrid\n',
    'Where does Robert Lewandowski play?' :'Bayern Munich\n',
    'Where does Eden Hazard play?' : 'Real Madrid\n',
    'Where does Sergio Agüero play? ' : 'Man City\n',
    'Where does Sadio Mané play?' : 'Liverpool\n',
    'Where does Jamie Vardy play?' : 'Leicester City\n',
    'Where does Kevin De Bruyne play?' : 'Man city\n',
    'Who is Chelseas GoalKeeper?' : 'Kepa\n',
    'Whos the best Chelsea Midfielder?' : 'KANTE!\n',
    'What animal has a long neck?' : 'Giraffee\n',
    'Where does Mohamed Salah play?' : 'Liverpool\n',
    'Where does Lingard play?' : 'ManchesterCity\n',
    'What position does Virgil van Dijk play?' : 'Defender\n',
    'What position does Karim Benzema play?' : 'Striker\n',
    'What position does Manuel Neuer play?': 'GoalKeeper\n',
    'Where does Tony Kroos play?': 'RealMadrid\n',
    'What position does Peter Schmeichel play?': 'GoalKeeper\n',
    'What position does Son play?': 'Midfielder\n',
    'What position does Petr Cech play?': 'GoalKeeper\n'
}
# turtle.bgpic("PythonPitch.jpg")


turtle.color('black')
style = ('Arial', 30, 'italic')
turtle.hideturtle()

# turtle.setup(800, 800)
# turtle.bgpic("PythonPitch.jpg")

#turtle.bgcolor("lightgreen") #This is to set the bg any color you want

# turtle.addshape("rocketship.png")
# turtle.shape("rocketship.png")

# turtle.addshape(image)
# turtle.shape(image)

# turtle.bgpic('image1.gif')


def Win():
    if Kevin.position() == (540.00,0.00):
        turtle.write('Win!', font=style, align='center')
def Loose():
    if Kevin.position() == (-540.00,0.00):
        turtle.write('Loose!', font=style, align='center')

Kevin = turtle.Pen()
Kevin.up()
# print("What is 2 + 2?")
# question1 = int(sys.stdin.readline())
# if question1 == 4:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# print("What is 10 - 5?")
# question2 = int(sys.stdin.readline())
# if question2 == 5:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# print("What is 2 * 12?")
# question3 = int(sys.stdin.readline())
# if question3 == 24:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# # print("What is 6 / 2?")
# question4 = int(sys.stdin.readline())
# if question4 == 3:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# # print("What is 9 - 3?")
# question5 = int(sys.stdin.readline())
# if question5 == 6:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)
# Win()
# Loose()
#
# # print("What is 44 - 11?")
# question6 = int(sys.stdin.readline())
# if question6 == 33:
#     Kevin.forward(90)
# else:
#     Kevin.backward(90)


while (Kevin.position() != (540.00,0.00) or Kevin.position() != (-540.00,0.00)):
    key = random.choice(list(questions))
    print(key)
    answer = str(sys.stdin.readline())
    if answer.lower() == questions[key].lower():
        Kevin.forward(90)
    else:
        Kevin.backward(90)
    Win()
    Loose()
    #print(Kevin.position())

turtle.mainloop()





