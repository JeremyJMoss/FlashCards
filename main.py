from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card.create_image(400, 263, image=card_front)
card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0)
yes_button.grid(row=1, column=0)
no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0)
no_button.grid(row=1, column=1)

window.mainloop()
