from tkinter import *
from learn_words import LearnWords
from create_words import CreateWords

class Options:

    def __init__(self):
        self.window_options = Tk()
        self.window_options.title("Hi there!")
        self.window_options.geometry("300x100")
        self.window_options.config(padx=10, pady=10)

        self.ask_label = Label(text="What do you want to do?", font="Arial 10 bold")
        self.ask_label.place(x=65, y=0)

        self.learn_button = Button(text="Learn words", command=self.learn_words)
        self.learn_button.place(x=40, y=40)

        self.create_button = Button(text="Add new words", command=self.add_words)
        self.create_button.place(x=150, y=40)

        self.window_options.mainloop()

    def learn_words(self):
        self.window_options.destroy()
        LearnWords()

    def add_words(self):
        self.window_options.destroy()
        CreateWords()

