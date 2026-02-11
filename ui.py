from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Njabs Quiz")
        self.score =  Label(text="Score", font=("Arial", 8, "normal"))

        self.window.mainloop()