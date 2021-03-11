from quotes import quotes
from random import choice
from tkinter import *
from time import time

LIGHT_BLUE = "e8e8e4"
GREEN = "#9bdeac"
start_typing = False
stop_typing = False
start_time = 0
end_time = 0
correct_words = []
incorrect_words = []
quote = choice(quotes)
# quote = "This is a lovely day today"
quote_words = quote.split(" ")
quote_word_count = len(quote_words)


def try_again():
    global start_typing
    global stop_typing
    global end_time
    global start_time
    global correct_words
    global incorrect_words
    global quote
    global quote_words
    global quote_word_count
    start_typing = False
    stop_typing = False
    start_time = 0
    end_time = 0
    correct_words = []
    incorrect_words = []
    quote = choice(quotes)
    quote_words = quote.split(" ")
    quote_word_count = len(quote_words)
    text_entry.delete("1.0", "end")
    results.config(text="To begin, simply start typing.\n\n When you complete typing the sentence above, you will get "
                        "your "
                        "results.")
    canvas.itemconfig(quote_text, text=quote)

def start_typing_f():
    global start_typing
    global start_time
    if len(text_entry.get("1.0", "end")) > 1 and not start_typing:
        start_time = time()
        start_typing = True
    window.after(1, start_typing_f)


def stop_typing_f():
    global end_time
    global start_time
    global stop_typing
    global correct_words
    global incorrect_words
    text = text_entry.get("1.0", "end")
    text_words = text.split(" ")
    text_words_count = len(text_words)
    # print(text_words)
    # print(quote_words)
    # print(text_words_count)
    # print(quote_word_count)
    if text_words_count == quote_word_count and \
            text_words[-1].replace("\n", "") == quote_words[-1] and not stop_typing:
        end_time = time()
        stop_typing = True
        total_time = end_time - start_time
        for word in quote_words:
            if word == text_words[quote_words.index(word)].replace("\n", ""):
                correct_words.append(word)
            else:
                incorrect_words.append(word)
        results.config(text=f'percent of words typed correctly: {int(100 * (len(correct_words) / quote_word_count))}%\n'
                            f'\nwords per minute: {int(quote_word_count * 60 / total_time)}')
    window.after(1, stop_typing_f)


window = Tk()
window.title("Speed Typing Test")
window.config(padx=20, pady=20)

canvas = Canvas(width=800, height=450)
background_img = PhotoImage(file="background.png")
canvas.create_image(400, 225, image=background_img)
quote_text = canvas.create_text(400, 225, text=quote, width=700, font=("Bebas Neue", 24, "bold"), fill="white")
canvas.grid(row=0, column=0, columnspan=2)

# quote_text = Label(text=quote, height=10, width=10, wraplength=500, justify="center", bg="yellow",
#                    font=("Arial", 24))
# quote_text.grid(row=0, column=0)

text_entry = Text(height=10, width=70)
text_entry.grid(row=1, column=0, padx=10, pady=10)

results = Label(text="To begin, simply start typing.\n\n When you complete typing the sentence above, you will get "
                     "your "
                     "results.", height=10, width=25, bg=GREEN, relief=RAISED, wraplength=150)
results.grid(row=1, column=1)
start_button = Button(text="New sentence", command=try_again, font=("Arial", 16, "bold"))
start_button.grid(row=2, column=0)

window.after(1, start_typing_f)
window.after(1, stop_typing_f)

window.mainloop()
