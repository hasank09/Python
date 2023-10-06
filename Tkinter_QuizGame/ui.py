from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        # self.window.minsize(width=350, height=350)
        self.window.title("Quizzzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # score label;

        self.score = Label(text="Score:0", font=("Arial", 8, 'italic'))
        self.score.config(bg=THEME_COLOR, foreground='white')
        self.score.grid(row=0, column=1, pady=10)

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text='Question',
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)

        # button_True
        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.if_answer_true)
        self.button_true.grid(row=2, column=0, pady=20)

        # button_False
        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.if_answer_false)
        self.button_false.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have completed the Quiz")
            self.button_true.config(state='disabled')
            self.button_false.config(state='disabled')
            # self.window.after(1000, self.window.destroy)
            # self.window.destroy()

    def if_answer_true(self):
        user_answer = 'True'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
        # self.get_next_question()

    def if_answer_false(self):
        user_answer = 'False'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.get_next_question)
