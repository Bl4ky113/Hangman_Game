# Made By Bl4ky113

import tkinter as tk
from tkinter import ttk
from typing import ForwardRef

bg_color = "#333333"
fg_color = "#e9e9e9"

def tkinter_wrapper (tk_element, pack_options=()):
    """ Creates a wrapper and return the wrapper item """
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
    """ Styled tkinter text creator """
    def title (self, tk_element, pack_options=(), content=""):
        """ Creates a title styled text """
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
        """ Creates a Simple styled text """
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
        """ Creates a styled text for the letters or word (not certain) of the word to guess. """        
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
        """ Creates a styled text with my personal-"artist" signature """
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
    """ Styled tkinter input creator """
    def btn_input (self, tk_element, onclick, content="", pack_options=""):
        """ Creates a Styled tkinter btn """
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
        """ Creates a Styled Tkinter text input """
        input_color = f"#{int(bg_color[1:]) - 111111}"

        text_input = tk.Entry(
            tk_element,
            textvariable= output_variable,
            justify="center",
            border=0,
            font=("Arial Black", 20),
            foreground=fg_color,
            background=input_color,
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

class tkinter_canvas ():
    """ Tkinter hangman-canvas class, contains the creator of the canvas and draw the progress of the "hang" """
    def __init__ (self, tk_element, width, height, pack_option):
        """ Creates the Canvas """
        canvas_bg_color = f"#{int(bg_color[1:]) - 111111}"
        self.canvas_item_ids = []
        self.cw = width
        self.ch = height

        self.canvas = tk.Canvas(
            tk_element,
            background=canvas_bg_color,
            border=0,
            width=self.cw,
            height=self.ch
        )
        self.canvas.pack(
            side=pack_option,
            padx=10,
            pady=10
        )

    def drawBase (self):
        """ Draws something to hang the man. The begining of the "hang" process (0/) """
        self.canvas.create_polygon(
            (self.cw * 0.15), (self.ch * 0.8), 
            (self.cw * 0.15), (self.ch * 0.7), 
            (self.cw * 0.2), (self.ch * 0.7), 
            (self.cw * 0.2), (self.ch * 0.15),
            (self.cw * 0.6), (self.ch * 0.15),
            (self.cw * 0.6), (self.ch * 0.25),
            (self.cw * 0.56), (self.ch * 0.25),
            (self.cw * 0.56), (self.ch * 0.2),
            (self.cw * 0.24), (self.ch * 0.2),
            (self.cw * 0.24), (self.ch * 0.7),
            (self.cw * 0.29), (self.ch * 0.7),
            (self.cw * 0.29), (self.ch * 0.8),
            (self.cw * 0.15), (self.ch * 0.8),
            fill=fg_color,
            width=4
        )

    def drawHead (self):
        """ Draws the head of the man. (1/) """
        self.canvas.create_oval(
            (self.cw * 0.5), (self.ch * 0.3),
            (self.cw * 0.66), (self.ch * 0.46),
            fill=fg_color
        )

    def drawBody (self):
        """ Draws the Body and Arms of the man. (2/) """
        self.canvas.create_rectangle(
            (self.cw * 0.54), (self.ch * 0.4),
            (self.cw * 0.6), (self.ch * 0.6),
            fill=fg_color,
            outline=fg_color
        )

        self.canvas.create_line(
            (self.cw * 0.54), (self.ch * 0.4),
            (self.cw * 0.70), (self.ch * 0.56),
            fill=fg_color,
            width=10
        )

        self.canvas.create_line(
            (self.cw * 0.6), (self.ch * 0.4),
            (self.cw * 0.44), (self.ch * 0.56),
            fill=fg_color,
            width=10   
        )