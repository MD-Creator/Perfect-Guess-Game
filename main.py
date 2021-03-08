# Name = Mohammed Aamir
# Date = 3-1-2021
# Project Name = Perfect Guess Game
# code starts from here
import random
import sys
import os
import pathlib
class game:
    
    def __init__(self,name):
        self.name = name
        self.first_start_check = "Enter '1' to start or '0' to exit"
        self.again_start_check = "Please try again, Enter '1' to start or '0' to exit"
        self.ask_for_guess = "Guess number between 1 and 100: "
        self.ask_for_down_guess = "come down! Guess number between 1 and 100: "
        self.ask_for_up_guess = "go up! Guess number between 1 and 100: "
        self.ask_for_right_guess = "Please try again, Guess number between 1 and 100: "
        self.ask_to_retry = "Type '1' if you want to play again or '0' to exit: "

    def check_to_start(self,message):
        usr_input = input(f"{message}: ")
        if usr_input == "1":
            return 1
        elif usr_input == "0":
            return 0
        else:
            return game.check_to_start(self, self.again_start_check)
    def startGame(self):
        comp_num = random.randint(1, 100)
        # comp_num = str(comp_num)
        game.perfect_guess(self, comp_num)
    def get_usr_guess(self,message):
        while True:
            try:
                usr_guess = int(input(f"{message}"))
                break
            except ValueError:
                print("Please input number between 1 and 100 only...")  
                continue
        if usr_guess <= 100:
            return usr_guess
        else:
            return game.get_usr_guess(self,self.ask_for_right_guess)
    def perfect_guess(self,comp_num):
        # name = self.name
        print(f"Hello {self.name}, Welcome To Perfect Guess Game")
        print("Computer number is between 1 and 100")
        print("We will ask unless your answer is not correct!")
        print("You have to guess right number in 5 tries")
        usr_guess = game.get_usr_guess(self.name,self.ask_for_guess)
        guesses = 0
        while usr_guess != comp_num:
                if usr_guess > comp_num:
                    print("Come Down!")
                    usr_guess = game.get_usr_guess(self.name,self.ask_for_down_guess)
                    guesses += 1
                elif usr_guess < comp_num:
                    print("Go Up!")
                    usr_guess = game.get_usr_guess(self.name,self.ask_for_up_guess)
                    guesses += 1
        print(f"You Won! you have guessed the right number")
        print(f"Computer Number Was {comp_num}")
        with open(os.path.dirname(os.path.abspath(__file__))+'\\highscore.txt','r') as f:
            highscore = int(f.read())
        if highscore > guesses:
            print(f"You have just broken your previous high score. Your New High Score Is {guesses}")
            with open(os.path.dirname(os.path.abspath(__file__))+'\\highscore.txt', 'w') as f:
                f.write(str(guesses))
        elif highscore < guesses:
            print(f"Your highscore is {highscore}")
        else:
            print(f"Near Miss!")
            print(f"Your highscore is {highscore}")

        retry_input = game.check_to_retry(self,self.ask_to_retry)
        if retry_input == 1:
            game.startGame(self)
        else:
            sys.exit()
    def check_to_retry(self,message):
        retry_input = input(f"{message}")
        if retry_input == "1":
            retry_input = int(retry_input)
            return retry_input
        elif retry_input == "0":
            retry_input = int(retry_input)
            return retry_input
        else:
            output = game.check_to_retry(self,self.ask_to_retry)
            return output
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

name = input("Enter Your Name: ")
perfect_guess_game = game(name)
to_start = perfect_guess_game.check_to_start(perfect_guess_game.first_start_check)
if to_start == 1:
    perfect_guess_game.startGame()
else:
    sys.exit()
