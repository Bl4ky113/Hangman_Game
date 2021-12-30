# Made By Bl4ky113

import tkinter as tk
from tkinter import ttk

bg_color = "#333333"
fg_color = "#e9e9e9"

def tkinter_wrapper (tk_element, pack_options=()):
    wrapper = tk.Frame(
        tk_element,
        bg=bg_color
    )
    wrapper.pack(
        expand=pack_options[0],
        fill=pack_options[1],
        side=pack_options[2]
    )

    return wrapper

class tkinter_text ():
    def title (self, tk_element, pack_options=(), content=""):
        title_bg_color = f"#{int(bg_color[1:]) + 111111}"

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

    def word_to_guess (self, tk_element, pack_options=(), content=""):
        word_bg_color = f"#{hex(int(bg_color[1:], 16) + int('151515', 16))[2:]}"
        
        text_element = ttk.Label(
            tk_element,
            padding=(20, 10),
            font=("Arial Black", 18, "underline"),
            foreground=fg_color,
            background=word_bg_color,
            text=content,
            anchor="center"
        )
        text_element.pack(
            expand=1,
            fill=pack_options[0],
            side=pack_options[1]
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

class tkinter_input ():
    def btn_input (self, tk_element, onclick, content="", pack_options=""):
        input_color = f"#{int(bg_color[1:]) + 111111}"
        active_input_color = f"#{int(bg_color[1:]) + 222222}"

        btn = tk.Button(
            tk_element,
            font=("Arial Greek", 14),
            text=content,
            command=onclick,
            border=0,
            background=input_color,
            foreground=fg_color,
            activebackground=active_input_color,
            activeforeground=fg_color,
        )
        btn.pack(
            ipadx=5,
            padx=5,
            side=pack_options
        )

    def txt_input (self, tk_element, output_variable, pack_options=()):
        input_color = f"#{int(bg_color[1:]) - 111111}"
        active_input_color = f"#{int(bg_color[1:]) - 111111}"

        text_input = tk.Entry(
            tk_element,
            textvariable= output_variable,
            justify="center",
            border=0,
            font=("Arial Black", 20),
            foreground=fg_color,
            background=input_color,
            highlightbackground=active_input_color,
            insertbackground=fg_color,
            insertwidth=5,
        )
        text_input.pack(
            ipadx=10,
            ipady=10,
            padx=5,
            pady=5,
            expand=1,
            side=pack_options[1],
            anchor=pack_options[2]
        )
