# Made By Bl4ky113

import tkinter as tk
from tk_classes import tkinter_canvas, tkinter_text, tkinter_wrapper, tkinter_input
import os 

# Tkinter items creators.
text_creator = tkinter_text()
inputs_creator = tkinter_input() 

def main ():
    word_to_guess = "hello"

    # Display The Main Page
    base_tk = tk.Tk(className="Hangman The Game")

    entry_variable = tk.StringVar()

    screen_width = base_tk.winfo_screenwidth()
    screen_height = base_tk.winfo_screenheight()

    # Calc the size of the base_tk. 3/4 of the user screen on with and height
    base_width = int(screen_width * 0.75)
    base_height = int(screen_height * 0.75)
    base_x_align = int((screen_width - base_width) / 2)
    base_y_align = int((screen_height - (base_height + 20)) / 2) # + 20, of the window title and close, min window, fullscreen btns

    base_tk.geometry(f"{base_width}x{base_height}+{base_x_align}+{base_y_align}")
    base_tk.configure(
        bg="#333",
        padx=20,
        pady=20
    )

    # Header and Bl4ky113
    header_wrapper = tkinter_wrapper(base_tk, (0, "x", "top"))
    text_creator.title(header_wrapper, ("both", "left"), "Hangman")
    text_creator.text(header_wrapper, ("both", "right"), "Try To Guess The Word")

    bl4ky_wrapper = tkinter_wrapper(base_tk, (0, "x", "top"))
    text_creator.bl4ky(bl4ky_wrapper, ("x", "top"))

    # Main 
    main_wrapper = tkinter_wrapper(base_tk, (1, "both", "top"))
    # Word to Guess and Hangman Icon
    content_wrapper = tkinter_wrapper(main_wrapper, (1, "both", "top"))
    # Word To Guess
    word_wrapper = tkinter_wrapper(content_wrapper, (1, "both", "left"))
    for letter in word_to_guess:
        text_creator.word_to_guess(word_wrapper, ("x", "left"), letter)

    # Hangman Icon
    # Calc the size of the hangman canvas. 35% width and 50% height of the base_tk
    canvas_width = int(base_width * 0.35)
    canvas_height = int(base_height * 0.5)

    hangman = tkinter_canvas(content_wrapper, canvas_width, canvas_height, "right")
    hangman.drawBase()
    hangman.drawHead()
    hangman.drawBody()
    hangman.drawLegs()
    hangman.drawRope()

    # Text Input
    input_wrapper = tkinter_wrapper(base_tk, (1, "x", "top"))
    inputs_creator.txt_input(input_wrapper, entry_variable, ("both", "top", "center"))

    # Footer
    footer_wrapper = tkinter_wrapper(base_tk, (0, "x", "bottom"))
    inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Skip Word", "top")
    inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Change Word List", "right")
    inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Create Word List", "right")

    base_tk.mainloop()

if __name__ == "__main__":
    main()