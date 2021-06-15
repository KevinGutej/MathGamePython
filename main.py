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

screen = turtle.Screen()
screen.setup(626, 420)
screen.title("Kevin Football  !")
turtle.bgpic("pitch.gif")

def Win():
    if Kevin.position() == (270.00,0.00):
        turtle.bgpic("")
        screen.update()
        turtle.bgcolor("green")
        turtle.write('Win!', font=style, align='center')
def Loose():
    if Kevin.position() == (-270.00,0.00):
        turtle.bgpic("")
        screen.update()
        turtle.bgcolor("red")
        turtle.write('LOSER!', font=style, align='center')

Kevin = turtle.Pen()
Kevin.up()

while (Kevin.position() != (270.00,0.00) or Kevin.position() != (-270.00,0.00)):
    key = random.choice(list(questions))
    print(key)
    answer = str(sys.stdin.readline())
    if answer.lower() == questions[key].lower():
        Kevin.forward(90)
        print("Great!")
    else:
        Kevin.backward(90)
        print("Wrong")
    Win()
    Loose()
turtle.mainloop()





