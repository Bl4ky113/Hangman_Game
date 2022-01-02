# Made By Bl4ky113

import tkinter as tk
import json
from random import randrange
from os import listdir
from tk_classes import tkinter_canvas, tkinter_popup, tkinter_text, tkinter_wrapper, tkinter_input

# Tkinter items creators.
text_creator = tkinter_text()
inputs_creator = tkinter_input()
popup_creator = tkinter_popup()

global game_data
game_data = {
    "status": True,
    "score": 0
}

def nextRound (popup):
    """ Swaps to the next round, changing the word to guess and restarting the round. Gets called from a Popup """
    global game_data, word_data

    popup.destroy()

    if len(word_data["passed"]) == len(word_data["list"]):
        game_data["status"] = False
        popup_creator.pop(
            lambda: changeWordListMenu(popup_creator.popup), 
            "You have finished this list.", f"Now you can choose another list and keep playing. \nYour Total Score is: {game_data['score']}"
        )
    else:
        word_data["guessed_letters"] = []
        word_data["to_guess"] = chooseWordToGuess(word_data["list"], word_data["passed"])
        word_data["word_output"] = transformWordToOutput(word_data["to_guess"], word_data["guessed_letters"])

        hangProcess(step="all", delete_step=True)
        hangman.current_step = 0
        word_label.configure(text=word_data["word_output"])
        score_label.configure(text=game_data["score"])
        game_data["status"] = True

def getListOfWordList ():
    """ Gets a list of the Word Lists available in the game files """
    main_list = []

    list_languages = listdir("./files")
    for language in list_languages:
        list_files = listdir(f"./files/{language}")
        for file in list_files:
            if (file[-5:] == ".json"):
                file_name = f"{language}_{file.replace('.json', '')}"

                main_list.append(file_name)

    return main_list

def changeWordListMenu (popup_caller=any):
    """ Creates a Popup Where the user can select a list of words from the game files or from their files """

    # Deletes the popup who called this function
    try:
        popup_caller.destroy()
    except:
        pass

    # List of Word Lists available
    list_wordlist = getListOfWordList()

    # Creates the Base of the change Word List menu
    popup_base = popup_creator.base_pop("Change The Word List")

    # Header 
    header_wrapper = tkinter_wrapper(popup_base, (0, "x", "top"))
    text_creator.title(header_wrapper, ("x", "top"), "Change The Word List")

    bl4ky_wrapper = tkinter_wrapper(popup_base, (0, "x", "top"))
    text_creator.bl4ky(bl4ky_wrapper, ("x", "top"))

    # Main
    body_wrapper = tkinter_wrapper(popup_base, (1, "both", "top"))

    boxlist = tkinter_input.listbox_input(body_wrapper, list_wordlist, ("both", "top"))

    # Footer 
    footer_wrapper = tkinter_wrapper(popup_base, (0, "x", "bottom"))
    inputs_creator.btn_input(
        footer_wrapper, 
        lambda: changeWordList(boxlist, popup_base),
        "Change To the new List", 
        "right"
    )

    # inputs_creator.btn_input(footer_wrapper, lambda: print("change"), "Open Word List", "right")

def changeWordList (boxlist, popup):
    """ Updates the global word list and passed words with the chosen word list and empty or new arr. 
    Restarts the score and then starts a new round 
    """
    try:
        selected_file = boxlist.get(boxlist.curselection()[0])
        file_language = selected_file[:2]
        file_name = selected_file[3:]
    except:
        popup_creator.pop(lambda: popup_creator.popup.destroy(), "Error On Loading Word List", "Please Enter a Valid Word List")
        return

    global word_data, game_data
    word_data["list"] = getWordList(file_name, file_language)
    word_data["passed"] = []
    game_data["score"] = 0

    nextRound(popup)

def getWordList (list_name="simple_words", language="en"):
    """ Gets the list of words in a json file """
    list_url = f"./files/{language}/{list_name}.json"
    words_arr = []

    with open(list_url, "r", encoding="UTF-8") as list_file:
        list_dict = json.load(list_file)
        
        for word in list_dict["words"]:
            words_arr.append(word.lower())

    return words_arr

def chooseWordToGuess (word_list=[], already_passed_words=[]):
    """ Choose in the word list a word, ignoring the ones who already passed """
    posible_words_to_chose = []
    index_word_chosen = 0

    for word in word_list:
        if word not in already_passed_words:
            posible_words_to_chose.append(word)

    if len(posible_words_to_chose) != 1:
        index_word_chosen = randrange(len(posible_words_to_chose) - 1)

    word_chosen = posible_words_to_chose[index_word_chosen]
    already_passed_words.append(word_chosen)

    return word_chosen

def transformWordToOutput (word="", visible_chars=[]):
    """ Transform the word to gues in to a output, hidding the characters the player hasn't enter """
    transformed_word = ""

    for letter in word:
        if letter not in visible_chars and not letter.isspace():
            transformed_word += " * "
        else:
            transformed_word += letter

    return transformed_word.strip()

def checkInput (input_word):
    """ 
        Checks if the Entry Variable or the Text input last entry is in word_data["to_guess"]. 
        If its right shows the letter in the outputWord, if the output word and word to guess are the same. Win the round.
        If it isn't right moves 1 step the hangman progress. If the hangman gets hang, lose the round.
    """
    global game_data

    if len(input_word.get()) > 0 and game_data["status"]:
        input_letter = input_word.get()[-1]

        if input_letter.lower() in word_data["to_guess"] and input_letter.lower() not in word_data["guessed_letters"]:
            word_data["guessed_letters"].append(input_letter.lower())
            word_data["word_output"] = transformWordToOutput(word_data["to_guess"], word_data["guessed_letters"])
            word_label.configure(text=word_data["word_output"])

            # Calc the amount of score to add, for each letter of a word
            # If the word is more long than 10 chars large, it gives more points
            # If the word is smaller than 10 chars, it gives fewer points
            game_data["score"] += int(25 * (len(word_data["to_guess"]) / 10))
            score_label.configure(text=game_data["score"])

            if word_data["word_output"] == word_data["to_guess"]:
                game_data["status"] = False
                popup_creator.pop(
                    lambda: nextRound(popup_creator.popup), 
                    "You Win This Round", 
                    "You have won this round. Congrats, you have saved him!!!"
                )
        else:
            hangman.current_step += 1
            hangProcess(hangman.current_step)

            # Calc the amount of score to subtract, for each letter of a word
            # If the word is more long than 10 chars, it takes fewer points
            # If the word is smaller than 10 chars, it takes more points
            game_data["score"] -= int(12 * (10 / len(word_data["to_guess"])))
            score_label.configure(text=game_data["score"])

            if hangman.current_step >= 4:
                game_data["status"] = False
                popup_creator.pop(
                    lambda: nextRound(popup_creator.popup), 
                    "You Lose This Round", 
                    "You have lost this round. You have killed him, monster."
                )

        input_word.set(input_letter)
    
    else: 
        input_word.set("")

def skipWord ():
    global game_data

    if game_data["status"]:
        game_data["score"] -= int(30 * (10 / len(word_data["to_guess"])))

        popup_creator.pop(
            lambda: nextRound(popup_creator.popup),
            "You Have Skiped This Word",
            "Atleast you tried, right?"
        )

def hangProcess (step=0, delete_step=False):
    """ Controls the progress of the hang process. Can Draw or delete each step """
    if delete_step:
        if step == "all":
            hangman.canvas.delete("all")
            hangman.drawStep0()
        else:
            hangman.canvas.delete(f"step_{step}")
    else:
        getattr(hangman, f"drawStep{step}")()

def main ():
    """ Main Function """

    # Get the Initial Word data 
    global word_data, hangman, word_label, score_label
    word_data = {
        "list": getWordList(),
        "passed": [],
        "guessed_letters": []
    }
    word_data["to_guess"] = chooseWordToGuess(word_data["list"], word_data["passed"])
    word_data["output"] = transformWordToOutput(word_data["to_guess"], word_data["guessed_letters"])

    # Display The Main Base
    base_tk = tk.Tk(className="Hangman The Game")

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
    wrap_len = int(base_width * 0.6) # Calc the wrap size of the letters in the wrapper.

    font_size = 40 # Calc the size of the font in the word to guess
    if len(word_data["to_guess"]) > 10:
        font_size = 30
    elif len(word_data["to_guess"]) > 15:
        font_size = 25
    elif len(word_data["to_guess"]) > 20:
        font_size = 20

    word_wrapper = tkinter_wrapper(content_wrapper, (1, "both", "left"))
    word_label = text_creator.word_to_guess(word_wrapper, ("x", "left"), word_data["output"], font_size, wrap_len)
    
    score_wrapper = tkinter_wrapper(content_wrapper, (0, "x", "bottom"))
    score_label = text_creator.score(score_wrapper, game_data["score"], ("x", "top"))

    # Hangman Icon
    # Calc the size of the hangman canvas. 35% width and 46% height of the base_tk
    canvas_width = int(base_width * 0.35)
    canvas_height = int(base_height * 0.45)

    hangman = tkinter_canvas(content_wrapper, canvas_width, canvas_height, "right")

    # Text Input
    entry_variable = tk.StringVar()
    entry_variable.trace_add("write", lambda x, y, z: checkInput(entry_variable))

    input_wrapper = tkinter_wrapper(base_tk, (1, "x", "top"))
    inputs_creator.txt_input(input_wrapper, entry_variable, ("top", "center"))

    # Footer
    footer_wrapper = tkinter_wrapper(base_tk, (0, "x", "bottom"))
    inputs_creator.btn_input(footer_wrapper, skipWord, "Skip Word", "top")
    inputs_creator.btn_input(footer_wrapper, changeWordListMenu, "Change Word List", "right")
    # inputs_creator.btn_input(footer_wrapper, lambda: print("hello"), "Create Word List", "right")

    base_tk.mainloop()

if __name__ == "__main__":
    main()