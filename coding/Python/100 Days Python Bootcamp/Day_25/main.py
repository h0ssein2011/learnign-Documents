import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title('U.S States Game')
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

us_states = pd.read_csv('./50_states.csv')


for i in range(len(us_states)):
    answer = screen.textinput(title="Guess the state" , prompt="what is the another state name?")
    answer = answer.lower().strip()
    df_temp = us_states.query('state == @answer')
    if len(df_temp) ==1 :
        print('x is :',df_temp.x)
        print('y is :',df_temp.y)

screen.exitonclick()