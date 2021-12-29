# Made By Bl4ky113

import tkinter as tk
from tkinter import ttk

bg_color = "#333"
fg_color = "#e9e9e9"

base_color = "#2601ff"
dark_color = "#1c00c0"

def tkinter_wrapper (tk_element, pack_options=()):
    wrapper = tk.Frame(
        tk_element,
        bg=fg_color
    )
    wrapper.pack(
        expand=pack_options[0],
        fill=pack_options[1],
        side=pack_options[2]
    )

    return wrapper

class tkinter_text ():
    def title (self, tk_element, pack_options=(), content=""):
        title_bg_color = f"#{int(bg_color[1:]) + 111}"

        title_element = ttk.Label(
            tk_element,
            padding=(20, 5),
            font=("Bahmschift SemiBold", 24, "underline"),
            foreground=fg_color,
            background=title_bg_color,
            text=content,
            anchor="center"
        )
        title_element.pack(
            expand=1,
            fill=pack_options[0],
            side=pack_options[1],
        )

    def text (self, tk_element, pack_options=(), content=""):
        text_element = ttk.Label(
            tk_element,
            padding=(20, 5),
            font=("Arial Greek", 16),
            foreground=fg_color,
            background=bg_color,
            text=content
        )
        text_element.pack(
            expand=0,
            fill=pack_options[0],
            side=pack_options[1],
        )

    def bl4ky (self, tk_element, pack_options=()):
        text_element = ttk.Label(
            tk_element,
            padding=(10, 5),
            font=("Consolas", 12),
            foreground=fg_color,
            background=bg_color,
            text="// Made By Bl4ky113",
            anchor="center"
        )
        text_element.pack(
            expand=1,
            fill=pack_options[0],
            side=pack_options[1]
        )