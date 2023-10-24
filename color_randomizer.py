from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.configure(background = "light grey")
root.title("Color Randomizer")

label = Label(root, text = "TEXT", font = ("Ariel", 30))
label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

entry = Entry(root)
entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)


class randomizer():
    
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
        self.random_num = random.randint(0,5)
        self.color = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.color_random = random.randint(0,5)
        
    def get_input(self):
        if(input_value == self.color[self.random_number_for_color]):
            self.__score = self.__score + random.randint(0, 10)
            obj.get_user_value(value)
            input_value.delete(0, END)

        
        
r = randomizer()
score = self.__score
label_score.place(relx = 0.1, rely = 0.1, anchor = CENTER)
      
btn = Button(root, text = "Check", command = r.get_input, bg = "IndianRed1", fg = "white", relief = FLAT, padx = 10, pady = 1, font = ("Arial,", 15))
btn.pack()

root.mainloop()
    