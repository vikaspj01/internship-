from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("Rock Paper Scissors Game")
app_font = font.Font(size = 20)
root.config(bg = 'white')
root.geometry('1000x500')

player_score = 0
computer_score = 0
options = [('rock', 0), ('paper', 1), ('scissors', 2)]

Label(text = 'Task 4 code Soft', font = font.Font(size = 25), bg = 'lightblue').pack()
Label(text = 'Rock Paper Scissors', font = font.Font(size = 25), bg = 'white').pack()



#Player input
def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text = "Tie")
    elif (player_input[1]-computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Your Score : ' + str(computer_score))

#computer choice
def get_computer_choice():
    return random.choice(options)


winner_label = Label(text = "Let's Start the Game...", fg = 'red', bg = 'white', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(root, bg = 'white')
input_frame.pack()

player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'black', bg = 'light grey')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock',font = font.Font(size = 15), width = 20, bd = 0, bg = 'pink', pady = 15, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper',font = font.Font(size = 15), width = 20, bd = 0, bg = '#FFEBCD', pady = 15, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors',font = font.Font(size = 15), width = 20, bd = 0, bg = 'light yellow', pady = 15, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'black', bg = 'light grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font,bg = '#F0FFFF')
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : 0', font = app_font, bg = 'light green')
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black', bg = '#F0FFFF')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : 0', font = app_font, fg = 'black', bg = 'light green')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

root.mainloop()


