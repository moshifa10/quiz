from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Njabs Quiz")
        self.window.config(bg=THEME_COLOR, padx=50, pady=20)

        self.score =  Label(text="Score: 0", font=("Arial", 15, "normal") , bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(150,125, 
                                                     width=280,
                                                     text="Hello welcome", 
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady= 50)


        self.wrong_photo = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_photo, highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(column=0, row=3)

        self.right_photo = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_photo, highlightthickness=0, command=self.true_pressed)
        self.right.grid(column=1, row=3)
        self.get_next_question()


        self.window.mainloop()

        # Change the color of the 

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.config(bg="white")
        # print(question)
        self.canvas.itemconfig(self.question_text, text=question)


    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feed_back(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feed_back(is_right)

    def give_feed_back(self, is_right):
        if is_right:
            print(is_right)
            self.window.after(ms=1000, func=self.get_next_question)
            self.canvas.config(bg="green")

        else:
            print(is_right)
            self.window.after(ms=1000, func=self.get_next_question)
            self.canvas.config(bg="red")

        
        # self.window.after(ms=1000, func=self.get_next_question)
        