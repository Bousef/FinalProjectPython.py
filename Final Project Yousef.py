#Yousef Osman
#COP 2500C
#Final Project: Knightro Rock paper scissors
#November 21st 2022

import random

choices = ['rock','paper','scissors']

def endgame():

    print("Knightro has challenged you to rock paper scissors")
    print("You must win to beat Knightro\n")

    score = 0
    computer_score = 0

    play = True

    while play != False:
        if score == 3:
            print("You beat Knightro Great work!")
            end_game = input("\n Select 'Y to end the game: ")
            if end_game == 'Y':
                play = False
                break
        if computer_score == 3:
            print("You lost to Knightro :c ! ")
            end_game = input("\n Select 'Y to end the game: ")
            if end_game.upper() == 'Y':
                play = False
                break

            
        user_input = input("What would you like to choose? : rock, paper, Or scissors: ")
        computer_input = random.choice(choices)
    #outcomes of rock paper scissors
        if user_input == computer_input:
                print("You tied! here are the current scores: ", "Your score: ", score, "\nKnightros Score:", computer_score)
        elif user_input == 'scissors' and computer_input == 'rock':
            computer_score += 1
            print("You lost! here are the current scores: ", "Your score: ", score, "\nKnightros Score:", computer_score)
        elif user_input == 'rock' and computer_input == 'scissors':
            score +=1
            print("You won! here are the current scores: ", "Your score: ", score , "\nKnightros Score:", computer_score)
        elif user_input == 'scissors' and computer_input == 'paper':
            score +=1
            print("You won! here are the current scores: ", "Your score: ", score , "\nKnightros Score:", computer_score)
        elif user_input == 'paper' and computer_input == 'scissors':
            computer_score += 1
            print("You lost! here are the current scores: ", "Your score: ", score, "\nKnightros Score:", computer_score)
        elif user_input == 'rock' and computer_input == 'paper':
            computer_score += 1
            print("You lost! here are the current scores: ", "Your score: ", score, "\nKnightros Score:", computer_score)
        elif user_input == 'paper' and computer_input == 'rock':
            score +=1
            print("You won! here are the current scores: ", "Your score: ", score, "\nKnightros Score:", computer_score)

            
endgame()

        
    


       
        
        
    





    



