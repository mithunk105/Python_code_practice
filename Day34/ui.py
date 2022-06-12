from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizWindow:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lable = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.lable.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(
            150,
            125,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 10, "italic"),
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=1)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lable.config(text=f"Score: {self.quiz.score}")
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_txt)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
