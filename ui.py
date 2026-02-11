from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Njabs Quiz")
        self.window.config(bg=THEME_COLOR, padx=50, pady=20)

        self.score =  Label(text="Score: 0", font=("Arial", 15, "normal") , bg=THEME_COLOR, fg="white")
        self.score.grid(column=2, row=0,pady=20)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.canvas.create_text(150,125, text="Hello welcome", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=4, pady= 20)


        self.wrong_photo = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_photo, highlightthickness=0)
        self.wrong.grid(column=1, row=3, pady=40)


        self.right_photo = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_photo, highlightthickness=0)
        self.right.grid(column=2, row=3)
        self.window.mainloop()