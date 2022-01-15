from tkinter import *
from tkinter import messagebox

class CreateWords:

    def __init__(self):
        self.window = Tk()
        self.window.title("Build your vocab bro!")
        self.window.config(padx=20, pady=20)

        self.word_label = Label(text="Word:")
        self.word_label.grid(column=0, row=0)
        self.type_label = Label(text="Type of word:")
        self.type_label.grid(column=0, row=1)
        self.meaning1_label = Label(text="Meaning 1:")
        self.meaning1_label.grid(column=0, row=2)
        self.meaning2_label = Label(text="Meaning 2:")
        self.meaning2_label.grid(column=0, row=3)
        self.meaning3_label = Label(text="Meaning 3:")
        self.meaning3_label.grid(column=0, row=4)
        self.meaning4_label = Label(text="Meaning 4:")
        self.meaning4_label.grid(column=0, row=5)
        self.synonym_label = Label(text="Synonym:")
        self.synonym_label.grid(column=0, row=6)
        self.antonym_label = Label(text="Antonym:")
        self.antonym_label.grid(column=0, row=7)

        self.word_entry = Entry(width=30)
        self.word_entry.grid(column=1, row=0)
        self.type_entry = Entry(width=30)
        self.type_entry.grid(column=1, row=1)
        self.meaning1_entry = Entry(width=30)
        self.meaning1_entry.grid(column=1, row=2)
        self.meaning2_entry = Entry(width=30)
        self.meaning2_entry.grid(column=1, row=3)
        self.meaning3_entry = Entry(width=30)
        self.meaning3_entry.grid(column=1, row=4)
        self.meaning4_entry = Entry(width=30)
        self.meaning4_entry.grid(column=1, row=5)
        self.synonym_entry = Entry(width=30)
        self.synonym_entry.grid(column=1, row=6)
        self.antonym_entry = Entry(width=30)
        self.antonym_entry.grid(column=1, row=7)

        self.add_button = Button(text="Add", width=10, command=self.add_word)
        self.add_button.grid(column=1,row=8)
        self.window.mainloop()

    def add_word(self):
        word = self.word_entry.get()
        type = self.type_entry.get()
        meaning1 = self.meaning1_entry.get()
        meaning2 = self.meaning2_entry.get()
        meaning3 = self.meaning3_entry.get()
        meaning4 = self.meaning4_entry.get()
        synonym = self.synonym_entry.get()
        antonym = self.antonym_entry.get()

        if len(word) == 0:
            messagebox.showinfo(title="Hmm", message="Bruh! Enter a word!")
        elif len(type) == 0:
            messagebox.showinfo(title="Hmm", message="Type of the word?")
        elif len(meaning1) == 0 and len(meaning2) == 0 and len(meaning3) == 0 and len(meaning4) == 0:
            messagebox.showinfo(title="Hmm", message="Give at least one definition of the word bro!")
        elif len(synonym) == 0:
            messagebox.showinfo(title="Hmm", message="Give at least one synonym of the word bro!")
        elif len(antonym) == 0:
            messagebox.showinfo(title="Hmm", message="Give at least one antonym of the word bro!")
        else:
            if len(meaning1) != 0:
                meaning1 += "\\n"
            if len(meaning2) != 0:
                meaning2 += "\\n"
            if len(meaning3) != 0:
                meaning3 += "\\n"

            # try:
            #     with open("data/remaining_words.csv", "a") as test2:
            #         test2.write(f"{word},{type},{meaning1}{meaning2}{meaning3}{meaning4},'{synonym}','{antonym}'\n")
            # except FileNotFoundError:
            #     pass

            with open("data/words_to_learn.csv", "a") as test:
                test.write(f'{word},{type},"{meaning1}{meaning2}{meaning3}{meaning4}","{synonym}","{antonym}"\n')
            messagebox.showinfo(title="Noice!!", message="You've successfully created a new word!\n Keep it up bro!")

            self.word_entry.delete(0, END)
            self.type_entry.delete(0, END)
            self.meaning1_entry.delete(0, END)
            self.meaning2_entry.delete(0, END)
            self.meaning3_entry.delete(0, END)
            self.meaning4_entry.delete(0, END)
            self.synonym_entry.delete(0, END)
            self.antonym_entry.delete(0, END)