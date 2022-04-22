from tkinter import *
import random

root = Tk()
root.title("Color Guesser")
root.geometry("400x400")
root.configure(background="gold")

label_title = Label(root, text="Color Guesser", font=("sans serif", 25), bg="gold")
label_title.place(relx=0.5, rely=0.1, anchor=CENTER)

label_color = Label(root, font=("sans serif", 20), bg="gold")
label_color.place(relx=0.5, rely=0.3, anchor=CENTER)

class Game:
    def __init__(self):
        self.__score = 0
    
    def updateGames(self):
        self.text = ["Yellow", "Red", "Pink", "Orange", "Green", "Blue"]
        self.random_number_text = random.randint(0, 5)
        label_color["text"] = self.text[self.random_number_text]
        
        self.color = ["red", "pink", "green", "orange", "purple", "yellow"]
        self.random_number_color = random.randint(0, 5)
        label_color["fg"] = self.color[self.random_number_color]

obj = Game()

button = Button(root, text="Start", command=obj.updateGames, bg="SteelBlue1", fg="SteelBlue4", padx=10, pady=1, font=("Arial", 13))
button.place(relx=0.7, rely=0.5, anchor=CENTER)

root.mainloop()