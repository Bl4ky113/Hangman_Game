# Made By Bl4ky113

import tkinter as tk
from tkinter import ttk

bg_color = "#333333"
fg_color = "#e9e9e9"

def colorChanger (base_color, added_color, mode="+"):
    """ Takes a hexadecimal color and adds other hexadecimal color. Returning the result as a string """  
    operator = 1
    if mode == "-":
        operator = -1

    new_color = f"#{hex(int(base_color[1:], 16) + (int(added_color, 16) * operator))[2:]}"

    return new_color

def tkinter_wrapper (tk_element, pack_options=()):
    """ Creates a Frame wrapper and return the wrapper item """
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
        title_bg_color = colorChanger(bg_color, "111111")

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
            anchor="center",
            justify="center",
            text=content
        )
        text_element.pack(
            expand=0,
            fill=pack_options[0],
            side=pack_options[1],
        )

    def word_to_guess (self, tk_element, pack_options=(), content="", font_size=20, wrap_len=0):
        """ Creates a styled text for the letters or word (not certain) of the word to guess. """
        word_bg_color = colorChanger(bg_color, "151515")
        
        text_element = ttk.Label(
            tk_element,
            padding=(5, 10),
            font=("Arial Black", font_size, "underline"),
            foreground=fg_color,
            background=word_bg_color,
            text=content,
            wraplength=wrap_len,
            justify="center",
            anchor="center"
        )
        text_element.pack(
            expand=1,
            fill=pack_options[0],
            side=pack_options[1]
        )

        return text_element

    def score (self, tk_element, content, pack_option=()):
        """ Creates a styled text for the score of the game """
        score_bg_color = colorChanger(bg_color, '111111', mode="-")

        score_element = ttk.Label(
            tk_element,
            padding=(10, 2),
            font=("consolas", 14, "underline"),
            foreground=fg_color,
            background=score_bg_color,
            text=content
        )
        score_element.pack(
            expand=0,
            fill=pack_option[0],
            side=pack_option[1]
        )

        return score_element

    def bl4ky (self, tk_element, pack_options=()):
        """ Creates a styled text with my personal-"artist" signature """
        text_element = ttk.Label(
            tk_element,
            padding=(10, 2),
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
        input_color = colorChanger(bg_color, "111111")
        active_input_color = colorChanger(bg_color, "222222")

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
        input_color = colorChanger(bg_color, "111111", mode="-")

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
            side=pack_options[0],
            anchor=pack_options[1]
        )

    def listbox_input (tk_element, list_options=[], pack_options=()):
        list_box = tk.Listbox(
            tk_element,
            background=bg_color,
            foreground=fg_color,
            font=("Arial Black", 12),
            border=0,
        )

        index_options = 0
        for option in list_options:
            list_box.insert(index_options, option)
            index_options += 1

        list_box.pack(
            padx=20,
            pady=5,
            expand=1,
            fill=pack_options[0],
            side=pack_options[1]
        )

        return list_box

    def textbox_input (tk_element, pack_options=()):
        """ Creates a Styled Tkinter text input """
        parent_height = tk_element.winfo_height()
        textbox_height = int(parent_height * 0.5) # element height is the 50% of the parent window (popup or tk_base)

        textbox = tk.Text(
            tk_element,
            background=bg_color,
            foreground=fg_color,
            font=("Arial Black", 16),
            blockcursor=True,
            border=2,
            relief="solid",
            height=textbox_height
        )
        textbox.pack(
            padx=20,
            pady=5,
            ipadx=10,
            ipady=10,
            expand=pack_options[0],
            fill=pack_options[1],
            side=pack_options[2]
        )

        return textbox

class tkinter_canvas ():
    """ Tkinter hangman-canvas class, contains the creator of the canvas and draw the initial progress of the "hang" """
    def __init__ (self, tk_element, width, height, pack_option):
        """ Creates the Canvas """
        canvas_bg_color = f"#{int(bg_color[1:]) - 111111}"
        self.canvas_item_ids = []
        self.current_step = 0
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

        self.drawStep0()

    def drawStep0 (self):
        """ Draws something to hang the man. The begining of the "hang" process (0/4) """
        self.canvas.create_polygon(
            (self.cw * 0.15), (self.ch * 0.8), 
            (self.cw * 0.15), (self.ch * 0.7), 
            (self.cw * 0.2), (self.ch * 0.7), 
            (self.cw * 0.2), (self.ch * 0.15),
            (self.cw * 0.58), (self.ch * 0.15),
            (self.cw * 0.58), (self.ch * 0.25),
            (self.cw * 0.56), (self.ch * 0.25),
            (self.cw * 0.56), (self.ch * 0.2),
            (self.cw * 0.24), (self.ch * 0.2),
            (self.cw * 0.24), (self.ch * 0.7),
            (self.cw * 0.29), (self.ch * 0.7),
            (self.cw * 0.29), (self.ch * 0.8),
            (self.cw * 0.15), (self.ch * 0.8),
            fill=fg_color,
            width=4,
            tags="step_0"
        )

    def drawStep1 (self):
        """ Draws the head of the man. (1/4) """
        self.canvas.create_oval(
            (self.cw * 0.5), (self.ch * 0.3),
            (self.cw * 0.66), (self.ch * 0.46),
            fill=fg_color,
            tags="step_1"
        )

    def drawStep2 (self):
        """ Draws the Body and Arms of the man. (2/4) """
        self.canvas.create_rectangle(
            (self.cw * 0.54), (self.ch * 0.4),
            (self.cw * 0.6), (self.ch * 0.6),
            fill=fg_color,
            outline=fg_color,
            tags="step_2"
        )

        self.canvas.create_line(
            (self.cw * 0.54), (self.ch * 0.4),
            (self.cw * 0.70), (self.ch * 0.56),
            fill=fg_color,
            width=12,
            tags="step_2"
        )

        self.canvas.create_line(
            (self.cw * 0.6), (self.ch * 0.4),
            (self.cw * 0.44), (self.ch * 0.56),
            fill=fg_color,
            width=12,
            tags="step_2"
        )

    def drawStep3 (self):
        """ Draws the legs of the man. (3/4) """
        self.canvas.create_line(
            (self.cw * 0.56), (self.ch * 0.58),
            (self.cw * 0.44), (self.ch * 0.7),
            fill=fg_color,
            width=15,
            tags="step_3"
        )

        self.canvas.create_line(
            (self.cw * 0.58), (self.ch * 0.58),
            (self.cw * 0.7), (self.ch * 0.7),
            fill=fg_color,
            width=15,
            tags="step_3"
        )

    def drawStep4 (self):
        """ Draws the rope around the man's neck and hangs him also writes on screen "hanged". (4/4) """
        rope_color = colorChanger(bg_color, '555555')

        self.canvas.create_polygon(
            (self.cw * 0.52), (self.ch * 0.44),
            (self.cw * 0.56), (self.ch * 0.44),
            (self.cw * 0.56), (self.ch * 0.23),
            (self.cw * 0.58), (self.ch * 0.23),
            (self.cw * 0.58), (self.ch * 0.44),
            (self.cw * 0.62), (self.ch * 0.44),
            (self.cw * 0.6), (self.ch * 0.46),
            (self.cw * 0.54), (self.ch * 0.46),
            (self.cw * 0.52), (self.ch * 0.44),
            fill=rope_color,
            tags="step_4"
        )

        self.canvas.create_text(
            (self.cw * 0.55), (self.ch * 0.9),
            font=("Arial Black", 20),
            justify="center",
            anchor="center",
            text="Hanged...",
            fill=rope_color,
            tags="step_4"
        )

class tkinter_popup ():
    def pop (self, funct, title="", content=""):
        # Tkinter Elements contructors
        text_creator = tkinter_text()
        inputs_creator = tkinter_input()

        self.popup = tk.Toplevel(
            background=bg_color,
            padx=30,
            pady=50
        )
        self.popup.wm_title(title)

        text_creator.title(self.popup, ("x", "top"), title)
        text_creator.text(self.popup, ("both", "top"), content)
        inputs_creator.btn_input(self.popup, funct, "Next", "top")

    def base_pop (self, title):
        popup = tk.Toplevel(
            background=bg_color,
            padx=30,
            pady=30
        )
        popup.wm_title(title)

        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()

        # Calc the size of the popup. 5/8 of the user screen on with and height
        popup_width = int(screen_width * 0.625)
        popup_height = int(screen_height * 0.625)
        popup_x_cord = int((screen_width - popup_width) / 2)
        popup_y_cord = int((screen_height - (popup_height + 20)) / 2) # + 20, of the window title and close, min window, fullscreen btns

        popup.geometry(f"{popup_width}x{popup_height}+{popup_x_cord}+{popup_y_cord}")

        return popup