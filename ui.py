from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score
        self.score = Label(text=f'Score: 0', highlightthickness=0, bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)
        # Question canvas
        self.question_canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125, font=("Arial", 20, "italic"),
                                                              text="Test", fill=THEME_COLOR, width=280)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=40)
        # Buttons
        false_button = PhotoImage(file='images/false.png')
        true_button = PhotoImage(file='images/true.png')
        self.right_button = Button(image=true_button, highlightthickness=0, highlightbackground=THEME_COLOR,
                                   command=self.click_true)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = Button(image=false_button, highlightthickness=0, highlightbackground=THEME_COLOR,
                                   command=self.click_false)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.question_canvas.config(bg='white')
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def click_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):

        if is_right:
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
