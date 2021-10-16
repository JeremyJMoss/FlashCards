from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
selected_entry = None
flip_card_delay = None


# function for swapping to english side of card
def flip_card():
    global selected_entry
    card.itemconfigure(card_side, image=card_back)
    card.itemconfigure(language, text="English", fill="white")
    card.itemconfigure(word, text=selected_entry["English"], fill="white")


# creating flash card
def card_create(button_pressed=None):
    global selected_entry, flip_card_delay
    try:
        window.after_cancel(flip_card_delay)
    except ValueError:
        pass
    finally:
        try:
            data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            data = pandas.read_csv("data/french_words.csv")
        finally:
            word_dictionary = data.to_dict(orient="records")
            if button_pressed == "yes":
                word_dictionary.remove(selected_entry)
                dataframe = pandas.DataFrame.from_dict(word_dictionary)
                dataframe.to_csv("data/words_to_learn.csv", mode="a", index=False)
            selected_entry = choice(word_dictionary)
            card.itemconfigure(card_side, image=card_front)
            card.itemconfigure(language, text="French", fill="black")
            card.itemconfigure(word, text=selected_entry["French"], fill="black")
            flip_card_delay = window.after(ms=3000, func=flip_card)


# creating the user interface
window = Tk()
window.title("Flash Cards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_side = card.create_image(400, 263, image=card_front)
language = card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = card.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=lambda: card_create("yes"))
yes_button.grid(row=1, column=0)
no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=card_create)
no_button.grid(row=1, column=1)
# initializing first card
card_create()

window.mainloop()
