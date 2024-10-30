# implementation of card game - Memory

import simplegui
import random

# global variables

exposed_card = [False]*16
mem_deck = range(0, 8)*2
counter = 0
card1 = 0
card2 = 0
x = 20
state = 0

# helper function to initialize globals
def new_game():
    global state, mem_deck, exposed_card, counter
    
    exposed_card = [False]*16
    state = 0
    counter = 0
    random.shuffle(mem_deck)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed_card, mem_deck, counter, card1, card2, state
    
    num_of_cards = pos[0]/50
    if exposed_card[num_of_cards] == False:
        exposed_card[num_of_cards] = True
        if state == 0:
            state = 1
            card1 = num_of_cards
        elif state == 1:
            state = 2
            card2 = num_of_cards
            counter += 1
            if mem_deck[card1] == mem_deck[card2]:
                exposed_card[card1] = True
                exposed_card[card2] = True            
        else:
            state = 1
            if mem_deck[card1] != mem_deck[card2]:
                exposed_card[card1] = False
                exposed_card[card2] = False
            card1 = num_of_cards
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global x, deck_pos, exposed, counter
    
    for num in range(0,len(mem_deck)):
        canvas.draw_text(str(mem_deck[num]),[x+50*num,60],40,"#D2B4DE ")
        if exposed_card[num] == False:
            canvas.draw_polygon([(num*50, 0),((num+1)*50, 0),((num+1)*50,100),(num*50,100) ], 2, '#CB4335', '#F1948A ')
    label.set_text("Turns = "+str(counter))



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+str(counter), 100)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
