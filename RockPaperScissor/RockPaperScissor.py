import tkinter as tk
from tkinter import *
import random

class RockPaperScissorGame:
    
    def __init__(self,Root):
        self.user_score=0
        self.computer_score=0
        self.root =Root
        self.root.title("Rock - Paper - Scissor Game")

        self.label_title = Label (Root,text="Rock - Paper - Scissor Game",font=('Helvetica',16,"bold"))

        self.img = PhotoImage(file='image1.png')
        self.image_label = Label(Root,image=self.img)
        self.image_label.pack(pady=20)

        self.result_label = Label(Root,text=" ",font=('Helvetics',14))
        self.result_label.pack(pady=10)

        self.button_frame = tk.Frame(Root)
        self.button_frame.pack(pady=20)

        self.create_button("Rock")
        self.create_button("Paper")
        self.create_button("Scissors")

    def create_button(self, choice):
        button = Button(self.button_frame,text=choice,command=lambda:self.play(choice),background="black",foreground="white")
        button.pack(side=tk.LEFT,padx=10)

    def play(self, user_choice):
        choices=["Rock","Paper","Scissors"]
        computer_choice = random.choice(choices)

        result_text = f"Computer choose {computer_choice} and You choose {user_choice}.\n Computer score = {self.computer_score} and Your score = {self.user_score}.\n"
        result_text+=self.determine_winner(user_choice,computer_choice)
    

        self.result_label.config(text=result_text)

    def determine_winner(self,user_choice,computer_choice):
        if user_choice==computer_choice:
            return "It's a tie"
        elif(
            (user_choice=="Rock" and computer_choice == "Scissors")or(user_choice=="Paper" and computer_choice == "Rock")or(user_choice=="Scissors" and computer_choice == "Paper")
        ):
            self.user_score+=1
            return "You win!"
        else:
            self.computer_score+=1
            return "Computer wins!"
        
if __name__=="__main__" :
    Root =tk.Tk()
    Root.geometry('500x550')
    game= RockPaperScissorGame(Root)
    Root.mainloop()
