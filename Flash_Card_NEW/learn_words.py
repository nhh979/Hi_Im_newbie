from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#7CD1B8"
ORANGE ="#FF7F3F"
PURPLE = "#502064"
DARK_BLUE = "#000B49"

dictionary = None

try:
    data = pandas.read_csv("data/remaining_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/words_to_learn.csv")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data/words_to_learn.csv")

dictionary = data.to_dict(orient="records")
random_word = {}

class LearnWords:

    def __init__(self):
        self.window = Tk()
        self.window.title("Flash Cards")
        self.window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
        self.front_image = PhotoImage(file="images/card_front.png")
        self.back_image = PhotoImage(file='images/card_back.png')

        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

        self.background = self.canvas.create_image(400, 263, image=self.front_image)
        self.current_word = self.canvas.create_text(400, 263, width=720, text=' ', font="Courier 50 bold")
        self.type_word = self.canvas.create_text(400, 100, text=' ', font="Courier 30 italic")
        self.synonym = self.canvas.create_text(100, 460, anchor="sw", text=" ", font="Calibri 15 italic")
        self.antonym = self.canvas.create_text(100, 485, anchor="sw", text=" ", font="Calibri 15 italic")
        self.remaining = self.canvas.create_text(130,50, text=" ", fill=ORANGE, font="Courier 12 bold")
        self.canvas.grid(column=0, row=0, columnspan=3, )

        check_image = PhotoImage(file="images/right.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.remove_cards)
        self.check_button.grid(column=2, row=1)

        cross_image = PhotoImage(file="images/wrong.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.next_card)
        self.cross_button.grid(column=0, row=1)

        self.reset_button = Button(text="reset", highlightthickness=0, command=self.reset)
        self.reset_button.grid(column=1, row=1)

        self.flip_timer = self.canvas.after(3000, self.flip_card)
        self.next_card()

        self.window.mainloop()


    def next_card(self):
        global random_word
        self.canvas.after_cancel(self.flip_timer)

        if len(dictionary) > 0:
            random_word = random.choice(dictionary)
            self.canvas.itemconfig(self.background, image=self.front_image)
            self.canvas.itemconfig(self.current_word, text=random_word["Word"], fill="black", font="Courier 50 bold")
            self.canvas.itemconfig(self.type_word, text=" ", fill="white")
            self.canvas.itemconfig(self.synonym, text=" ", fill="white")
            self.canvas.itemconfig(self.antonym, text=" ", fill="white")
            self.canvas.itemconfig(self.remaining, text=f"Remaining cards: {len(dictionary)}")
            self.flip_timer = self.canvas.after(3000, self.flip_card)
        else:
            self.cross_button.config(state='disabled')
            self.check_button.config(state='disabled')
            self.canvas.itemconfig(self.background, image=self.front_image)
            self.canvas.itemconfig(self.current_word, text="Congrats!!\nYou've finished all the words.", fill="pink")
            self.canvas.itemconfig(self.type_word, text=" ", fill="white")
            self.canvas.itemconfig(self.synonym, text=" ", fill="white")
            self.canvas.itemconfig(self.antonym, text=" ", fill="white")
            self.canvas.itemconfig(self.remaining, text=f" ")

    def flip_card(self):
        add_line_meaning = random_word["Meaning"].replace("\\n", "\n")
        self.canvas.itemconfig(self.background, image=self.back_image)
        self.canvas.itemconfig(self.current_word, text=add_line_meaning, fill="white", font="Arial 25 normal")
        self.canvas.itemconfig(self.type_word, text=random_word["Type"], fill=PURPLE)
        self.canvas.itemconfig(self.synonym, text=f"Synonym: {random_word['Synonym']}", fill=DARK_BLUE)
        self.canvas.itemconfig(self.antonym, text=f"Antonym: {random_word['Antonym']}", fill=DARK_BLUE)
        self.canvas.itemconfig(self.remaining, text=f" ")

    def remove_cards(self):
        dictionary.remove(random_word)
        data_words = pandas.DataFrame(dictionary)
        data_words.to_csv("data/remaining_words.csv", index=None)
        self.next_card()

    def reset(self):
        global dictionary
        os.remove("data/remaining_words.csv")
        data = pandas.read_csv("data/words_to_learn.csv")
        dictionary = data.to_dict(orient="records")
        self.cross_button.config(state='normal')
        self.check_button.config(state='normal')
        self.next_card()