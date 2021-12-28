# Made By Bl4ky113

import tkinter as tk
import os 


def main (): 
    base_tk = tk.Tk(className="Hangman The Game", screenName="Hangman The Game", baseName="Hangman The Game")

    screen_width = base_tk.winfo_screenwidth()
    screen_height = base_tk.winfo_screenheight()
    base_width = int(screen_width * 0.75)
    base_height = int(screen_height * 0.75)
    base_x_align = int((screen_width - base_width) / 2)
    base_y_align = int((screen_height - (base_height + 20)) / 2)

    base_tk.geometry(f"{base_width}x{base_height}+{base_x_align}+{base_y_align}")

    base_tk.mainloop()

if __name__ == "__main__":
    main()