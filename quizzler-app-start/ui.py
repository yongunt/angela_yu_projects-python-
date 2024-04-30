from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.lbl.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR, width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, columnspan=2, pady=50)

        true_photo = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_photo, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_photo = PhotoImage(file="images/false.png")

        self.false_button = Button(image=false_photo, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nYour score is: "
                                                            f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        color = self.quiz.check_answer("True")
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)

    def false_answer(self):
        color = self.quiz.check_answer("False")
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)
