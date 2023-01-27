"""
Todo:
- add gif file to the background
- prompt for each states a question and find the x and y coordinates from the csv file
- send the prompted text to the cordination
"""


import turtle 
import pandas as pd


screen = turtle.Screen()
screen.title('U.S States Game')
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

us_states = pd.read_csv('./50_states.csv')
right_answers =[]


for i in range(len(us_states)):
    answer = screen.textinput(title=f"Guess the state {i+1}/50 " , prompt="what is the another state name?").title()
    state_list = us_states['state'].tolist()
    if answer in right_answers:
        print('You said it before')
    
    elif answer in state_list:
        idx = state_list.index(answer) 
        x_cor = us_states.loc[idx,'x']
        y_cor = us_states.loc[idx,'y']
        right_answers.append(answer)
        # create a text to move to x and y coordinates
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.shape(name=None)
        text_turtle.penup()
        text_turtle.goto(x_cor,y_cor)
        text_turtle.write(answer)
        # text_turtle.hideturtle()
    elif answer =='Exit':
        missed_states =[state for state in us_states['state'].tolist() if state not in right_answers]
        with open('missed_states.csv', 'a') as f:
            for state in missed_states:
                f.write(state)
                f.write('\n')

        break
    else :
        print(f'{answer} is not a U.S states')
        pass





