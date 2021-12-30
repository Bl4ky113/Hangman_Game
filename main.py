# Made By Bl4ky113

import tkinter as tk
from tk_classes import tkinter_text, tkinter_wrapper, tkinter_input
import os 


def main (): 
    base_tk = tk.Tk(className="Hangman The Game")

    # Calc the size of the base_tk. 3/4 of the user screen on with and height
    screen_width = base_tk.winfo_screenwidth()
    screen_height = base_tk.winfo_screenheight()
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

    # Tkinter items creators.
    text_creator = tkinter_text()
    inputs_creator = tkinter_input()
 
    # Header and Bl4ky113
    header_wrapper = tkinter_wrapper(base_tk, (0, "x", "top"))
    text_creator.title(header_wrapper, ("both", "left"), "Hangman")
    text_creator.text(header_wrapper, ("both", "right"), "Try To Guess The Word")

    bl4ky_wrapper = tkinter_wrapper(base_tk, (0, "x", "top"))
    text_creator.bl4ky(bl4ky_wrapper, ("x", "top"))

    # Main 
    main_wrapper = tkinter_wrapper(base_tk, (1, "both", "top"))

    # Footer
    footer_wrapper = tkinter_wrapper(base_tk, (0, "x", "bottom"))
    inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Skip Word", "top")
    inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Change Word List", "right")
    inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Create Word List", "right")

    base_tk.mainloop()

if __name__ == "__main__":
    main()