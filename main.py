import pandas
import turtle

screen = turtle.Screen()
screen.title("India Map Quiz")
screen.setup(700,750)

image = "India_Map.gif"
screen.bgpic(image)

states_data = pandas.read_csv("states.csv")
all_states = states_data.state.to_list()
guessed_states = []


#The loop will not stop until user tells name of all states or types "exit" 
while(len(guessed_states) < 28):
    answer_state = screen.textinput(title="Guess the State",prompt="What's another state's name ?").title()

    if answer_state == 'Exit':
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        #Printing the missed states to cross-check
        print(missed_states)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("Missed_states.csv")
        break 

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        else:
            continue
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item()) #here .item() is used soo that only values will be printed
        t.write(answer_state)



'''
Used this function to get the co-ordinates on the map 
By using this you can create the same game for different Country, State or even for world map

def get_mouse_click_coor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
'''

